'''
- Python comes with built-in smtplib module for sending emails using the Simple Mail Transfer 
  Protocol (SMTP).smtplib uses the RFC 821 protocol for SMTP.

- We will use the Gmail SMTP server to send emails, but the same principles apply to other email
  services. 

- SMTP ports:
    Port 25: This is the default SMTP port. It is used for sending emails. 
             But it is unencrypted. 
             And also being blocked by many ISPs(Internet Service Providers).

    Port 465: This port is used for SMTP over SSL(Secure Socket Layer). It is encrypted. 
              But it is now considered deprecated.

    Port 587: This port is used for SMTP over TLS(Transport Layer Security). It is encrypted.


    **** Summary ****
    Port 25: Server-to-server SMTP (often blocked by ISPs for outbound mail).
    Port 587: Client-to-server SMTP (recommended, supports STARTTLS for encryption).
    Port 465: SMTP over SSL (deprecated, but still in use by some services).

    - Gmail: 587
    - Yahoo: 465
    - Outlook: 587
    - AOL: 587
    - AT&T: 465
'''

'''
Now, there are two options to send an email using Python:
1. Setting up Gmail 
2. Setting up a local SMTP server


If you decide to use a Gmail account to send your emails, I highly recommend setting up a
throwaway account for the development of your code. This is because you'll have to adjust your 
Gmail account's security settings to allow access from your Python code, and because there's a 
chance you might accidentally expose your login details. Also, I found that the inbox of my 
testing account rapidly filled up with test emails, which is reason enough to set up a new Gmail 
account for development.
 
A nice feature of Gmail is that you can use the + sign to add any modifiers to your email address, right before the @ sign. For example, mail sent to my+person1@gmail.com and my+person2@gmail.com will both arrive at my@gmail.com. When testing email functionality, you can use this to emulate multiple addresses that all point to the same inbox.

'''

### STARTING A SECURE SMTP CONNECTION
'''
When you send emails through Python, you should make sure that your SMTP connection is encrypted,
so that your message and login credentials are not easily accessed by others. SSL (Secure Sockets
Layer) and TLS (Transport Layer Security) are two protocols that can be used to encrypt an SMTP 
connection. It's not necessary to use either of these when using a local debugging server.

- There are two ways to start a secure connection with your email server:

    1. Start an SMTP connection that is secured from the beginning using SMTP_SSL().
    2. Start an unsecured SMTP connection that can then be encrypted using .starttls().

    In both instances, Gmail will encrypt emails using TLS, as this is the more secure successor of SSL.

    it is highly recommended that you use create_default_context() from the ssl module. This will 
    load the system's trusted CA certificates, enable host name checking and certificate 
    validation, and try to choose reasonably secure protocol and cipher settings.

'''

# CODE USING SMTP_SSL()
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "your@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# CODE USING .starttls()
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



###############
# Sending Fancy Emails: HTML Content
'''
Python's built-in email package allows you to structure more fancy email.

- If you want to format the text in your email (bold, italics, and so on), or if you want to add 
  any images, hyperlinks, or responsive content, then HTML comes in very handy. Today's most common type of email is the MIME (Multipurpose Internet Mail Extensions) Multipart email, combining HTML and plain-text.

- MIME messages are handled by Python's email.mime module.
'''

# Below is the code to make Fancy email
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
www.github.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.github.com">GitHub</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )


#### Sending Emails with Attachments
'''
In order to send binary files to an email server that is designed to work with textual data, they 
need to be encoded before transport. This is most commonly done using base64, which encodes binary 
data into printable ASCII characters.
'''
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)


############
# Above is a bit complex, here are multiple libraries designed to make sending emails easier, 
# such as Envelopes, Flanker and Yagmail.

'''
Yagmail is designed to work specifically with Gmail, and it greatly simplifies the process of 
sending emails through a friendly API
'''
import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("my@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)


#####
# If you plan to send a large volume of emails, want to see email statistics, and want to ensure
# reliable delivery, it may be worth looking into transactional email services.