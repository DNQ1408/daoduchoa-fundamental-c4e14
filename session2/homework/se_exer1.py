wei = float(input("Hi, plz tell me your weight in kg?"))
hei = float(input("Ok. So what is your height in cm?")) / 100
bmi = wei / (hei * hei)

print("Here is your BMI", int(bmi))
if bmi < 16:
    print("You're severely underweight")
elif bmi < 18.5:
    print("You're underweight")
elif bmi <25:
    print("You're normal")
elif bmi < 30:
    print("You're overweight")
else:
    print("You're obese")
