import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd
import numpy as np



#make a string of URL of desired product
url="https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGLM366/ref=asc_df_B07HGLM366/?tag=googleshopdes-21&linkCode=df0&hvadid=397076931806&hvpos=&hvnetw=g&hvrand=9023911045069890752&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300154&hvtargid=pla-921590129718&psc=1&ext_vrnc=hi"


#------------------------creating header---------------------------------------------

'''
HTTP headers User-Agent :It is a request header that allows a characteristic 
        string that allows network protocol peers to identify the Operating System and 
        Browser of the web-server.  


for more info : https://www.geeksforgeeks.org/http-headers-user-agent/#:~:text=The%20HTTP%20headers%20User%2DAgent,Browser%20of%20the%20web%2Dserver.
'''
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
'''
The following conclusions can be drawn with the help of user-agent header:

The user agent application is Mozilla version 5.0.
The operating system is NT version 10.0 (and is running on a Windows(64-bit) Machine).
The engine responsible for displaying content on this device is AppleWebKit version 537.36 (KHTML, an open-source layout engine, is present too).
The client is Chrome version 74.0.3729.169
The client is based on Safari version 537.36.

'''
#--------------------------End----------------------------------------------------------------


#----------------Geting the webpage which is specified in "url"-----------------------------
page=requests.get(url,headers=headers)
#-----------------END-------------------------------------------------------------------


#------------creating BeautifulSoup Object---------------------------------------------
#This is done by passing the html to the BeautifulSoup() function.The BeautifulSoup
# package is used to parse the html, that's take the raw html text and break into python
# objects.
soup=BeautifulSoup(page.content,'html.parser')

#soup object allows us to extract interesting information about the website you're
# scraping such as getting the title of the page, you can also get the text of
# webpage and quickly print it out to check if it is what you expect

#--------------END---------------------------------------------------------------------



'''
#----------------product information----------------------------------
#produxt title
print(soup.title)

#get attribute
print(soup.title.name)

#get value
print(soup.title.string)

#beginning navigation
print(soup.title.parent.name)

#getting specific values
print(soup.p)


#all paragraph tag value
print(soup.find_all('p'))


# In[8]:


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    #  or print(str(paragraph.text))


# In[9]:


for url in soup.find_all('a'):
    print(url.get('href'))


# In[10]:


print(soup.get_text())


# In[11]:


a = soup.find(id = "productTitle")
b = a.get_text()


# In[12]:


print(b.strip())


# In[13]:

----------------------------------END-----------------------------------------------

'''



#accessing price as a Stirng in 'price' variable
price = soup.find(id="priceblock_ourprice")
#print(price.get_text())


#cp ex: ₹ 17,499 ,cp[0] = ₹ ,cp[1] = " " other are actual price
cp = price.get_text()
#print("cp:",cp)

#getiing actual price
s = cp[2:10]  # 17,499
#print("s:type:",type(s)) #price



#we have to remove "," from actual price
c = s.replace(",","")

#now convert string into float
c = float(c)

#print("C: ",c) #price in correct format
#print("type:",type(c))


def send_mail():
    # creates SMTP session 
    server =smtplib.SMTP("smtp.gmail.com",587)


    # identify ourselves to smtp gmail client
    server.ehlo()

    # start TLS for security 
    server.starttls() 

    # re-identify ourselves as an encrypted connection
    server.ehlo()

    # Authentication 
    # from which Email Id you want to send the mail(sender_mail_id, Password)
    server.login("xyz123---@gmail.com", "<Password>") 
    subject="Price down!"
    body="check out the amazon product link :https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGLM366/ref=asc_df_B07HGLM366/?tag=googleshopdes-21&linkCode=df0&hvadid=397076931806&hvpos=&hvnetw=g&hvrand=9023911045069890752&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300154&hvtargid=pla-921590129718&psc=1&ext_vrnc=hi"
    msg=f"Subject:{subject}\n\n{body}"
    
    # sending the mail
    server.sendmail(
        "-------@gmail.com",
        "-------@gmail.com",
        msg
    )
    #for our acknowledgement
    print("mail send")
    #Don't forget to terminate the session
    server.quit()



#main condition to check whether the prize goes down or not if it is, then send the mail 
#   to specified mails id

#17499 is cur price when you checked at first time
#(if price doesn't drop )for geting the mail ,you have to use '=='
if(c < 17499.0):
    send_mail()
