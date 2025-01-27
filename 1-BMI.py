weight = float ( input ("enter youe weight: "))
height = float ( input("enter your height ")) /100
bmi = weight / height**2
if bmi < 18.5:
    print("your bmi is " , bmi , "and you are undeweight")
if bmi > 18.5 and bmi < 24.9:
    print ("your bmi is " , bmi , " and you are normal weight")
if bmi > 24.9:
    print(" yor bmi is ", bmi , "and you are overweight")


