import datetime

# now=datetime.datetime.now()
# print(now) #print present date and time

# print(datetime.date.today()) #print today's date

# print(now.strftime("%d:%m:%y")) #print date in a specific dd-mm-yyyy format

# sample_date=datetime.datetime(2024,1,1) #passing date
# print(sample_date)

order_date=datetime.datetime(2024,1,1)
delivery_date=datetime.datetime(2024,1,11)
dif=delivery_date-order_date #date difference
print(dif)