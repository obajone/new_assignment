
# server = 'smtp.gmail.com'
# port = 465
sender = input("Enter sender's email in string: ")
password = input("Enter sender's password in string: ")

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


def sendEmail(sender, password, name_email_function):
    from smtplib import SMTP
    import smtplib
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        for name, email in name_email_function.items():
            msg = f"""Dear {name},
                    APPLICATION FOR THE POST OF ASSISTANT LECTURER, DEPARTMENT OF ENGLISH AND LITERARY STUDIES
                    I wish to apply for the position of Assistant Lecturer in the Department of English and Literary Studies in your institution. Along with my application, I am attaching my curriculum vitae for your assessment and consideration.
                    I am a product of Delta State University and I have seven years experience in research, teaching and examining students at the secondary and advanced levels. At present, I teach English as a Second Language (ESL) and Cambridge Literature at Chokhmah International Academy, Port Harcourt, Rivers State.
                    As a lecturer in Delta State University, I will bring a creative and positive energy along with a strong desire for literary productivity. My research interests include African Literature, Comparative Literature, Postcolonial Studies and Literary Criticism in general. In addition to this, I have a passion for creative writing, one which will enrich the English department.
                    I would welcome the opportunity of an interview to discuss my experience and qualifications with you in detail. """
            server.sendmail(sender, email, msg)





   
   
   
   

