import smtplib
import datetime as dt
import random


user = "shaheenpython@gmail.com"
password = "asdf@1234"
quote = ""
with open("quotes.txt") as file:
   line = file.readlines()
   quote = random.choice(line)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= user, password = password)
    recipients = ["shaheen.shanavaz94@gmail.com", "anupbdn@gmail.com"]
    connection.sendmail(from_addr=user,
                        to_addrs=", ".join(recipients),
                        msg=f"Subject: Today's Positivity Quotes\n\n {quote} ")
    now = dt.datetime.now()
