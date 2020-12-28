# 자바 라이브 스터디 6주차

#### 목표

```
자바의 패키지에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- 🟢 package 키워드
- ⚪ import 키워드
- ⚪ 클래스패스
- ⚪ CLASSPATH 환경변수
- ⚪ -classpath 옵션
- ⚪ 접근지시자

---

## Package

패키지는 클래스의 묶음이다. 패키지에는 클래스 또는 인터페이스를 포함할 수 있고 서로 관련된 클래스들끼리 그룹 단위로 묶어서 클래스를 효율적으로 관리할 수 있다. 서로 다른 패키지 안에 같은 이름의 클래스가 존재할 수 있다. 클래스의 전체이름(full name)은 패키지명을 포함한다. 그렇기 때문에 클래스 이름이 같더라도 패키지명으로 구별이 가능하다. 

클래스가 물리적으로 하나의 클래스파일(.class)인 것과 같이 **패키지는 물리적으로 하나의 디렉토리**이다. 디렉토리가 하위 디렉토리를 갖듯이, 패키지도 다른 패키지를 포함할 수 있고 점 `.`으로 구분한다.

예를 들어 String 클래스의 full name은 java.lang.String이다. 즉, java.lang 패키지에 속한 String 클래스라는 의미이다. 물리적으로는 디렉토리 java의 서브 디렉토리 lang에 속한 String.class 파일이다. 

![String directory](img/week7/string_dir.png)

Date 클래스는 동일 클래스 이름으로 java.util 패키지에 속한 Date 클래스, java.sql에 속한 Date 클래스 두 개가 있는 것이 보이고 패키지명으로 구별할 수 있다.

![date package](img/week7/date_pkg.png)

```
- 하나의 소스파일에는 첫 줄에 단 한 번의 패키지 선언만을 허용한다.
- 모든 클래스는 반드시 하나의 패키지에 속해야 한다.
- 패키지는 점(.) 을 구분자로 하여 계층구조로 구성할 수 있다.
- 패키지는 물리적으로 클래스파일(.class)을 포함하는 하나의 디렉토리이다.
```

---

## package 키워드

클래스나 인터페이스의 소스파일에 다음과 같이 패키지를 선언해준다:

```java
package 패키지명;
```

패키지 선언문은 주석과 공백을 제외하고 반드시 첫 줄에 와야하며 하나의 소스파일에 단 한번만 선언될 수 있다. 패키지명은 대소문자 모두 가능하지만 클래스명과 구분하기 쉽게 소문자로 하는 것이 원칙이다.

소스파일에 자신이 속할 패키지를 지정하지 않은 클래스는 자동적으로 `unnamed package`에 속하게 된다. 따라서 패키지를 지정하지 않는 모든 클래스들은 같은 패키지에 속하게 된다.

---

## import 키워드

---

## 클래스패스

---

## CLASSPATH 환경변수

---

## -classpath 옵션

---

## 접근지시자

---

## 참고자료

1. 남궁성. *Java의 정석 3판.* 도우출판, 2016.

2. Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.

3. https://howtodoinjava.com/java/basics/java-classpath/

4. https://docs.oracle.com/javase/tutorial/java/package/index.html