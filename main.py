import weakref
from idlelib import window

# from http.cookiejar import DAYS

# THE_OVERALL_SCORE=60
#
# def is_past(score:int):
#     if score >=THE_OVERALL_SCORE:
#         print("is_past")
#     else:
#         print("is_not_past")
# is_past(85)
# is_past(40)

# THE_WEATHER=30
# DAYS=3
import logging
logging.basicConfig(
      level=logging.DEBUG,
      format="%(asctime)s %(levelname)s %(message)s",
      filename="e.log",
      filemode="a")
logging.debug("vcxv")



#
# def Collect_findings():
#     weather_weighting=[]
#
#     for nam in range(DAYS):
#
#         nam= float(input("temp day :  "))
#         weather_weighting.append(nam)
#     return weather_weighting
#
# def windor(weather_weighting):
#     weather_weighting = sum(weather_weighting)
#     average_weather=weather_weighting/DAYS
#     if average_weather>THE_WEATHER:
#         print("avg",average_weather,"hot")
#
# weather_list = Collect_findings()
#
# windor(weather_list)


info= {"title":"mr.","age":25,"citi":"haifa"}

def make_griting(name,info,punct="!"):
    title = info.get("title","")
    return f"hello {title}{punct} from {name} you are"
print(make_griting("momo",info= {"title":"mr.","age":25,"citi":"haifa"}))