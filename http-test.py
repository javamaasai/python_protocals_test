#!/usr/bin/env python3

import httplib2

# Demonstrating Usage of The httplib2 module 
# comprehensive HTTP client library

#Function print_lines_with_prefix(strg, prefx)
#For printing lines in string with a prefix
def print_lines_with_prefix(strg, prefx):	
	for line in strg.split('\n'):
		print (prefx + line);

h = httplib2.Http(".cache")
resp, content = h.request("http://localhost:8080/", "GET")

print ()
print ("----------------------------------------------------")
print (" Http test Response")
print ("----------------------------------------------------")
print_lines_with_prefix(content.decode('utf-8'), "|- ")
print ("----------------------------------------------------")