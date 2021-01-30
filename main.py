#to grab data from url
import requests
#this imports elements from url
from bs4 import BeautifulSoup
import smtplib

URL= '''URL OF YOUR AMAZON PRODUCT'''

#get your browser user agent
headers= {" YOUR BROWSER USER AGENT "}


def checkprice():
    page= requests.get(URL, headers= headers)

    #extracting relevant information like title etc..
    soup= BeautifulSoup(page.content, 'html.parser')
    price= soup.find(id= "priceblock_ourprice").get_text()
    #CONVERTING PRICE INTO FLOAT
    converted_price=float("".join(d for d in price if d.isdigit()))
    

    if (converted_price < PRICE YOU DESIRE):
        send_mail()
    


def send_mail():
    #gmail server
    server= smtplib.SMTP('smtp.gmail.com', 587)
    #to esatblish connection
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(' YOUR MAIL ID', ' PASSWORD ')

    subject= 'Price Fell Down'
    body= f"Check the amazon link: {URL}"

    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        ' MAIL ID',
        ' TARGETED MAIL ID ',
        msg
    )
    print("Hey Email Has been Sent!")

    server.quit()

checkprice()