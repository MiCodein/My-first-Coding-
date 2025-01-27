blood_sugar = 100
daily_time = 0 
meal_time = 4
while daily_time < 24:
    daily_time = daily_time + 1
    r = daily_time % 4
    if r != 0:
        blood_sugar = blood_sugar - 10
    else: 
        blood_sugar = blood_sugar + 30
        
    print("daily time: ",daily_time , " ", " blood sugar: ", blood_sugar)        


