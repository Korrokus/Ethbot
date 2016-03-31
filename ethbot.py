#!/usr/bin/python
# -*- coding: utf-8 -*-

###ethbot currently only supports G-Mail users, if intereset is there I'll add other smtp servers###


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import json
import urllib2
import time
import sys
import platform
from time import gmtime, strftime


system = platform.system()+platform.release()
gmail_user = "****" #gmail Username e.g. john.doe@gmail.com
gmail_pwd = "****" #password
try:
    alert = float(sys.argv[1]) #run the script with an number as an argument for the desired worth of ETH e.g. "python ethbot.py 12" sends an mail if ETH is worth 12$
except:
    alert = 100
coins = 20 #enter the amound of ETH - geth compatibility is coming in version 1.2
email = False
bot = "[EthBot-1.0]" #current version
freq = 20 #time in seconds - refreshs every x seconds


def mail(to, subject, text):
   msg = MIMEText(text)

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject
   


   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()
   



while True:
    if (strftime("%H:%M", gmtime()) == "08:06"): #sets email to True so does not send multiple mails, change hour(08) or minute(06) to your schedule
        email = True

    try:
        stats = json.loads(urllib2.urlopen("http://coinmarketcap-nexuist.rhcloud.com/api/eth/price").read())

    
        worth = stats["usd"]*coins #change "eur" to "usd" for us dollars

        subject = "%s: Ethereum is now at %s $" % (bot,str(stats["usd"]))
        text = "Your %6.2f coins are now %6.2f$ worth!\n\nSend from %s @ %s " % (coins,worth,system,bot) 

        if (stats["usd"] > alert):
            print "%s: Goal of %s reached! Sending out Mail..  " % (bot,alert)
            print "%s: Done." % bot
            mail(gmail_user,subject,text)
            break
        else:
            print "%s: Checking status until ETH is over" % bot,alert," | Currently at %s" % (str(stats["usd"]))
            
            time.sleep(freq)
            
    except:
        print "%s: API seems to be offline, trying again in %ss..." % (bot,freq)
        time.sleep(freq)
        pass

    if (email == True):

        print "%s: Sending daily update-mail..." % bot
        mail("skreeler@gmail.com","Daily Update for ETHER",subject)
        print "%s: Done." % bot
        email = False
    else:
        pass    


