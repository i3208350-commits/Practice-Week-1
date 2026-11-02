# תרגיל 1

DISCOUNT_ELIGIDILITY_PRISE=500
THE_DISCOUNT_AMOUNT=50

def shopping_calculator(price,number_of_products):
    purchase_amount=price*number_of_products
    if purchase_amount>=DISCOUNT_ELIGIDILITY_PRISE:
        purchase_amount=purchase_amount-THE_DISCOUNT_AMOUNT
        print(f" price to pay {purchase_amount}")
    return purchase_amount


shopping_calculator(120,5)
shopping_calculator(30,2)

# תרגיל 2

# TotalPrice (a variable)  הבעיה היא שכתב באות גדולה למרות משתנה מקומי
# numberofstudents (a variable)  הבעיה היא שכתב באות גדולה למרות משתנה מקומי
# max_grade (a variable)  מצויין
# vat_rate (a constant that never changes)  מצויין
# GetAverage (a function)  הבעיה היא שכתב באות גדולה למרות שפונקציה

# תרגיל 3
#
# def calculate_average(name,grades):
#     total = 0
#     for grade in grades:
#         total = total + grade
#     average = total / len(grades)
#     return average
#
# def is_passing(average,name):
#     if average>= 55:
#        print_average=(name+": average",average,"quot- passed quot;")
#        return print_average
#     else:
#         print_average=(name+": average",average,"quot- failed&quot;")
#         return print_average
#
#
# def print_report(print_average):
#     print(print_average)
#
# name="sdf"
# grades=[12,34,56]
# a=calculate_average(name,grades)
# b=is_passing(a,name)
# print_report(b)


# תרגיל 4- משלוח ומחיר קניה למינמום

# SHIPPING_ELIGIBILITY_PRICE=200
# SHIPPING_PRICE=30
#
# def final_price(total):
#     if total <SHIPPING_ELIGIBILITY_PRICE:
#         total =total+ SHIPPING_PRICE
#
#     return total
#
#
# print(final_price(150))
# print(final_price(250))

