"""
BMI Calculator - calculates Body Mass Index based on weight and height
"""

def bmi_calculator():
    
    user_weight = input('Enter your weight in kilograms(kg): ')
    user_height = input('Enter your height in meters: ')

    try:
        user_weight_float = float(user_weight)
        user_height_float = float(user_height)
    except ValueError:
        print('Please enter valid numbers for your weight and height.')

    BMI = (user_weight_float/(user_height_float*user_height_float))
    print(f'\nYour BMI is: {BMI:.1f}')

    if BMI < 18.5:
        print('You are underweight. Consider changing your health habits')
    elif 18.5 <= BMI <= 24.9:
        print('Your weight is in the normal range. Keep the good work!')
    elif 25.0 <= BMI <= 29.9:
        print('You are overweight. Consider changing your health habits.')
    elif 30.0 <= BMI <= 39.9:
        print('Your BMI indicates obesity. Consider seeing a doctor.')
    else:
        print('Your BMI indicates severe obesity. Consider seeing a doctor.')


if __name__ == '__main__':
    bmi_calculator()