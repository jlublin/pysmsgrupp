#!/usr/bin/env python

import sys
import requests
import getpass

phone_number = '<phone number>'
password = '<password>'
gid = '<group id>'

if(len(sys.argv) < 2):
	print 'Usage: %s \'<text message>\'' % sys.argv[0]
	exit()

sms_text = sys.argv[1]

if(phone_number == '' || type(phone_number != str)):
    phone_number = raw_input('Phone number: ')

if(password == '' || type(password != str)):
    password = getpass.getpass()

if(gid == '' || type(gid != str)):
    gid = raw_input('Groud ID: ')

s = requests.Session()

d = s.post('http://smsgrupp.se/', {'number' : phone_number, 'password' : password})

d = s.get('http://smsgrupp.se/weblogic/send_sms_to_group.php', params={'gid' : gid, 'deliver' : 'now', 'msg' : sms_text, 'self_send' : 'true'})

if(d.text == '{"status":"ok"}'):
    print 'SMS sent'
else:
    print 'Error: ' + d.text

