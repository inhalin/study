# 자바 라이브 스터디 3주차

#### 목표

```
자바가 제공하는 다양한 연산자를 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `🔘 not done`

- 🟢 산술 연산자
- 🟡 비트 연산자
- 🟡 관계 연산자
- 🟢 논리 연산자
- 🟡 instanceof
- 🟢 assignment(=) operator
- 🟡 화살표(->) 연산자
- 🟡 3항 연산자
- 🟢 연산자 우선 순위
- 🔘 (optional) Java 13. switch 연산자

---

## 연산자란?

연산자는 1, 2, 3항의 피연잔자에 대해 **특정한 연산을 수행하고 결과를 생성하는 기호**이다. 연산자의 종류와 피연산자는 그 피연산자에 수행되는 연산의 종류와 생성되는 결과의 종류를 결정한다.

#### 자바 연산자의 유형

자바의 연산자는 두 기준으로 분류할 수 있다:

- **피연산자의 수** - 피연산자의 수에 따라 단, 2항, 3항 연산자 세가지 종류로 나눌 수 있다. 만약 연산자가 하나의 피연산자만을 취한다면 단항 연산자(unary operator), 두 개를 취하면 2항 연산자(binary operator),세 개를 취하면 3항 연산자(ternary operator)라고 부른다.
- **수행하는 연산의 종류** 피연산자에 대해 수행하는 연산의 종류에 따라 산술 연산자(arithmatic operator), 관계 연산자(relational operator), 논리 연산자(logical operator), 비트 연산자(bitwise operator)라고 부른다.

---

## 산술 연산자

- +(덧셈), -(뺄셈), \*(곱셈), /(나눗셈) 과 같은 연산자를 산술 연산자라고 한다.

- 숫자형 피연산자와만 사용할 수 있다. 즉, 산술 연산자에 대한 피연산자는 반드시 `byte`, `short`, `char`, `int`, `long`, `float`, `double` 중 하나여야 한다.

- 산술 연산자는 boolean형이나 참조형 피연산자를 가질 수 없다.

- 단항 연산자

```java
public class Ex02{
    public static void main(String[] args){
        byte sum=1+2;
        int sub=10-5;
        long multi=100*200;
        float division=6.5f/2;
        double remain=7.5%2;

        System.out.println("sum="+sum);
        System.out.println("sub="+sub);
        System.out.println("multi="+multi);
        System.out.println("division="+division);
        System.out.println("remain="+remain);
    }
}
```

> 결과

```java
sum=3
sub=5
multi=20000
division=3.25
remain=1.5
```

---

## 비트 연산자

비트연산자는 피연산자 **각각의 비트를 조작**한다. 자바는 여러가지 비트연산자를 정의하고, 이 연산자들은 정수유형인 long, int short, char, byte의 에 적용된다.

연산자 | 설명
---|--------------------------------------------------
`&`| **이진 AND 연산자**(비트곱 연산자)는 양쪽의 값이 1일 때만 연산결과를 1로 반환
`ㅣ`| **이진 OR 연산자**(비트합 연산자)는 둘 중 하나의 값만 1이어도 연산결과를 1로 반환
`^`| **이진 XOR 연산자**는 양쪽 값이 다를 경우에만 연산결과를 1로 반환
`~`| **이진 NOT 연산자**는 피연산자 값의 반대값을 반환
`<<`| **이진 Left Shift 연산자**는 왼쪽 피연산자값을 연산자 오른쪽에서 지정한 수만큼 왼쪽으로 이동, 비어있는 비트를 0으로 채운다.
`>>`| **이진 Right Shift 연산자**는 왼쪽 피연산자 값을 연산자 오른쪽에서 지정한 수만큼 오른쪽으로 이동, 부호비트를 이용해서 비어있는 비트를 채운다. 예를 들어, 피연산자의 수가 양수이면 0으로, 음수이면 1로 채운다.
`>>>`| **Shift right zero fill 연산자**는 `>>` 연산자와 같이 오른쪽으로 이동시키고, 비어있는 곳을 0으로 채운다.

---
 
## 관계 연산자

- 모든 관계 연산자는 이진 연산자이고 두개의 피연산자를 갖는다.
- 관계 연산자의 결과값은 항상 boolean 값 `true` 또는 `false`이다.
- 대부분 if문이나 while문에서 사용된다.

연산자 | 설명
---|--------------------------------------------------
`==`| 피연산자의 값을 비교해서 둘이 같으면  `true`를 반환
`!=`| 피연산자의 값을 비교해서 둘이 다르면 `true`를 반환
`>`| 왼쪽 값이 오른쪽 값보다 크면 `true`를 반환
`<`| 왼쪽 값이 오른쪽 값보다 작으면면 `true`를 반환
`>=`| 왼쪽 값이 오른쪽 값보다 크거나 같으면 `true`를 반환
`<=`| 왼쪽 값이 오른쪽 값보다 작거나 같으면 `true`를 반환

---

## 논리 연산자

연산자 | 설명
--|------------------------------------
`!`| 피연산자 값이 false이면 `true`를 반환
`&&`| 피연산자 값이 둘다 true 이면 `true`를 반환, 왼쪽 값이 false이면 오른쪽은 계산하지 않고 넘어간다. `ex01`
`&`| 피연산자 값이 둘다 true 이면 `true`를 반환
`││`| 피연산자 둘중 하나가 true 이면 `true`를 반환, 왼쪽 값이 true이면 오른쪽은 계산하지 않고 넘어간다. `ex01`
`ㅣ`| 피연산자 둘중 하나가 true 이면 `true`를 반환
`^`| 피연산자 둘의 값이 다를때만 `true`를 반환
`&=`| 피연산자 둘을 비트곱 한 값이 true 이면 `true`를 반환
`ㅣ=`| 피연잔자 둘을 비트합 한 값이 true 이면 `true`를 반환


#### `&&` vs `&`, `||` vs `|`

```java
public class Ex01 {
	public static void main(String[] args) {
		int a=10;
		int b=5;
		if(a>3&&++b>5) {
			System.out.println("short-circuit AND operator '&&' 사용시 : b="+b);
		}
		if(a>3&&++b>5) {
			System.out.println("logical AND operator '&' 사용시 : b="+b);
		}
	}
}
```

> 결과

```java
short-circuit AND operator '&&' 사용시 : b=6
logical AND operator '&' 사용시 : b=7
```

---

## instanceof

자바의 **instanceof**는 유형비교 연산자라고도 하며, 오브젝트가 특정 유형의 인스턴스(클래스, 서브클래스 또는 인터페이스)인지 테스트한다. 주로 고건문에 사용하며, instanceof의 왼쪽에 참조변수, 오른쪽에 타입(클래스명)이 피연산자로 위치한다.

- 변수가 특정 클래스, 즉 구현된 인터페이스나 상위클래스나 상위 인터페이스의 인스턴스이면 `true`를 반환하고 이는 참조변수가 검사한 타입으로 형변환이 가능하다는 뜻이다.
- 변수가 특정 클래스의 인스턴스가 아니거나 변수가 null이면 `false`를 반환

---

## assignment(=) operator

대입연산자 `=`은 오른쪽 피연산자의 값을 왼쪽 피연산자에 저장한다. 결합규칙은 오른쪽에서 왼쪽의 순서로 수행되고, 연산자들 중에 가장 낮은 우선순위를 가지고 있기 때문에 연산에서 제일 나중에 수행된다.

```java
public class Ex01 {
	public static void main(String[] args) {
		int a, b;
		a=2;
		System.out.println("첫번째 a="+a);
		a=b=3;
		System.out.println("두번째 a="+a);
	}
}
```

> 결과

```java
첫번째 a=2
두번째 a=3
```

대입연산자의 왼쪽 피연산자를 lvalue(left value), 오른쪽 피연산자를 rvalue(right value)라고 한다. rvalue는 변수, 식, 상수 등 모두 가질 수 있지만 lvalue는 변수와 같이 값을 변경할 수 있어야 한다. 따라서 리터럴이나 상수같이 값을 저장할 수 없는 것은 lvalue가 될 수 없다.

```java
public class Ex02 {
	public static void main(String[] args) {
		int a=0;
		5=a;
	}
}
```

> 결과

```java
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The left-hand side of an assignment must be a variable
```

```java
public class Ex03 {
	final double pi=3.14;   // 변수 앞에 final을 붙이면 상수가 된다.
	pi=10.0;
}
```

> 결과

```java
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The left-hand side of an assignment must be a variable
```

---

## 화살표(->) 연산자

<!-- 아직 잘 모르겠음.. -->

자바에서 사용하는 람다 표현식으로 왼쪽에 매개변수목록, 오른쪽에 함수를 갖는다. 

```
(매개변수1, 매개변수2, ...) -> {함수}
```

- 매개변수의 타입을 추론할 수 있는 경우 타입을 생략할 수 있다.
- 매개변수가 하나인 경우에는 괄호를 생략할 수 있다.

---

## 3항 연산자

3항 연산자 `?:`는 세 개의 피연산자를 필요로 하고 종류는 조건 연산자 하나뿐이다. `조건식 ? 식1 : 식2`의 모양을 가지고 있고, 조건식이 true이면 식1을, false이면 식2를 결과값으로 갖는다.

```java
public class Ex01 {
	public static void main(String[] args) {
		int result;
		int a=5, b=3;		
		result=a>b?a:b;
		System.out.println(result);
	}
}
```

> 결과

```java
5
```

---

## 연산자 우선 순위

연산자가 둘 이상인 경우 연산자의 우선순위에 의해서 연산순서가 결정된다. 우선순위가 높은것부터 낮은것 순으로 정리하면 아래의 표와 같다.

종류 | 결합규칙 | 연산자
---|---|---
단항연산자 | **<--** | `++` `--` `+` `-` `~` `!`
산술연산자 | --> | `*` `/` `%`
--- | --> | `+` `-`
--- | --> | `<<` `>>`
비교연산자 | --> | `<` `>` `<=` `>=` `instanceof`
--- | --> | `==` `!=`
논리연산자 | --> | `&`
--- | --> | `^`
--- | --> | `ㅣ`
--- | --> | `&&`
--- | --> | `││`
--- | --> | `?:`
대입연산자 | **<--** | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `!=`

---

## 참고자료

남궁성. _Java의 정석 3판._ 도우출판, 2016.

https://howtodoinjava.com/java/basics/data-types-in-java/

https://www.oreilly.com/library/view/java-8-pocket/9781491901083/

https://www.tutorialspoint.com/Bitwise-right-shift-operator-in-Java

http://www.tcpschool.com/java/java_lambda_concept

