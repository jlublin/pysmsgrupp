#!/usr/bin/env python

import sys
import requests
import getpass

# Edit the following options
# Leave blank ('') to get asked for the parameter when running the program

phone_number = '<phone number>'
password = '<password>'
gid = '<group id>'

# End of parameters

if(len(sys.argv) < 2):
	print 'Usage: %s \'<text message>\'' % sys.argv[0]
	exit()

sms_text = sys.argv[1]

if(phone_number == '' or type(phone_number != str)):
    phone_number = raw_input('Phone number: ')

if(password == '' or type(password != str)):
    password = getpass.getpass()

if(gid == '' or type(gid != str)):
    gid = raw_input('Groud ID: ')

# Session which saves cookies
s = requests.Session()

# Login
d = s.post('http://smsgrupp.se/', {'number' : phone_number, 'password' : password})

# Send message
d = s.get('http://smsgrupp.se/weblogic/send_sms_to_group.php', params={'gid' : gid, 'deliver' : 'now', 'msg' : sms_text, 'self_send' : 'true'})

if(d.text == '{"status":"ok"}'):
    print 'SMS sent'
else:
    print 'Error: ' + d.text

