# 자바 라이브 스터디 8주차

#### 목표

```
자바의 인터페이스에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- 🟢 인터페이스 정의하는 방법
- 🟢 인터페이스 구현하는 방법
- 🟡 인터페이스 레퍼런스를 통해 구현체를 사용하는 방법
- 🟡 인터페이스 상속
- 🟢 인터페이스의 기본 메소드 (Default Method), 자바 8
- 🟢 인터페이스의 static 메소드, 자바 8
- 🟡 인터페이스의 private 메소드, 자바 9

---

## 인터페이스 정의하는 방법

인터페이스는 오로지 추상메소드와 상수만을 멤버로 가질 수 있다. 인터페이서를 정의할 때는 클래스를 작성하는 것과 같은데 키워드로 `interface`를 사용한다. 인터페이스의 멤버들은 아래와 같은 제약사항이 있다:

    1. 모든 멤버변수는 `public static final`이어야 하고 이를 생략할 수 있다.
    2. 모든 메소드는 `public abstract`이어야 하고 이를 생략할 수 있다.

```java
interface Myinterface{
  public static final int PI=3.141592;
  final int e=2.71828;
  static double light=3.0e8;
  double GRAVITY=6.67e-11;

  public abstract int getArea();
  double getWeight();
}
```

---

## 인터페이스 구현하는 방법

인터페이스는 그 자체로 인스턴스를 생성할 수 없고 자신에 정의된 추상메소드를 구현할 클래스를 정의해야 한다. 이때 키워드는 `implements`를 사용한다.

```java
class MyClass implements MyInterface{
  public int getArea(){
    // 생략
  }
  public double getWeight(){
    // 생략
  }
}
```

만약 구현하는 인터페이스의 메소드 중 일부만 구현한다면 `abstract`를 붙여서 추상클래스로 선언해야 한다.

```java
abstract PartialClass implements MyInterface{
  public int getArea(){
    // 생략
  }
}
```

---

## 인터페이스 레퍼런스를 통해 구현체를 사용하는 방법

```java
interface Shape{
    void draw();
}

class Square implements Shape{
    @Override
    public void draw() {
        System.out.println("This is a square.");
    }
}

class Circle implements Shape{
    @Override
    public void draw() {
        System.out.println("This is a circle.");
    }
}
public class ReferenceImplements {
    public static void main(String[] args) {
        Shape shape1=new Square();
        Shape shape2=new Circle();

        shape1.draw();
        shape2.draw();
    }
}
```
```java
// 결과
This is a square.
This is a circle.
```

---

## 인터페이스 상속

인터페이스는 다중상속이 가능하고 자손 인터페이스는 조상 인터페이스에 정의된 멤버를 모두 상속받는다.

### 인터페이스를 이용한 다중상속

인터페이스는 static 상수만 정의할 수 있기 때문에 조상 클래스의 멤버변수와 충돌하는 경우는 거의 없고 충돌되더라도 클래스 이름을 붙여서 구분이 가능하다. 또 추상메소드는 구현내용이 없기 때문에 조상클래스의 메소드와 선언부가 일치해도 조상클래스의 메소드를 상속받으면 되기 때문에 문제가 없다.

다만 이렇게 하면 다중상속의 장점을 잃게 된다. 만약 두 클래스에서 상속을 받아야 된다면 둘 중 비중이 높은 쪽을 선택하고 다른 쪽은 클래스 내부에 멤버로 포함시키거나 필요한 부분을 인터페이스로 만든 다음 구현하도록 한다.

---

## 인터페이스의 기본 메소드 (Default Method), 자바 8

인터페이스에서 메소드가 추가된다면 해당 인터페이스를 구현한 기존의 모든 클래스에서 새로 추가된 메소드를 구현해야 한다. 그리고 그 클래스의 수가 많다면 이는 굉장히 번거롭고 큰 일이 될 수 있다. 그래서 나온 것이 디폴드 메소드이다. 

디폴트 메소드는 추상 메소드의 기본적인 구현을 제공하는 메소드로 추상메소드가 아니기 때문에 디폴트 메소드가 새로 추가되어도 해당 인터페이스를 구현한 클래스를 변경하지 않아도 된다. 

디폴트 메소드는 앞에 키워드 `default`를 붙이고 추상메소드와 다르게 일반 메소드처럼 구현부가 있어야 한다. 접근제어자는 `public`이고 생략 가능하다.

```java
inteface MyInterface{
  // ...
  default void newMethod(){
    // 코드작성
  }
}
```

새로 추가된 디폴트 메소드가 기존 메소드 이름과 중복되서 충돌하는 경우과 해결하는 규칙은 다음과 같다:

    1. 여러 인터페이스의 디폴트 메소드 간의 충돌 - 인터페이스를 구현한 클래스에서 디폴트 메소드를 오버라이딩한다.
    2. 디폴트 메소드와 조상 클래스 메소드 간의 충돌 - 조상 클래스의 메소드가 상속되고 디폴트 메소드는 무시된다.

#### 1. default 메소드가 있는 interface를 구현하는 Child class

```java
interface Printable{
    default void printStr(){
        System.out.println("default method printStr() in Printable interface");
    }
}

class Child implements Printable{
   public void printThis(){
       System.out.println("printThis() method in Child class");
   }
}

public class DefaultMethodTest {
    public static void main(String[] args) {
        Child child = new Child();
        child.printStr();
        child.printThis();
    }
}
```
```java
// 결과
default method printStr() in Printable interface
printThis() method in Child class
```

#### 2. 이름이 중복되는 default 메소드를 가진 interface를 두개 구현하는 Child class

```java
interface Printable{
    default void printStr(){
        System.out.println("default method printStr() in Printable interface");
    }
}

interface Changeable {
    default void printStr(){
        System.out.println("default method printStr() in Changeable interface");
    }
}

class Child implements Printable,Changeable{
   public void printThis(){
       System.out.println("printThis() method in Child class");
   }

    @Override
    public void printStr() {
        System.out.println("printStr() method overridden in Child class");
    }
}

public class DefaultMethodTest {
    public static void main(String[] args) {
        Child child = new Child();
        child.printStr();
        child.printThis();
    }
}
```
```java
// 결과
printStr() method overridden in Child class
printThis() method in Child class
```

#### 3. interface의 default 메소드 이름과 부모 클래스의 메소드 이름이 중복되는 Child class

```java
interface Printable{
    default void printStr(){
        System.out.println("default method printStr() in Printable interface");
    }
}

interface Changeable {
    default void printStr(){
        System.out.println("default method printStr() in Changeable interface");
    }
}

class Parent{
    public void printStr(){
        System.out.println("printStr() method in Parent class");
    }
}

class Child extends Parent implements Printable,Changeable{
   public void printThis(){
       System.out.println("printThis() method in Child class");
   }
}

public class DefaultMethodTest {
    public static void main(String[] args) {
        Child child = new Child();
        child.printStr();
        child.printThis();
    }
}
```
```java
// 결과
printStr() method in Parent class
printThis() method in Child class
```

---

## 인터페이스의 static 메소드, 자바 8

static 메소드는 인스턴스와 관계 없는 독립적인 메소드이다. 자바의 규칙을 단순하게 하면서도 인터페이스의 모든 메소드는 추상 메소드여야 한다는 규칙에 예외를 두지 않기 위해 인터페이스와 관련된 static 메소드는 별도의 클래스에 따로 두어야 했다.

인터페이스의 static 메소드의 접근 제어자도 항상 `public`이고 생략가능하다.

```java
interface Usable{
    static void printStr(){
        System.out.println("static method printStr() in Usable Interface");
    }
}

public class StaticMethodInterface {
    public static void main(String[] args) {
        Usable.printStr();
    }
}
```
```java
// 결과
static method printStr() in Usable Interface
```

---

## 인터페이스의 private 메소드, 자바 9

인터페이스의 private 메소드는 인터페이스 내의 코드 재사용을 용이하게 한다. 예를 들어 두개의 default 메소드가 코드를 공유할 때 private 메소드가 이것을 가능하게 하고 이 과정이 해당 인터페이스를 구현하는 클래스에 노출되지 않는다.

인터페이스에서 private 메소드를 사용하기 위한 네가지 규칙이 있다:

1. private 메소드는 구현부를 가져야만 한다.
2. 오직 인터페이스 내부에서만 사용할 수 있다. 
3. private static 메소드는 다른 static 또는 static이 아닌 메소드에서 사용할 수 있다.
4. static이 아닌 private 메소드는 다른 private static 메소드에서 사용할 수 없다.

```java
interface CustomCalculator
{
    default int addEvenNumbers(int... nums) {
        return add(n -> n % 2 == 0, nums);
    }

    default int addOddNumbers(int... nums) {
        return add(n -> n % 2 != 0, nums);
    }

    private int add(IntPredicate predicate, int... nums) {
        return IntStream.of(nums)
                .filter(predicate)
                .sum();
    }
}
```
코드 출처 : https://howtodoinjava.com/java9/java9-new-features-enhancements/#interface-private-methods

---

## 참고자료

1. 남궁성. *Java의 정석 3판.* 도우출판, 2016.

2. Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.

3. https://howtodoinjava.com/java9/java9-new-features-enhancements/#interface-private-methods

4. https://docs.oracle.com/javase/tutorial/java/IandI/index.html

5. https://docs.oracle.com/javase/specs/jls/se15/html/jls-9.html

6. http://www.tcpschool.com/java/java_polymorphism_interface
