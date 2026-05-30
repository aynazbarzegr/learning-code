try:    
    birth_year =int(input("enter birth year:!"))
    birth_month = int(input("enter birth month(1-12):"))
    birth_day = int(input("enter birth day(1-31):"))
    today_year = 2025
    today_month = 11
    today_day = 6
    age = today_year - birth_year
    if (today_month,today_day) <(birth_month,birth_day):
        age-=1
        print(f"your age is :{age}")
except:
    print("please enter valid numbers for date!")   


    
    