
#정수형, 실수형, 불 자료형, 문자열 변수를 선언하고 type을 출력해보세요.

an_int=4
a_float=.27
a_boolean=True
a_string="This is a string"

print(type(an_int))
print(type(a_float))
print(type(a_boolean))
print(type(a_string))

#"저는 모각코의 000입니다" 라는 문자열 변수를 만들고 문자열 슬라이싱으로 "000"만 출력해보세요. ( 000은 본인의 별명입니다.) 

nickname="inini"
str=f"저는 모각코의 {nickname}입니다"
index=str.find(nickname)
length=len(nickname)

print(str[index:index+length])

