#BMI Calculator
#remember that the ones that had volleyball games could upload at 12am.

try:
    BMI = input("If you want to know your BMI answer this question: imperial system or metric system? ")

    if BMI.lower() == "imperial system":
        weight = float(input(" Your weight in pounds: "))
        height= float(input("Your height in inches: "))

        height= height * height
        bmi = weight / height
        bmi = bmi * 703

        if bmi <= 18:
            a = "You are almost dying of anorexia :)"

        elif bmi >= 19 and bmi <= 24:
            a = "You are in perfect conditions!"

        elif bmi >= 25 and bmi <= 29:
            a = "You are kinda fat, sorry.."

        elif bmi >= 30 and bmi <= 39:
            a = "You are obese."

        else:
            a = "You are almost dying of obeseness"

        print(f"Your BMI is {bmi} and {a}.")

    elif BMI.lower() == "metric system":
        weight2 = float(input("Your weight in kilograms: "))
        height2 = float(input("Your height in meters: "))

        height2 = height2 * height2
        b = weight2 / height2

        if b <= 18:
            a = "You are almost dying of anorexia :)"

        elif b >= 19 and b <= 24:
            a = "You are in perfect conditions!"

        elif b >= 25 and b <= 29:
            a = "You are kinda fat and overweight, sorry.."

        elif b >= 30 and b <= 39:
            a = "You are obese."

        else:
            a = "You are almost dying of obeseness"

        print(f"Your BMI is {b} and {a}.")

    else:
        print("Invalid option")
    
except ValueError:
    print("Invalid input: ValueError. ")
except ZeroDivisionError:
    print("Invalid input: ZeroDivisionError. ")