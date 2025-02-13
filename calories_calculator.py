
def calo_calc():
    print("-" * 60)
    weight = float(input("Enter your weight (kg): "))
    height = float(input("-" * 60 + "\nEnter your height (cm): "))
    age = float(input("-" * 60 + "\nEnter your age (years): "))

    BMR_for_men = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    BMR_for_women = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    while True:
        ask_gender = input("-" * 60 + "\nEnter your gender (male/female): ").lower().strip()
        if ask_gender in ["male", "female"]:
         break
        print("Invalid input! Please enter 'male' or 'female'.")


    print("-" * 60 + "\nChoose you activity level: ")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise 1-3 days/week)")
    print("3. Moderately active (moderate exercise 3-5 days/week)")
    print("4. Very active (hard exercise 6-7 days/week)")
    print("5. Super active (intense exercise + physical job)")

        
    activity_multipliers = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
        }
    
    while True:
        try:
          activity_level = int(input("Enter your activity level (1-5): "))
          if activity_level not in [1, 2, 3, 4, 5,]:
           print("Invalid input! Please choose between (1-5)")
           continue
          break
        except ValueError:
           print("Please entre valid number")



    if ask_gender.lower().strip() != "male":
           daily_cal = BMR_for_women * activity_multipliers[activity_level]
    else:
           daily_cal = BMR_for_men * activity_multipliers[activity_level]
    print("-" * 60)
    return f"Your daily calorie needs: {daily_cal:.2f} kcal 🔥\n"
           
        
print(calo_calc())


