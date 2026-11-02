


def parse_percentage(text):
    try:
       if not text.endswith("%"):
          raise ValueError("must end with %")
       number = int(text[:-1])

       if number<0 or number>100:
           raise ValueError("Wrong number 0 - 100")
       return number

    except ValueError as a:
        print(a)
        return "Enter information again"

Import logging
logging.basicConfig(
      level=logging.DEBUG,
      format="%(asctime)s %(levelname)s %(message)s",
     filename=""
     filemode=""
logging.debug("")

    print(parse_percentage("8")) # 75
