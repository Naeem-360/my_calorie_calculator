# 🔥 Daily Calorie Calculator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Nutrition](https://img.shields.io/badge/Health-Nutrition-red.svg)](https://github.com/Naeem-360/my_calorie_calculator)
[![BMR](https://img.shields.io/badge/Feature-BMR%20Calculation-orange.svg)](https://en.wikipedia.org/wiki/Basal_metabolic_rate)

A command-line Python application that calculates your daily calorie needs based on weight, height, age, gender, and activity level using the Basal Metabolic Rate (BMR) formula.

## ✨ Features

- 📊 Calculates BMR using scientifically-backed formulas
- 👫 Gender-specific calculations for more accurate results
- 🏃‍♂️ Activity level adjustments with 5 different intensity options
- 🖥️ Clean and user-friendly command-line interface
- 🧮 Precise calorie calculations with decimal point accuracy

## 📋 Requirements

- Python 3.x

## 🚀 Installation

### Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Naeem-360/my_calorie_calculator.git

# Navigate to the project directory
cd my_calorie_calculator
```

## 💻 Usage

Run the script using Python:

```bash
python calories_calculator.py
```

## 📝 How It Works

The calculator:

1. Asks for your weight (in kg), height (in cm), and age (in years)
2. Requests your gender (male/female)
3. Prompts you to select your activity level from five options
4. Calculates your Basal Metabolic Rate (BMR) using different formulas based on gender:
   - Men: 88.36 + (13.4 × weight) + (4.8 × height) - (5.7 × age)
   - Women: 447.6 + (9.2 × weight) + (3.1 × height) - (4.3 × age)
5. Applies an activity multiplier to determine your total daily calorie needs
6. Displays your recommended daily calorie intake in kcal

## 🏋️‍♀️ Activity Levels Explained

| Level | Description | Multiplier |
|-------|-------------|------------|
| 1 | Sedentary (little or no exercise) | 1.2 |
| 2 | Lightly active (light exercise 1-3 days/week) | 1.375 |
| 3 | Moderately active (moderate exercise 3-5 days/week) | 1.55 |
| 4 | Very active (hard exercise 6-7 days/week) | 1.725 |
| 5 | Super active (intense exercise + physical job) | 1.9 |

## 🔬 The Science Behind It

This calculator uses the Mifflin-St Jeor equation, which is considered one of the most accurate formulas for calculating BMR. The activity multipliers then adjust this base rate to account for different activity levels, providing a more personalized calorie recommendation.

## 💡 Use Cases

- 🥗 Meal planning and dietary management
- 💪 Support for fitness and weight management goals
- 🏥 Nutritional education and health awareness
- 🏋️ Fitness coaching and personal training support

## 📝 Notes

- All measurements must be in metric units (kg for weight, cm for height)
- The calculator performs validation to ensure proper inputs
- Results are rounded to two decimal places for precision

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Naeem-360/my_calorie_calculator/issues).

## 📜 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.
