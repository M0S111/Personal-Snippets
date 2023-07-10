from email.message import EmailMessage
import os,mimetypes,smtplib,getpass

message = EmailMessage()

sender = 'stormbrewer@yandex.com'
recipient = 'berkahabid99@gmail.com'

message['From'] = sender
message['To'] = recipient

message['Subject'] = 'From your brother.'

body = 'To my darling sister.'

message.set_content(body)

attach_path = '/storage/emulated/0/DCIM/100ANDRO/DSC_0051.JPG'
attach_file = os.path.basename(attach_path)

mime_type, mime_subtype = mimetypes.guess_type(attach_path)

mime_type,mime_subtype = mime_type.split('/',1)

print(mime_type)
print(mime_subtype)

with open(attach_path,'rb') as ap:
	message.add_attachment(ap.read(),maintype = mime_type,subtype = mime_subtype,filename = os.path.basename(attach_path))
	
m_server = smtplib.SMTP_SSL('smtp.gmail.com')

m_pass = getpass.getpass('Password? ')

m_server.login(sender,m_pass)
