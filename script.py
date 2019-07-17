import requests
from bs4 import BeautifulSoup
import urllib3
import random
import threading
from colorama import init
from termcolor import colored
import datetime

init()

raffleurl = 'https://reporting.jdsports.co.uk/cgi-bin/msite?yeezy_comp+a+0+0+0+0+0&utm_source=RedEye&utm_medium=Email&utm_campaign=Yeezy+Boost+350+Clay&utm_content=0805+Yeezy+Clay#SR'

sizes = ["3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12", "12.5", "13", "13.5", "14"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#headers

headers1 = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

}

global session
session = requests.session()

#INFORMATION

print(colored("JD | Yeezy Boost 350 V2 Antlia | BY @0CHARLIE01 | CharlieAIO#0001", "blue"))


def send():
    print(colored("Enter Number Of Entries ", "magenta"))
    numberoftasks = input()
    print(colored("Enter First Name", "cyan"))
    firstn = input()
    print(colored("Enter Last Name", "cyan"))
    lastn = input()
    print(colored("Enter Catchall", "cyan"))
    Catchall = input()
    print(colored("Enter Paypal Email", "cyan"))
    ppemail = input()
    print(colored("Enter Phone Country Code (e.g. For GB: +44)", "cyan"))
    countrycode = input()
    print(colored("Enter Phone Number Without Country Code ", "cyan"))
    mobilebase = input()
    fullnumber = countrycode + mobilebase
    print(colored("Enter Address Line 1", "cyan"))
    adddy1 = input()
    print(colored("Enter Address Line 2 (REQUIRED)", "cyan"))
    addy2 = input()
    print(colored("Enter City", "cyan"))
    addy3 = input()
    print(colored("Enter County", "cyan"))
    addy4 = input()
    print(colored("Enter Postcode", "cyan"))
    postcode = input()

    for i in range(int(numberoftasks)):
        p = datetime.datetime.now()
        print(colored(f"[{p}]Submitting Entry...", "green"))
        email = random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + Catchall
        shoesize = random.choice(sizes)

        urllib3.disable_warnings()
        sendload = {
            "comp_firstname": firstn,
            "comp_lastname": lastn,
            "comp_email": email,
            "paypal_email": ppemail,
            "comp_countrycode": countrycode,
            "comp_mobile_end": mobilebase,
            "comp_mobile": fullnumber,
            "shoesize": shoesize,
            "comp_address1": adddy1,
            "comp_address2": addy2,
            "comp_address3": addy3,
            "comp_address4": addy4,
            "comp_postcode": postcode,
            "emailhold": "on",
            "emailpermit": "1",
            "sms_optout": "",
            "submit": "ENTER NOW",
            "comp_yeezy_1":"1"

          }

        r = session.post(raffleurl, data=sendload, verify=False, headers=headers1)

        print(colored(f"Selected Shoe Size - [{shoesize}] UK", "green"))
        print(colored(f"Selected Email - [{email}]", "green"))
        print(colored(f"Entry Submitted ", "green"))

send()



