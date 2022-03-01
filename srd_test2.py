import json

# lst1 = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

lst2 =input("Please enter the json:")
print(lst2)
lst1 = json.loads(lst2)
print(lst1)
for i in lst1:
    height_cm = i["HeightCm"]
    mass = i["WeightKg"]
    height_m = height_cm/100
    count = 0
    BMI = mass / (height_m * height_m)

    if BMI<=18.4:
        i["BMI"]=BMI
        i["BMI Category"]="Underweight"
        i["Health risk"]="Below malnutrition risk"
    elif BMI>=18.5 and BMI< 24.9:
        i["BMI"] = BMI
        i["BMI Category"]="Normal weight"
        i["Health risk"]="Low risk"
    elif BMI>=25 and BMI<29.9:
        i["BMI"] = BMI
        count += 1
        i["BMI Category"]="Overweight"
        i["Health risk"]="Enhanced risk"
    elif BMI>=30 and BMI<=34.9:
        i["BMI"] = BMI
        i["BMI Category"]="Moderately obese"
        i["Health risk"]="Medium risk"
    elif BMI>=35 and BMI<=39.9:
        i["BMI"] = BMI
        i["BMI Category"]="Severely obese"
        i["Health risk"]="High risk"
    elif BMI>=40:
        i["BMI"] = BMI
        i["BMI Category"]="Very severely obese"
        i["Health risk"]="Very high risk"

print(lst1)