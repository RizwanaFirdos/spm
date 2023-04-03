import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('pathanrizwanafirdos@gmail.com','vwqfiysuixvokmjx')
    msg=EmailMessage()
    msg['From']='pathanrizwanafirdos@gamil.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

    







        
    
