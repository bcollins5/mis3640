import datetime

from datetime import date
import calendar


now = datetime.datetime.now()


# '''Gives you today's date, and the current time'''

# print('Month', now.month)
# print('Day', now.day)
# print('Year', now.year)



# print('Hour', now.hour)
# print('Minute', now.minute)
# print('Second', now.second)


# def check_weekday():

#     weekday = datetime.datetime.today().weekday()
   


#    if weekday is:
#        == 1
#        return "Tue"
#        == 2
#        return "wed"
#        == 3
#        return "Thurs"
#        == 4
#        return "Fri"
#        == 5
#        return "Sat"
#        == 6
#        return "Sun"
#        == 7 
#        return "Mon"

# print(check_weekday())

# check_weekday()

# # def test():

# #     if weekday == 3:
#         return "Thursday"

# print(test)



'''Gives you today's weekday and date'''



Month = now.month
Day = now.day
Year = now.year



my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]

print(weekday,',', Month,'-', Day,'-', Year)






def birthday():

    print("Please enter your birthday")
    bd_y = input("Year: ")
    bd_m = input("Month (1-12): " )
    bd_d = input("Day: ")

    now = date.today()
    birthdate = date(int(bd_y), int(bd_m), int(bd_d))


    print(birthdate)

    age = now - birthdate

    print ("Your age is %s" % age)

birthday()


def next_birthday():

    # print("Please enter your birthday")
    # bd_y = input("Year: ")
    # bd_m = input("Month (1-12): " )
    # bd_d = input("Day: ")

    print("Enter your next birthday (Year, Month, Day)")

    nx_y = input("Year: ")
    nx_m = input("Month (1-12): ")
    nx_d = input("Day: ")
    

    now = date.today()
    birthdate = date(int(bd_y), int(bd_m), int(bd_d))
    next_bday = (int(nx_y), int(nx_m), int(nx_d))

    diff = next_bday - now
    print('Time til next birthday', diff)

next_birthday()


#above i tried finding the difference between next birthday and now
#as for hours, seconds and minutes..




# I'm not sure what you are asking for here: 
# there is a day when one is twice as old as the other. 
# That’s their Double Day

