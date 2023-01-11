import datetime
import random
import smtplib

import pandas

today = datetime.datetime.now()

today_tuple = (today.month,today.day)
print(today_tuple)

data = pandas.read_csv("birthdays.csv")
print(0)
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows() }
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person["name"])
    file_pasth = f"letter_{random.randint(1,3)}.txt"
    with open(file_pasth) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(1)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("nta1998@gmail.com","aypxirbzkmkbgltd")
        connection.sendmail(from_addr="nta1998@gmail.com",to_addrs= birthday_person["email"],msg=f"{contents}")
        print(2)
