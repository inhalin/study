 자바 라이브 스터디] 11주차 - Enum

#### 목표

```
자바의 열거형에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- 🟡 enum 정의하는 방법
- 🟡 enum이 제공하는 메소드 (values()와 valueOf())
- 🟡 java.lang.Enum
- 🟡 EnumSet

--- 

## enum 정의하는 방법

열거형은 서로 관련된 여러 상수를 정의할 때 사용한다. 

#### 장점

- 열거체를 비교할 때 실제 값 뿐 아니라 타입까지 체크한다.
- 열거체의 상수값이 재정의되어도 다시 컴파일할 필요가 없다.

#### 정의
```java
enum Direction{ EAST, SOUTH, WEST, NORTH }
```

#### 사용법
```java
class MyEnum{
  Direction dir;

  void init(){
    dir = Direction.EAST;
  }
}
```

---

## enum이 제공하는 메소드 (values()와 valueOf())

### values()

- 열거형의 모든 상수를 배열에 담아 반환
- 모든 열거형이 가지고 있고 컴파일러가 자동으로 추가해줌

#### valueOf()

- 열거형 상수의 이름으로 문자열 상수에 대한 참조를 얻음

```java
Direction d = Direction.valueOf("SOUTH");

System.out.println(d);  // SOUTH
```

---

## java.lang.Enum

모든 열거형의 조상으로 아래 표와 같은 메서드가 정의되어 있다.
| 메서드 | 설명 |
|---|---|
| static E values() | 해당 열거체의 모든 상수를 저장한 배열을 생성하여 반환 |
| protected void finalize() | 해당 Enum 클래스가 final 메소드를 가질 수 없게 됨 |
| static E valueOf(String name) | 전달된 문자열과 일치하는 해당 열거체의 상수를 반환 |
| Class<E> getDeclaringClass() | 열거형의 Class 객체 반환 |
| String name() | 열거형 상소 이름 문자열로 반환 |
| int ordinal() | 열거형 상수가 정의된 순서 반환(0부터 시작) |
| T valueOf(Class<T> enumType, String name) | 지정된 열거형에서 name와 일치하는 열거형 상수 반환 |

---

## EnumSet

`java.util.EnumSet` 클래스는 enum 타입과의 사용을 위해 특화된 Set 구현이다. 

EnumSet의 주요 포인트
- enum set의 모든 요소는 그 set이 만들어졌을 때 명시적으로든 암묵적으로든 지정된 단일 enum 타입에서 와야 한다.
- Enum set은 내부적으로 비트 벡터로 나타냅니다.
- EnumSet은 동기화되어 있지 않다. 만약에 여러 스레드가 동시에 enum set에 접근해서 그중 최소 하나의 스레드가 set을 변경한다면 enum set은 외부적으로 동기화되어야 한다.

---

## 참고자료
 
- 남궁성. *Java의 정석 3판.* 도우출판, 2016.
- https://www.tcpschool.com/java/java_api_enum
- https://www.tutorialspoint.com/java/util/java_util_enumset.htm
<!--- Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.
- https://docs.oracle.com/javase/specs/jls/se15/html/jls-17.html
- https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.State.html
- https://howtodoinjava.com/java/multi-threading/
- https://www.baeldung.com/java-daemon-thread -->
