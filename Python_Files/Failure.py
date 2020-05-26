#!/usr/bin/env python
# coding: utf-8

# In[8]:


import smtplib
from email.message import EmailMessage

sender_mail="shoumiksahu2000@gmail.com"
rec_mail="sahushoumik23@gmail.com"
password="Testing2000"
msg = EmailMessage()
msg.set_content('The model you sent is not having above 80%  accuracy, so we are modifying it for you...\n\nThank You,\nJenkins,\nDevOps.')

msg['Subject'] = 'Model is not very accurate 2 '
msg['From'] = sender_mail
msg['To'] = rec_mail

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_mail,password)
print("Login Success")
server.send_message(msg)
print("Email has been sent to ",rec_mail)
server.quit()


# In[ ]:




