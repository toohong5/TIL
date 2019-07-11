# 네이버 메일 보내기

import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

# msg = EmailMessage()
# msg['Subject'] = '배고파...'
# msg['From'] = 'tkfkd1909@naver.com'
# msg['To'] = 'toohong5@gmail.com', '91hongppie@gmail.com', 'dave.juya777@gmail.com'
# msg.set_content('치킨사줘..')

# ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
# ssafy.login('tkfkd1909', password)
# ssafy.send_message(msg)

# print('이메일 전송 완료!')


# for문 이용

to_email_list = ['toohong5@gmail.com', '91hongppie@gmail.com', 'dave.juya777@gmail.com']

for email in to_email_list:
    msg = EmailMessage()
    msg['Subject'] = '배고파...'
    msg['From'] = 'tkfkd1909@naver.com'
    msg['To'] = email
    msg.set_content('치킨사줘..')
    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('tkfkd1909', password)
    ssafy.send_message(msg)

    print('이메일 전송 완료!')