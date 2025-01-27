patient_weight = int(input("patient weight/kg : "))
fluid_need = 0
if patient_weight < 10: 
    fluid_need = patient_weight * 100
    
if patient_weight <= 20 and patient_weight >= 10:
    fluid_need = (patient_weight-10)*50 + 1000
   
if patient_weight > 20:
    fluid_need = (patient_weight-20)*20 + 1500
print(" the amount of fluid that patient need in 24h is " , fluid_need , " ml")
    
