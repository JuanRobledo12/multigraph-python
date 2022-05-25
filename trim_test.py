


date = '17/05/2022 9:00:58 AM'
split_date = date.split()
print(split_date)
hour = split_date[1][0:4]
print(hour)
day = split_date[0][0:2]
mon = split_date[0][3:5]
yir = split_date[0][6:10]

print(yir + '/' + mon + '/' + day + " " + hour)
date_2 = '2022/05/17  9:03:03'
#print(date_2[0:10])
new_date_2 = date_2[0:10] + date_2[11:16]
print(new_date_2)
print(hour.split(':'))