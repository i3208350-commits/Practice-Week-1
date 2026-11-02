# info= {"title":"mr.","age":25,"citi":"haifa"}
#
# def make_griting(name,info,punct="!"):
#     title = info.get("title","")
#     return f"hello {title}{punct} from {name} you are"
# print(make_griting("momo",info= {"title":"mr.","age":25,"citi":"haifa"}))

prices=[20,75,120,45,90]
ex= list(filter(lambda p:p >50,prices))
print(ex)