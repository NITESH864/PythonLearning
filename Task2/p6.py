''' Write a python program to calculate electricity bill based on following parameters:-
 
Units                                          Bill/unit

1-150                                          2.40
For next 151-300                               3.00
For next more than
300                                            3.20

'''
unit=int(input("Enter the unit of electricity bill : "))

if(unit<=150):
	print(unit*2.40,"Rs.")

elif(unit>150 and unit<=300):
	bill = (150 * 2.40) + (unit - 150) * 3.00
	print(bill,"Rs.")
else:
	bill=(150*2.40)+(150*3.00)+(unit-300)*3.20
	print(bill,"Rs.")