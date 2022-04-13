from flask import request

def convert_to_kg():
    weight_value = float(request.form['Weight value'])
    weight_unit = str(request.form['Unit of weight'])
    if 'pounds' in weight_unit:
        weight_in_kg = round(weight_value/2.205, 1)
    elif 'kg' in weight_unit:
        weight_in_kg = weight_value
    elif 'g' in weight_unit:
        weight_in_kg = round(weight_value/1000, 1)
    return weight_in_kg
    
def convert_to_Metre():
    height_value = float(request.form['height value'])
    height_unit = str(request.form['Unit of height'])
    if 'cm' in height_unit:
        height_in_metres = round(height_value/100, 1)
    elif 'm' in height_unit:
        height_in_metres = height_value
    elif 'inches' in height_unit:
        height_in_metres = round((height_value*2.54)/100,2)
    return height_in_metres

def B_M_I_Status(BMI_value):
    if BMI_value < 18.5:
        BMI_status = f'Your BMI Status is {BMI_value}. You are underweight.'
    elif BMI_value >=18.5<=24.9:
        BMI_status = f'Your BMI Status is {BMI_value}.You are healthy.'
    elif BMI_value >=25.0<=29.9:
        BMI_status = f'Your BMI Status is {BMI_value}.You are overweight.'
    elif BMI_value >=30.0:
        BMI_status = f'Your BMI Status is {BMI_value}.You are obese.'
    return BMI_status



# def calculate_BMI():
#     BMI = round(convert_to_kg()/(convert_to_Metre()**2),2)
#     return BMI

# x = calculate_BMI()
# print(x)


# def BMI_Func():
#     weight_value = float(request.form['name2'])
#     weight_unit = str(request.form['name1'])
#     height_value = float(request.form['name4'])
#     height_unit = str(request.form['name3'])
#     if 'pounds' in weight_unit:
#         weight_in_kg = round(weight_value/2.205, 1)
#     elif 'kg' in weight_unit:
#         weight_in_kg = weight_value
#     elif 'g' in weight_unit:
#         weight_in_kg = round(weight_value/1000, 1)
    
#     if 'cm' in height_unit:
#         height_in_metres = round(height_value/100, 1)
#     elif 'm' in height_unit:
#         height_in_metres = height_value
#     elif 'inches' in height_unit:
#         height_in_metres = round((height_value*2.54)/100,2)
#         # height_in_metres = round(height_in_cm/100, 2) 

#     B_M_I = round(weight_in_kg/(height_in_metres**2),2)
#     return render_template('home.html', weight_value = weight_value, weight_unit = weight_unit, height_value = height_value, height_unit = height_unit, B_M_I = B_M_I)
