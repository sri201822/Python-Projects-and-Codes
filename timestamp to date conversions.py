########## code to take today's date and get previous 7 days and select the rows in the database 
######## converting string to datetime
start_date="2020-04-23"
date_object = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
one_week=date_object-datetime.timedelta(days=7)
print(one_week)
print(type(one_week))
# converting datetime to string
end_date=one_week.strftime("%Y-%m-%d")
print(end_date)
