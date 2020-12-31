while True:
  try:
    print("<< Simple Calculator 3.0 >>")
    print("put n to exit")
    print("---------------------------")

    a=input("put a number > ")
    if a=="n": break
    if "." in a: float(a)
    else: int(a)

    b=input("put another one > ")
    if b=="n": break
    if "." in b: float(b)
    else: int(b)

    op=input("put an operator > ")
    if op=="n":
      break
    valid_op=["+","-","*","/","//","%"]

    if op in valid_op:
      print(round(eval(a+op+b),4))
    else:
      print("not a valid operator")
    
  except :
    print("not a number")
