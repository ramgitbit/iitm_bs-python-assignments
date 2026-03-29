age =int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[0:2]),int(dob[3:5]),int(dob[6:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day)+"/"+str(month)+"/"+str(year+age)  # str: last birthday formatted as day/month/year  #Birth year + number of birthdays = us birthday ka year

month += 10
month, year = (month-1)%12+1, year+(month-1)//12
tenth_month = f"{day}/{month}/{year}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month, fifth_birthday ,last_birthday, sep=', ')

weight = float(input()) # float: Read a number as float from stdin(Standard input)
kg = int(weight)
grams= int((weight-kg)*1000)

weight_readable = f"{kg} kg {grams} grams"# str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)