import smtplib
import datetime
import random

now = datetime.datetime.now()
current_week_day = now.weekday()

if current_week_day == 2:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    my_email = "amanrazaonline@gmail.com"
    password = "xkqinhmukxhegwkr"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="amanraza1010@gmail.com",
                            msg=f"Subject:Quote of the day\n\n{quote}"
                            )



