from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pyautogui

def input2(pa):
    pp=str(pyautogui.prompt(pa))
    return pp

#give a information
your_address = input2('your email address:')
your_password = pyautogui.password('your password:')
to_address = input2('send to email address:')
Subject = input2('select a subject:')
a=pyautogui.confirm('do you send file?','file',['yes','no'])

# create message object instance
msg = MIMEMultipart()
 
 
message = input2('write your message:')
 
# setup the parameters of the message
password = your_password
msg['From'] = your_address
msg['To'] = to_address
msg['Subject'] = Subject 
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
pyautogui.alert("successfully sent email to "+str(to_address))
