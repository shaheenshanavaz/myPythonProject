import smtplib

my_email = "shaheenpython@gmail.com"
password = "asdf@1234"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="shaheen.shanavaz94@gmail.com",
                        msg="Subject:Hello\n\n This is my mgs")