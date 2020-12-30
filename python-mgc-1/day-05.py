# 두 수 a와 b를 입력받고, a와 b의 사칙연산 계산기를 만들어 보세요.

print("<< Simple Calculator 2.0 >>")

try:
  a=float(input("첫번째 수를 입력하세요 > "))
  b=float(input("두번째 수를 입력하세요 > "))
  op=input("연산자를 입력하세요. (+ : 덧셈, - : 뺄셈, * : 곱셈, / : 나눗셈, // : 몫, % : 나머지) > ")

  if (a+b)%1!=0:
    if op=="+": print(f"{a} + {b} =", a+b)
    elif op=="-": print(f"{a} - {b} =", a-b)
    elif op=="*": print(f"{a} * {b} =", a*b)
    elif op=="/": print(f"{a} / {b} =", a/b)
    elif op=="//": print(f"{a} // {b} =", a//b)
    elif op=="%": print(f"{a} % {b} =", a%b)
    else : print("괄호 안의 연산자만 사용하세요.")
  else:
    if op=="+": print(f"{int(a)} + {int(b)} =", int(a+b))
    elif op=="-": print(f"{int(a)} - {int(b)} =", int(a-b))
    elif op=="*": print(f"{int(a)} * {int(b)} =", int(a*b))
    elif op=="/": print(f"{int(a)} / {int(b)} =", int(a/b))
    elif op=="//": print(f"{int(a)} // {int(b)} =", int(a//b))
    elif op=="%": print(f"{int(a)} % {int(b)} =", int(a%b))
    else : print("괄호 안의 연산자만 사용하세요.")
    
except :
  print("숫자를 입력하세요")

