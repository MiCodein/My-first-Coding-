age = int ( input("patient age: "))
family_history = input("patient FH (0/1): ")
weight = int( input ("patient weight in kg: "))
height = int (input ("patient height in cm: "))/100
bmi = weight/height**2
print(bmi)
score = 0
if age > 45:
    score = score + 2
if family_history == '0':
    pass
if family_history == '1':
    score += 1
if bmi > 30:
    score = score + 3
if score>5: 
    print("score = " , score , ",patients diabetic risk score is high and is at risk of developing diabetes.")
else :
    print ("score = " , score , ",patient has no risk for Developing DM.")
