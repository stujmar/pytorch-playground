import os
import smtplib
from io import StringIO
from email.message import EmailMessage
import csv

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dev", action="store_true", help="development mode")
args = parser.parse_args()
config = vars(args)

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_RECIPIENT = os.environ['EMAIL_RECIPIENT']

my_data = [
    {
    'name': 'John',
    'age': 25,
    'job': 'gardener'
    },
    {
    'name': 'Jill',
    'age': 26,
    'job': 'teacher'
    },
    {
    'name': 'Jack',
    'age': 27,
    'job': 'programmer'
    },
    {
    'name': 'Jenny',
    'age': 28,
    'job': 'doctor'
    }
]

# Create a file-like object to receive the CSV data.
csvfile = StringIO()
# use the keys from the first dict as the fieldnames
fieldnames = my_data[0].keys()
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
for row in my_data:
    writer.writerow(row)

# Old hard way.
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

message = EmailMessage()
if config['dev']:
    message['Subject'] = 'Dev email'
else:
    message['Subject'] = 'Production email'
message['From'] = EMAIL_ADDRESS
message['To'] = EMAIL_RECIPIENT
message.set_content('This is a test email.')
message.add_attachment(csvfile.getvalue(), filename='my_data.csv')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Old hard way.
    # subject = 'Test email'
    # body = 'This is a test email.'
    # msg = f'Subject: {subject}\n\n{body}'
    # smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECIPIENT, msg)
    smtp.send_message(message)
