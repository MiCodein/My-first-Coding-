age = int(input("patient age: "))
heart_rate = int (input(" patient HR : "))
systolic_Blood_pressure = int(input("patient SBP: "))
diastolic_blood_pressure = int (input(" patient DBP: "))
if age > 60 and heart_rate > 100:
    print("you are over 60 years old and your HR is over 100, it's dangerous situations")
if systolic_Blood_pressure >140 or diastolic_blood_pressure > 90:
    print(" your BP is in dengerous situation")
elif age<60 or heart_rate<100 and systolic_Blood_pressure<140 and diastolic_blood_pressure<90:
    print (" you are healthy")
else: print("you should have assessment")

