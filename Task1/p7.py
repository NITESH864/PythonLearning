#WAP for days ,year, weeks

days=int(input("Enter the numer of days:"))

years=days//365
remain_day=days%365
weeks=remain_day//7
Day=remain_day%7

print("Years",years,"Weeks",weeks,"Days",Day)