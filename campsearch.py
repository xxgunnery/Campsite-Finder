import requests
import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from campdata import campsites

baseURL = "https://www.recreation.gov/api/camps/campgrounds/251869"
y = requests.get(
    baseURL,
    headers =
    {
        "User-Agent" : "Mozilla/5.0"
    }
)

campsites2 = []
response2 = y.json()
campsiteResponse = response2["campground"]["campsites"]
for site in campsiteResponse:
    converted = int(site)
    if converted < 99627:
        site = str(converted)
        campsites2.append(site)

print(str(len(campsites2)) + " campsites to look for in Many Glacier!")
print(str(len(campsites)) + " campsites to look for in Fish Creek!")
print("-------------------------------------")

x =  0
while x < len(campsites):
    campsites2.append(campsites[x])
    x+=1

#print(campsites)

message = MIMEMultipart('alternative')
me = 'pbdantonio@gmail.com'
subject = "Campground Availability Found at: "

campInfo = ""

x = 0
while(True):
    x+=1

    txtSent = "N"

    if x > 40:
        campgroundID = "Fish Creek"
    else:
        campgroundID = "Many Glaciers"

    baseURL = "https://www.recreation.gov/api/camps/availability/campsite/"
    startDate = "?start_date=2021-07-08T00%3A00%3A00.000Z"
    endDate = "&end_date=2021-07-12T00%3A00%3A00.000Z"

    reserveRequest = requests.get( 
    baseURL+campsites2[x]+startDate+endDate, 
    headers =
        {
            "User-Agent" : "Mozilla/5.0"
        }
    )
    #print(reserveRequest.status_code)
    if reserveRequest.status_code != 200:
        print("ERROR! " + str(reserveRequest.status_code))
        print(reserveRequest.content.decode())
        exit()
    else:
        response = reserveRequest.json()
        #print(response)

    availInfo = response["availability"]["availabilities"]
    #print(availInfo)

    x2=0
    for k in availInfo:
        x2 += 1
        campNight = k.split("T")[0]


        if (availInfo[k] != "Available") and (availInfo[k] != "Reserved"):
            print(availInfo[k])
            print(response["availability"]["campsite_id"])
            print(response["availability"]["campsite_type"])
            print(response["availability"]["campsite_reserve_type"])
            print(response["availability"]["type_of_use"])
            print("Not a site we can reserve...")
            print("----------------------------------")
            break
        elif (availInfo[k] == "Available"):
            if campgroundID == "Broken Arrow":
                if (campNight != "2021-07-11") and (campNight != "2021-07-10") and (campNight != "2021-07-08"):
                    newDiv = "<div>" + str(x) + " - " + "Campsite " + campsites[x] + " is " + availInfo[k] + " in " + campgroundID + " Campground on " + campNight + " | Time Processed: " + str(datetime.datetime.now().time()) + "</div>"
                    campInfo += newDiv
                    print(newDiv)
                    txtSent = "Y"
            elif campgroundID == "Many Glaciers":
                if (campNight != "2021-07-09") and (campNight != "2021-07-08"):
                    newDiv = "<div>" + str(x) + " - " + "Campsite " + campsites[x] + " is " + availInfo[k] + " in " + campgroundID + " Campground on " + campNight + " | Time Processed: " + str(datetime.datetime.now().time()) + "</div>"
                    campInfo += newDiv
                    print(newDiv)
                    txtSent = "Y"
            elif campgroundID == "Fish Creek":
                if (campNight != "2021-07-09") and (campNight != "2021-07-08"):
                    newDiv = "<div>" + str(x) + " - " + "Campsite " + campsites[x] + " is " + availInfo[k] + " in " + campgroundID + " Campground on " + campNight + " | Time Processed: " + str(datetime.datetime.now().time()) + "</div>"
                    campInfo += newDiv
                    print(newDiv)
                    txtSent = "Y"
        if x2 == len(availInfo):
            if txtSent != "Y":
                print(str(x) + " - We screwed for " + response["availability"]["campsite_id"] + " at " + campgroundID)
    
    if x == (len(campsites2) - 1):
        print("Looping around again...")
        x = 0
        if campInfo != "":
            subject = subject + campgroundID
            message["Subject"] = subject
            message["From"] = me
            message["To"] = me

            messageText = MIMEText(campInfo,"html")
            message.attach(messageText)

            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            server.ehlo()
            server.starttls()
            server.login( me, 'tvehujrljftbbkxh')
            server.sendmail(me,me,message.as_string())
            server.close()

            campInfo = ""
            
    elif (x == 20) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 41) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 60) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 80) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 100) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 120) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 140) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 160) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 180) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 200) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 220) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""
    elif (x == 240) and (campInfo != ""):
        subject = subject + campgroundID

        message["Subject"] = subject
        message["From"] = me
        message["To"] = me

        messageText = MIMEText(campInfo,"html")
        message.attach(messageText)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.ehlo()
        server.starttls()
        server.login( me, 'tvehujrljftbbkxh')
        server.sendmail(me,me,message.as_string())
        server.close()
        campInfo = ""

    time.sleep(3)








