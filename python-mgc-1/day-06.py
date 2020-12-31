# 1) 세 개의 숫자를 입력 받은 후에, 그 세 개의 숫자 중에서 가장 큰 수를 출력하는 프로그램을 작성하세요.

print("<<큰수 찾기>>")
print("숫자를 3개 입력하세요. 구분자는 , 를 사용하세요. (ex. 2 5 ,   33.3,  1  2  3)")

def get_max():
  num=input("> ").split(",")
  result=[]

  if len(num)>3:
    print("3개 초과 입력하였습니다.")
    get_max()
  elif len(num)<3:
    print("3개 미만 입력하였습니다.")
    get_max()
  else:
    for i in num:
      if "." in i:
        result.append(float(i.replace(" ","")))
      else: 
        result.append(int(i.replace(" ","")))

    print(f"입력하신 수 {result} 중 가장 큰 수는 {max(result)}입니다.\n")

get_max()


# 2) 한 문자열을 입력 받은 후에, 그 문자열 안에 "모각코"라는 단어가 들어있으면 "모각코! 좋아요!"를 없으면 "모각코! 없어요ㅠ" 를 출력해주세요

print("<<\"모각코\" 찾기>>")
print("문자열을 입력하세요. (ex. \"  모   각코  가 있나요?\" 또는 \"무각코!는 없는 것 같네요\")")
str=input("> ")

print(f"입력하신 \"{str}\"에 \"모각코\"가 포함되어 있습니까?")
if "모각코" in str.replace(" ",""):
  print("네 있습니다!")
else:
  print("아니요 없습니다.")

# 정규식 이용

import re

print("<<\"모각코\" 찾기>>")
print("문자열을 입력하세요. (ex. 모   !!각코?가 있나요??? 또는 무각~~~코!없다...)")
str=input("> ")
parse = re.sub('[ ,.~!?]', '', str)

print(f"입력하신 \"{str}\"에 \"모각코\"가 포함되어 있나요?")

if "모각코" in parse:
  print("네 있습니다!")
else:
  print("아니요 없어요..ㅜㅜ")

