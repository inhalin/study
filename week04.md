# [자바 라이브 스터디] 4주차 - 제어문

#### 목표

```
자바가 제공하는 제어문을 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- 🟢 선택문
- 🟢 반복문

#### 과제 (Optional)

- ⚪ JUnit5 테스트
- ⚪ live-study 대시보드 코드
- ⚪ LinkedList
- ⚪ Stack
- ⚪ 앞서 만든 ListNode를 사용한 Stack
- ⚪ Queue

---

## 자바의 제어문

자바의 제어문에는 `조건문`과 `반복문`이 있다. `조건문`은 조건에 따라 명령을 실행하고, `반복문`은 특정 명령을 반복 실행한다. 조건식의 결과값은 반드시 `true` 또는 `false`여야 하고, `true`일 경우에 명령을 실행하고 `false`일 경우에는 건너뛴다.

---

## 선택문(조건문)

조건문은 조건식과 문장을 포함하는 블럭 `{}`으로 구성되어 있으며, 조건식의 연산결과에 따라 실행할 문장이 달라진다. 조건문에는 if문과 switch문이 있고 처리해야 하는 경우의 수가 많을 경우 switch문이 효율적이지만, if문보다 제약이 많다.

### 1.1 if문

가장 기본적인 조건문으로 `조건식`이 참일 때만 `괄호 {}` 안의 명령을 실행한다. 형태는 다음과 같다 :

```java
if (조건식){
  //조건식이 true일때 실행할 문장
}
```

만약 조건식이 `false`일 경우 if문 바로 다음 문장으로 넘어간다. 

```java
public class Ex01 {
	public static void main(String[] args) {
		if(true) {
			System.out.println("condition is true");
		}
		if(false) {
			System.out.println("condition is false");
		}
		System.out.println("if statements all done");
	}
}
```

> 결과

```java
condition is true
if statements all done
```

#### 조건식

if문에 사용되는 조건식은 일반적으로 비교연산자와 논리연산자로 구성된다. 조건식을 작성할 때 등가비교 연산자 `==` 대신 대입연산자 `=`를 사용하지 않도록 주의한다.

```java
public class Ex02 {
  public static void main(String[] args) {
    int x=0;
    if(x=0){  // 조건식의 결과값이 boolean이 아닌 int가 되면서 에러발생
      System.out.println("x=0 : x is 0");
    }
  }
}
```

> 결과

```java
Exception in thread "main" java.lang.Error: Unresolved compilation problem:
Type mismatch: cannot convert from int to boolean
```

#### 블럭 {}

제어문이 실행할 문장을 괄호 안에 적어 하나의 단위로 묶은 것을 `블럭`이라고 한다. 만일 블럭 내의 문장이 하나일 경우 괄호 {}는 생략이 가능하다. 다만, 나중에 코드가 추가될 경우에 괄호를 묶어주는 것을 잊어버리는 실수를 할 수 있기 때문에 가능하면 괄호를 생략하지 않는 것을 권장한다.

```java
public class Ex03 {
	public static void main(String[] args) {
		int score=85;
		if(score>90)
			System.out.println("score is over 90");
			System.out.println("congrats!");  // 원하는 결과 : 점수가 90을 넘을 경우만 출력
		if(score>80)
			System.out.println("score is over 80");
	}
}
```

> 결과

```java
congrats!
score is over 80
```

### 1.2 if-else문

if문에 else 블럭을 추가해주면 if 의 조건식이 `false`일때 else 블럭 안의 명령문을 실행한다. 두개의 if문의 조건식이 상반관계이 있을 때 사용할 수 있다. 하나의 조건식만 계산하면 되기 때문에 더 효율적이고 간단하다. 형태는 다음과 같다 :

```java
if(조건식){
  //조건식이 true일때 실행할 문장
}else{
  //조건식이 false일때 실행할 문장
}
```

### 1.3 if-else if문

처리해야 할 경우의 수가 세가지 이상인 경우에 사용한다. 첫 번째 조건식부터 순서대로 계산해서 결과가 참인 조건식을 만나면 해당 블럭만 수행하고 if-else if문 전체를 벗어난다. 형태는 다음과 같다 :

```java
if(조건식1){
  //조건식1이 true일때 실행할 문장
}else if(조건식2){
  //조건식2가 true일때 실행할 문장
}...{

}else if(조건식n){
  //조건식n이 true일때 실행할 문장
}else{
  //조건식이 전부 false일때 실행할 문장
}
```

#### if-else if문 사용 예시

```java
public class Ex04 {
	public static void main(String[] args) {
		int score=87;
		if(score>=90) {
			System.out.println("score is 90 or over.");
		}else if(score>=80){  //조건식이 true인 블럭 실행 후 
			System.out.println("score is 80 or over.");
		}else if(score>=70){
			System.out.println("score is 70 or over.");
		}else if(score>=60){
			System.out.println("score is 60 or over.");
		}else {
			System.out.println("score is under 60.");
		}
		
		System.out.println("if-else if statements all done."); //if-else if문 빠져나와 실행
	}
}
```

>결과

```java
score is 80 or over.
if-else if statements all done.
```

### 1.4 중첩 if문

if문의 블럭 안에 또다른 if 을 포함시켜 중첩 if문을 만들 수 있다. 형태는 다음과 같다 : 

```java
if(조건식1){
  //조건식1이 true일때 실행할 문장
  if(조건식2){
    //조건식1, 2가 전부 true일때 실행할 문장
  }else{
    //조건식1이 true이고 조건식2가 false일때 실행할 문장
  }
}else{
  //조건식이 전부 false일때 실행할 문장
}
```

**`주의점!`** 중첩 if문에서 괄호를 생략하여 사용할 경우 else 블럭은 가장 가까운 if문의 속한 것으로 간주된다.

```java
public class Ex05 {
	public static void main(String[] args) {
		int i=1, j=2, k=2;
		if(i==j)
			if(j==k)
				System.out.println("i=k");
		else
			System.out.println("i!=j");
	}
}
```

위의 프로그램은 아무것도 출력하지 않는다. else가 가까운 if(j==k){...}속하는 것으로 간주되고, if(i==j)(...) 의 조건식이 거짓이기 때문이다. 따라서 원하는 결과를 얻기 위해서는 다음과 같이 괄호로 묶어주어야 한다:

```java
public class Ex05 {
	public static void main(String[] args) {
		int i=1, j=2, k=2;
		if(i==j) {
			if(j==k)
				System.out.println("i=k");
		}else {
			System.out.println("i!=j");
		}
	}
}
```

>결과

```java
i!=j
```

#### 중첩 if문 사용 예시

```java
public class Ex06 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("put your score > ");
		int score=sc.nextInt();
		String grade="F", opt="0";
		
		if(score>=90) {
			grade="A";
			if(score>96) {
				opt="+";
			}else if(score<94) {
				opt="-";
			}
		}else if(score>=80) {
			grade="B";
			if(score>86) {
				opt="+";
			}else if(score<84) {
				opt="-";
			}
		}else if(score>=70) {
			grade="C";
			if(score>76) {
				opt="+";
			}else if(score<74) {
				opt="-";
			}
		}else if(score>=60) {
			grade="D";
			if(score>66) {
				opt="+";
			}else if(score<64) {
				opt="-";
			}
		}else {
			opt="";
		}
		System.out.printf("your grade is %s%s.",grade,opt);
	}
}
```

>결과

```java
put your score > 92
your grade is A-.

put your score > 75
your grade is C0.

put your score > 68
your grade is D+.

put your score > 40
your grade is F.
```

### 2. switch문

switch문은 먼저 조건식을 계산하고 그 결과와 일치하는 case문으로 이동해 해당 블럭을 실행하고 break문을 만나면 전체 switch문을 빠져나간다. 조건식의 결과와 일치하는 case문이 하나도 없는 경우 default문으로 이동한다. 형태는 다음과 같다 :

```java
switch(조건식){
  case 값1 :
    // 조건식의 결과가 값1인 경우 실행할 문장
    break;
  case 값2 :
    // 조건식의 결과가 값2인 경우 실행할 문장
    break;
  ...
  case 값n :
    // 조건식의 결과가 값n인 경우 실행할 문장
    break;
  default :
    // 조건식과 결과와 일치하는 case가 전혀 없는 경우 실행할 문장
}
```
if문은 경우의 수가 많아질수록 복잡해지고 계산해야할 조건식의 수도 많아지기 때문에 처리시간이 길어진다. 이에 비해 switch문은 하나의 조건식으로 많은 경우의 수를 처리할 수 있고 표현도 간결해 알아보기 쉽다. 다만 switch문은 제약조건이 있기 때문에 경우의 수가 많아도 어쩔 수 없이 if문을 써야하는 경우도 있다.
```java
public class Ex07 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("put any month > ");
		int month=sc.nextInt();
		String season="winter";
		
		//switch statement
		switch(month) {
			case 3: case 4: case 5:
				season="spring"; break;
			case 6: case 7: case 8:
				season="summer"; break;
			case 9: case 10: case 11:
				season="fall"; break;
			case 12: case 1: case 2:
				break;
			default: 
				season="not a valid number"; break;
		}
		System.out.printf("switch : it's %s.%n",season);
		
		//if statement
		if(month==3||month==4||month==5) {
			season="spring";
		}else if(month==6||month==7||month==8) {
			season="summer";
		}else if(month==9||month==10||month==11) {
			season="fall";
		}else if(month>13||month<1) {
			season="not a valid number";
		}
		System.out.printf("if : it's %s.",season);
	}
}
```

>결과

```
put any month > 0
switch : it's not a valid number.
if : it's not a valid number.

put any month > 2
switch : it's winter.
if : it's winter.

put any month > 5
switch : it's spring.
if : it's spring.

put any month > 6
switch : it's summer.
if : it's summer.

put any month > 9
switch : it's fall.
if : it's fall.
```

switch 문에서 break문은 각각의 case문을 구분해준다. 만약 실행한 case문에 break문이 없으면 다음 break문을 만나거나 switch문이 끝날때까지 모든 문장을 수행한다. 그렇기 때문에 break문을 빠뜨리고 쓰지 않는 실수를 주의해야 한다. 그러나 경우에 따라서는 고의적으로 break문을 생략하기도 한다.

```java
switch(level){
  case 3: 
    grantDelete();
  case 2:
    grantWrite();
  case 1:
    grantRead();
}
```

위쪽부터 밑으로 차례대로 수행되기 때문에 레벨이 3일 경우 모든 권한을 부여받고, 레벨이 1인 경우 읽기 권한만 부여받는다.

#### switch문의 제약조건

switch문의 조건식은 결과값이 반드시 정수여야 하고 case문의 값 역시 정수여야 한다. 변수나 실수, 문자열은 case문의 값으로 사용할 수 없다.

```java
public class Ex08 {
	public static void main(String[] args) {
		int result=1;
		int num=0; 
		final int one=1;
		
		switch(result) {
			case one: // integer constant
			case '1': // character constant
			case num: // Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
								// case expressions must be constant expressions
			case 1.0: // Eception in thread "main" java.lang.Error: Unresolved compilation problem: 
								// Type mismatch: cannot convert from double to int
		}
	}
}
```

---

## 반복문

반복문은 어떤 작업을 반복적으로 실행할때 사용하며 종류로는 for문, while문, do-while문이 있다. for문이나 while문에 속한 문장은 조건에 따라 한번도 수행되지 않을 수 있지만 do-while문에 속한 문장은 최소한 한번은 반드시 실행된다. 반복문도 조건식을 포함하며, 조건식의 결과가 `true`일때 문장을 수행하고 `false`일때는 건너뛴다.

### 1.1 for문

for문은 일반적인 반복패턴에서 while문이나 do-while문보다 반복구조를 보기가 더 편하다. 대부분의 반복문은, 반복문이 시작하기 전에 초기화되는 값, 반복문을 실행할 것인지를 분별할 조건식, 반복문 재실행 전에 실행될 증감식을 가진다. 이러한 초기화, 조건식, 증감식은 반복문에서 가장 중요한 세가지 요소인데 for문은 이 세 단계를 명시적으로 보여준다.

```java
for(초기화;조건식;증감식){
  //조건식의 결과값이 참일 동안 반복 실행할 문장
}
```

이는 다음에 오는 while문과 동일하다.

```java
초기화;
while(조건식){
  //조건식의 결과값이 참일 동안 반복 실행할 문장
  증감식;
}
```

for문의 경우 초기화, 조건식, 증감식을 반복문의 맨 위에서 모두 명시해주기 때문에 해당 반복문이 어떤 조건으로 수행되는지 이해하기 쉽고 초기화나 증감식을 잊어버리는 등의 실수들을 막아준다. 이 세가지 요소는 필요하지 않으면 생략할 수 있고 모두 생략하는 것도 가능하다. 조건식이 생략된 경우 참으로 간주되어 무한반복문이 된다. for문도 중첩사용이 가능하다.

#### for문 사용 예시

- 삼각형 별모양 출력하기
```java
public class Ex01 {
	public static void main(String[] args) {
		for(int i=0;i<5;i++) {
			for(int j=0;j<=i;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
		System.out.println("");
		for(int i=5;i>0;i--) {
			for(int j=0;j<i;j++){
				System.out.print("*");
			}
			System.out.println("");
		}
	}
}
```

>결과

```java
*
**
***
****
*****

*****
****
***
**
*
```

- 구구단 출력하기

```java
public class Ex02 {
	public static void main(String[] args) {
		for(int i=2;i<10;i++) {
			System.out.printf("[%d단] ",i);
			for(int j=1;j<10;j++) {
				System.out.printf("%dx%d=%-2d ",i,j,i*j);
			}
			System.out.println("");
		}
	}
}
```

>결과

```java
[2단] 2x1=2  2x2=4  2x3=6  2x4=8  2x5=10 2x6=12 2x7=14 2x8=16 2x9=18 
[3단] 3x1=3  3x2=6  3x3=9  3x4=12 3x5=15 3x6=18 3x7=21 3x8=24 3x9=27 
[4단] 4x1=4  4x2=8  4x3=12 4x4=16 4x5=20 4x6=24 4x7=28 4x8=32 4x9=36 
[5단] 5x1=5  5x2=10 5x3=15 5x4=20 5x5=25 5x6=30 5x7=35 5x8=40 5x9=45 
[6단] 6x1=6  6x2=12 6x3=18 6x4=24 6x5=30 6x6=36 6x7=42 6x8=48 6x9=54 
[7단] 7x1=7  7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49 7x8=56 7x9=63 
[8단] 8x1=8  8x2=16 8x3=24 8x4=32 8x5=40 8x6=48 8x7=56 8x8=64 8x9=72 
[9단] 9x1=9  9x2=18 9x3=27 9x4=36 9x5=45 9x6=54 9x7=63 9x8=72 9x9=81
```

### 1.2 향상된 for문(enhanced for statement)

향상된 for문은 배열과 컬렉션에 저장된 요소에 접근할 때 기존보다 편리하고 간결한 방법으로 처리할 수 있다. 그러나 향상된 for문은 일반적인 for문과 다르게 배열이나 컬렉션에 저쟝된 요소들을 읽어오는 용도로만 사용할 수 있다.

```java
for(타입 변수명 : 배열/컬렉션){
  //반복할 문장
}
```

#### 향상된 for문 사용 예시

```java
public class Ex03 {
	public static void main(String[] args) {
		int[] arr= {1,2,3,4,5,6,7};
		//enhanced for statement
		for(int a:arr) {
			System.out.print(a);
		}
		System.out.println("");
		
		// for statement
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]);
		}
	}
}
```

>결과

```java
1234567
1234567
```

### 2. while문

while문은 자바의 기본적인 반복문 구조 중 하나이다. 조건식의 결과값을 판별해서 그 값이 참인 동안 while문에 속하는 문장을 반복 수행하고, 조건식이 false가 되는 순간 반복문을 빠져나와 다음 코드로 넘어간다. while(true){...}로 무한반복하는 형태로 만들수도 있다. 위에서 살펴봤듯이 for문과 while문은 항상 서로 변환이 가능하다. 초기화나 증감식이 필요하지 않은 경우아는 while문이 더 적합하다.

```java
while(조건식){
  //조건식의 결과값이 참일 동안 반복 실행할 문장
}
```

#### while문의 조건식 생략 불가

for문과 달리 while문의 조건식은 생략할 수 없다. 그래서 while문의 조건식이 항상 참이 되도록 하려면 반드시 `true`를 넣어야 한다. 그러나 이렇게 되면 무한 반복문이 되기 때문에 반드시 블럭 안에 조건문을 넣어서 특정 조건을 만족하면 무한 반복문을 벗어나도록 해야 한다.

#### while문 사용 예시

```java
public class Ex04 {
	public static void main(String[] args) {
		int i=5;
		while(i>0) {
			System.out.println("countdown : "+i);
			i--;
		}
	}
}
```

>결과

```java
countdown : 5
countdown : 4
countdown : 3
countdown : 2
countdown : 1
```

### 3. do-while문

do-while문의 기본적인 구조는 while문과 같지만 조건식과 블럭의 순서를 바꾸어 놓아서 먼저 블럭을 수행하고 조건식을 평가한다. 따라서 최소 한번은 블럭이 수행된다.

```java
do{
  //실행할 문장
}while(조건식);
```

#### do-while문 사용 예시

```java
public class Ex04 {
	public static void main(String[] args) {
		System.out.println("<<<up down game>>>");
		System.out.print("put a number between 1 and 10 > ");
    Scanner sc=new Scanner(System.in);
    int n=0;
    int rn=(int)(Math.random()*10+1);
    do{
      n=sc.nextInt();
      if(n<rn){
        System.out.print("up > ");
      }else if(n>rn){
        System.out.print("down > ");
      }
    }while(n!=rn);
		System.out.println("Correct!");
	}
}
```

>결과

```java
<<<up down game>>>
put a number between 1 and 10 > 5
up > 7
down > 6
Correct!
```

<!-- 
## JUnit5 테스트

인텔리J, 이클립스, VS Code에서 JUnit 5로 테스트 코드 작성하는 방법에 익숙해 질 것.

**_JUnit4 vs JUnit5_**

## live-study 대시보드 코드

깃헙 이슈 1번부터 18번까지 댓글을 순회하며 댓글을 남긴 사용자를 체크 할 것.
참여율을 계산하세요. 총 18회에 중에 몇 %를 참여했는지 소숫점 두자리가지 보여줄 것.
Github 자바 라이브러리를 사용하면 편리합니다.
깃헙 API를 익명으로 호출하는데 제한이 있기 때문에 본인의 깃헙 프로젝트에 이슈를 만들고 테스트를 하시면 더 자주 테스트할 수 있습니다.

## LinkedList

LinkedList에 대해 공부하세요.
정수를 저장하는 ListNode 클래스를 구현하세요.
ListNode add(ListNode head, ListNode nodeToAdd, int position)를 구현하세요.
ListNode remove(ListNode head, int positionToRemove)를 구현하세요.
boolean contains(ListNode head, ListNode nodeTocheck)를 구현하세요.

## Stack

int 배열을 사용해서 정수를 저장하는 Stack을 구현하세요.
void push(int data)를 구현하세요.
int pop()을 구현하세요.

## 앞서 만든 ListNode를 사용한 Stack

ListNode head를 가지고 있는 ListNodeStack 클래스를 구현하세요.
void push(int data)를 구현하세요.
int pop()을 구현하세요.

## Queue

배열을 사용해서 한번
ListNode를 사용해서 한번. 
-->

---

## 참고자료

- 남궁성. _Java의 정석 3판._ 도우출판, 2016.
- Evans, Benjamin J. and David Flanagan. _Java in a Nutshell._ O'Reilly Media, 2019.
- https://howtodoinjava.com/java/flow-control/control-flow-statements/
