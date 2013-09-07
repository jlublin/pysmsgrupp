#!/usr/bin/env python

import sys
import requests

phone_number = 'phone number'
password = 'password'
gid = 'group id'

if(len(sys.argv) < 2):
	print 'Usage: %s \'<text message>\'' % sys.argv[0]
	exit()

sms_text = sys.argv[1]

s = requests.Session()

d = s.post('http://smsgrupp.se/', {'number' : phone_number, 'password' : password})

d = s.get('http://smsgrupp.se/weblogic/send_sms_to_group.php', params={'gid' : gid, 'deliver' : 'now', 'msg' : sms_text, 'self_send' : 'true'})

if(d.text == '{"status":"ok"}'):
    print 'SMS sent'
else:
    print 'Error: ' + d.text

