'''Write a python program to compute gross salary based on following parameters:-

Basic Salary           HRA              DA
1-4000                 10%              50%
4001-8000               15%              60%
8001-12000              20%              70%
More than 12000         25%              80%

gs=bs+hra+da
'''

salery=int(input("Enter the salery:"))

if salery<=4000:
    hra=(salery*10)/100
    da=(salery*50)/100
    gs=salery+hra+da
    print("Gross salery is:",gs)
elif salery>4000 and salery<=8000:
    hra=(salery*15)/100
    da=(salery*60)/100
    gs=salery+hra+da
    print("Gross salery is:",gs)
elif salery>8000 and salery<=12000:
    hra=(salery*20)/100
    da=(salery*70)/100
    gs=salery+hra+da
    print("Gross salery is:",gs)
else:
    hra=(salery*25)/100
    da=(salery*80)/100
    gs=salery+hra+da
    print("Gross salery is:",gs)
        