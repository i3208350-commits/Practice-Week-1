# product=["Pen","Notebook","Bag"]
# price=[5,12,60]
# amount=[4,2,1]
#
# # def namcer(pruse,amount)
# #     return pruse*amount
# def Grocery_checkout(product,price,amount):
#     total=0
#     for i in range(len(price)):
#         ama=price[i]*product[i]
#         print()
#
#
#
# a=Grocery_checkout(product,price,amount)
# print_Grocery_checkout(a)

# def calculate_bmi(weight, height):
#     bambur=("BMI:", round(weight / (height * height), 1))
#     return bambur
# def print_bmi(o):
#     print(o)
#
#
# o=calculate_bmi(70,1.75)
# print_bmi(o)


# COLD=15
# PLEASANT=28
#
#
#
# def classify(temperature):
#     for i in temperature:
#         if i< COLD:
#             print(i, "cold")
#
#         elif i>COLD and i<PLEASANT:
#             print(i, "pleasant")
#         else:
#             print(i, "hot")
#
#
#
# temperature = [12, 24, 33]
# classify(temperature)

# def safe_divide(a_text, b_text):
#     try:
#         a_text=int(a_text)
#         b_text=int(b_text)
#         return a_text+b_text
#     except ValueError:
#         return "numbers only"
#     except ZeroDivisionError:
#         return "cannot divide by zero"
#
#
# print(safe_divide("10", "4"))
# print(safe_divide("10", "0"))
# print(safe_divide("ten", "2"))



def min_max():
    lowest=(min(numbers))
    highest=(max(numbers))
    print(lowest, highest)
numbers=[40, 3, 99, 17]
min_max()


# def nambur(visits):
#     views=0
#     dicti = {}
#     for i in visits:
#         print(i)
#         if i in dicti:
#             dicti[i]+=1
#         else:
#             dicti[i]=1
#
#         views+=1
#         o="tom" in visits
#     print( views,o,dicti)
#
# visits = ["dana", "avi", "dana", "noa", "avi", "dana"]
# nambur(visits)
# def sell(prices, position):
#     try:
#
#         a = (prices[position])
#
#         open_register()
#     except IndexError:
#         open_register()
#         a = None
#
#     finally:
#         close_register()
#         print(a)




# def open_register():
#     print("register opened")
#
#
# def close_register():
#     print("register closed")
#
#
# sell([10, 20, 30], 1)
# sell([10, 20, 30], 7)

info= {"title":"mr.","age":25,"citi":"haifa"}

def make_griting(name,info,punct="!"):
    title = info.get("title","")
    return f"hello {title}{punct} from {name} you are"
print(make_griting("momo",info= {"title":"mr.","age":25,"citi":"haifa"}))