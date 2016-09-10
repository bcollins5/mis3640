#In Class 1
#Exercise 2
#Question 1

print('Question 1')

seconds=(42*60 + 42)
print(seconds, '\n')

print('Question 2')

miles=(10/1.61)
print(miles, '\n')


print('Question_3')

seconds_per_mile=(seconds/miles)



minutes_per_mile=(seconds_per_mile/60)

print('Minutes per Mile')
testing_mang=(minutes_per_mile-int(minutes_per_mile))

real_test_test=(round((testing_mang*60),2))



print(int(minutes_per_mile),'min', real_test_test , 'sec' ,'/mile', '\n')



hours_per_mile=(minutes_per_mile/60)



mph=(1/hours_per_mile)

print('Avg Speed in MPH')
print(mph)






#In Class 2
#Exercise 1

print('\n')

print('Question 1')


volume_of_sphere=((4/3)*3.1415926*(5**3))
rounded_volume_of_sphere=round(volume_of_sphere,2)
print('Volume of sphere =', rounded_volume_of_sphere)



print('\n')

print('Question 2')

cover_price = 24.95
discount_price = (cover_price)-(cover_price*.4)
shipping_cost = 3
extra_shipping_cost = .75

cost=((60*discount_price) + shipping_cost + (59*extra_shipping_cost))
rounded_cost=round(cost, 2)
print('cost', rounded_cost)

print('\n')

print('Question 3')



print('Departure Time: 6:52am')
print('Time Zero: 12:00am')
print('"Number of Seconds From Time Zero to Departure Time" = Number of Seconds from 12:00am to 6:52am')
print('Number of Seconds From Time Zero to Departure Time = 6*60*60 + 52*60')
Number_of_Seconds_From_Time_Zero_to_Departure_Time=((6*60*60)+(52*60))
print('Total Length of Run in Seconds = Length of Phase 1 in Seconds + Length of Phase 2 in Seconds + Length of Phase 3 in Seconds')
print('Example Calculation: Length of Phase 2 in Seconds = number of miles * pace per mile in seconds = (3 miles) * ((7 minutes * 60 seconds) + 12 seconds)')
Length_of_Phase_1_in_Seconds = (1)*((8*60)+15)
print('Length of Phase 1 in Seconds = ', Length_of_Phase_1_in_Seconds)
Length_of_Phase_2_in_Seconds = (3)*((7*60)+12)
print('Length of Phase 2 in Seconds = ', Length_of_Phase_2_in_Seconds)
Length_of_Phase_3_in_Seconds = (1)*((8*60)+15)
print('Length of Phase 3 in Seconds = ', Length_of_Phase_3_in_Seconds)
Total_Length_of_Run_in_Seconds = Length_of_Phase_1_in_Seconds + Length_of_Phase_2_in_Seconds + Length_of_Phase_3_in_Seconds
print('Total Length of Run in Seconds = ', Total_Length_of_Run_in_Seconds)
Number_of_Seconds_From_Time_Zero_to_Return_Time_From_Run = Number_of_Seconds_From_Time_Zero_to_Departure_Time + Total_Length_of_Run_in_Seconds
print('Number of Seconds From Time Zero to Return Time From Run = ', Number_of_Seconds_From_Time_Zero_to_Departure_Time + Total_Length_of_Run_in_Seconds)
Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run = Number_of_Seconds_From_Time_Zero_to_Return_Time_From_Run/60
print('Number of Minutes From Time Zero to Return Time From Run = ', Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run)
Number_of_Hours_From_Time_Zero_to_Return_Time_From_Run = Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run/60
print('Number of Hours From Time Zero to Return Time From Run = ', Number_of_Hours_From_Time_Zero_to_Return_Time_From_Run)
Number_of_Minutes_in_Remainder_of_Hours_Calculation = Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run % 60
print('Number of Minutes in Remainder of Hours Calculation = ', Number_of_Minutes_in_Remainder_of_Hours_Calculation)
print('Final Answer for Question 3: The time at which the runner returns to his or her house for breakfast is 7 hours and 30 minutes from time zero, or 12:00 am. Thus, the runner\'s return time is 7:30 am.')


print('\n')



print('Question 4')

grade_1 = 82
grade_2 = 89

grade_change = ((grade_2-grade_1)/grade_1)
percent_increase = (grade_change*100)
rounded_percent_increase=round(percent_increase,2)
print(rounded_percent_increase,'%')

print('Hey professor I need help creating it in XX.X% I know it has something to do with %05.2f but I keep running into errors.')

input()








print('Pi equals %06.2f.' % 3.1415926)

hours = int(13/5)
min = 13%5

print(hours, min)


import math
print(math.pi)


import time
print (time.time())

time = (time.time())

hours = (time/60)

print('hour')
print(hours)
