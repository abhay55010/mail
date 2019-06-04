import smtplib
import imghdr
import os
from email.message import EmailMessage

EMAIL_ADDRESS=os.environ.get('##############@gmail.com')
EMAIL_PASSWORD=os.environ.get('###########')
msg=EmailMessage()
msg['Subjecct']='this is for image'
msg['From']=EMAIL_ADDRESS
msg['To']='#############@gmail.com'
msg.set_content('image attached')
with open('test.jpg','rb')as f:
          file_data=f.read()
          file_type=imghdr.what(f.name)
          file_name=f.name
          
msg.add_attachment(file_data,maintype='image',subtype='file_type',filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
    smtp.login('################@gmail.com','###########')
    smtp.send_message(msg)
