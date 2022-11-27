# class compute_bmi:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#
# new_bmi = compute_bmi(136, 65)


def calculate_body_mass_index(weight, height):
    kilograms_per_pound = 0.45359237
    meters_per_inch = 0.0254

    weight_in_kilograms = weight * kilograms_per_pound
    height_in_meters = height * meters_per_inch
    bmi = weight_in_kilograms / (height_in_meters * height_in_meters)

    print("BMI is", format(bmi, ".2f"))
    if bmi < 18.5:
        print("underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("overweight")
    else:
        print("obese")


if __name__ == '__main__':
    user_weight = eval(input("Enter weight in pounds: "))
    user_height = eval(input("Enter height in inches"))
    calculate_body_mass_index(user_weight, user_height)