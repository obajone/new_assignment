
def get_name_emails(file_name_in_string):
    with open(file_name_in_string, 'r') as e:
        doc = e.read().split('\n')
    names = []
    email = []
    for i in range(0, len(doc)):
        first_name = doc[i].split()[0][0].upper() + doc[i].split()[0][1:]
        last_name = doc[i].split()[1][0].upper() + doc[i].split()[1][1:-1]
        full_name = f'{first_name} {last_name}'
        names.append(full_name)
        emails_a = doc[i].split()[2]
        email.append(emails_a)
    name_email_dict = dict(zip(names, email))
    return name_email_dict

from smtplib import SMTP
import smtplib

server = 'smtp.gmail.com'
port = 465
sender = 'adelekeo254@gmail.com'
password = '4943@Adeleke'
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    for name, email in get_name_emails('Emails.txt').items():
        msg = f'Hi, {name}! Please, come home.'
        server.sendmail(sender, email, msg)



   
   
   
   

