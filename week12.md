# 자바 라이브 스터디 12주차

#### 목표

```
자바의 애노테이션에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- ⚪ 애노테이션 정의하는 방법
- ⚪ @Retention
- ⚪ @Target
- ⚪ @Documented
- ⚪ 애노테이션 프로세서

---

## 애너테이션이란

애너테이션은 자바에서 프로그램의 소스코드 안에 다른 프로그램을 위한 정보를 미리 약속된 형식으로 포함시킨 것이다. 애너테이션은 주석처럼 프로그래밍 언어에 영향을 미치지 않으면서 다른 프로그램에 유용한 정보를 제공할 수 있다. 

예를 들어 소스코드 중에 특정 메서드만 테스크하고 싶다면 `@Test`라는 애너테이션을 메서드 앞에 붙여주만 된다. 그렇다고 모든 프로그램에게 의미가 있는 건 아니고 해당 프로그램에 미리 정의된 종류와 형식으로 작성해야만 의미가 있다. 즉 `@Test`는 테스트 프로그램을 제외한 다른 프로그램에는 아무 의미 없는 것이다.

```java
@Test
public void someMethod(){
  // write test code here
}
```

애너테이션은 JDK에서 기본적으로 제공하는 것과 다른 프로그램에서 제공하는 것이 있다. JDK에서 제공하는 표준 애너테이션은 주로 컴파일러를 위한 것으로 컴파일러에게 유용한 정보를 제공한다. 새로운 애너테이션을 정의할 수 있는 메타 애너테이션도 제공한다.

### 표준 애너테이션

애너테이션 | 설명
---|---
@Override | 컴파일러에게 오버라이딩하는 메서드라는 것을 알린다.
@Deprecated | 앞으로 사용하지 않을 것을 권장하는 대상에 붙인다.
@SupperessWarnings | 컴파일러의 특정 경고메시지가 나타나지 않게 해준다
@SafeVarargs | 지네릭스 타입의 가변인자에 사용한다.
@FunctionalInterface | 함수형 인터페이스라는 것을 알린다.
@Nativenative | 메서드에서 참조되는 상수 앞에 붙인다.
@Target * | 애너테이션이 적용가능한 대상을 지정하는데 사용한다.
@Documented * | 애너테이션 정보가 javadoc으로 작성된 문서에 포함되게 한다.
@Inherited * | 애너테이션이 자손 클래스에 상속되도록 한다.
@Retention * | 애너테이션이 유지되는 범위를 지정하는데 사용한다.
@Repeatable * | 애너테이션을 반복해서 적용할 수 있게 한다.

<small>* 표시 : 메타 애너테이션</small> 

#### @Override

메서드 위에만 붙일 수 있는 애너테이션으로 조상의 메서드를 오버라이딩하는 걸 컴파일러에게 알려주는 역할을 한다. 오버라이딩 할때 메서드의 이름을 잘못 쓰면 컴파일러는 새로운 이름의 메서드가 추가된 것으로 인식하고 만다. 하지만 `@Override`를 붙여주면 컴파일러가 조상 클래스에 동일한 이름의 메서드가 있는지 확인하고 잘못된 경우 에러를 발생시킨다.

#### @Deprecated

새로운 버전에 JDK가 소개될 때 기존의 기능을 대채할 수 있는 새로운 기능이 추가되면서 더이상 사용되지 않는 필드나 메서드에 더이상 사용하지 않을 것을 권하는 의미로 `@Deprecated`를 붙여준다. 

기존의 것에 해당 애너테이션이 붙어있더라도 사용할 수 는 있지만 가능하면 `@Deprecated`가 붙은 것은 사용하지 않는 것이 좋다. 

#### @FunctionalInterface

함수형 인터페이스를 선언할 때 이 애너테이션을 붙이면 컴파일러가 함수형 인터페이스를 올바르게 선언했는지 확인하고 잘못된 경우 에러를 발생시킨다.

#### @SuppressWarnings

컴파일러가 보여주는 경고메시지가 나타나지 않게 해준다. 해당 애너테이션을 억제할 수 있는 경고메시지의 종류는 deprecation, unchecked, rawtypes, varargs 등이 있고 JDK 버전이 올라가면서 추가 될 수 있다. 

종류 | 억제할 경고메시지
---|---
deprecation | `@Deprecated`가 부튼 대상을 사용해서 발생하는 경고
unchecked | 지네릭스로 타입을 지정하지 않았을 때 발생하는 경고
rawtypes | 지네릭스를 사용하지 않아서 발생하는 경고
varargs | 가변인자의 타입이 지네릭 타입일 때 발생하는 경고

```java
@SuppressWarnings("unchecked")
ArrayList list = new ArrayList();
list.add(Obj);

// 둘 이상의 경고를 동시에 억제할 때는 아래와 같이 사용한다.
@SuppressWarnings({"deprecation", "unchecked","varargs"})
```

사용방법은 위와 같이 억제하려는 경고메시지를 애너테이션 뒤의 괄호 안에 문자열고 지정해준다. 경고메시지의 종류는 `-Xlint` 옵션으로 컴파일하면 경고내용을 자세하게 볼 수 있는데 거기에서 대괄호 안에 있는 것이 메시지의 종류이다. 

`@SuppressWarnings`를 붙이면 해당 대상에 포함되는 모든 코드에서 경고가 억제되기 때문에 경고의 억제범위는 최소화하는 것이 좋다.

#### @SafeVarargs

`@SafeVarargs`는 `static`이나 `final`이 붙은 메서드나 생성자에만 붙일 수 있다. 즉 오버라이드되는 메서드에는 사용할 수 없다.

컴파일 후에 제거되는 타입을 reifiable 타입이라고 하고 제거되지 않는 타입을 non-reifiable 타입이라고 한다. 지네릭 타입들은 대부분 컴파일시에 제거되기 때문에 non-reifiale 타입이다. 이때 해당 메서드를 선언하는 부분과 호출하는 부분에서 unchecked 경고가 발생한다. 이럴 때 메서드 앞에 `@SafeVarargs`를 붙여서 해당 메서드의 가변인자는 타입 안정성이 있다고 컴파일러에 알려서 경고가 발생하지 않도록 해준다.

메서드를 선언할때 `@SafeVarargs`를 붙이면 해당 메서드를 호출하는 곳에서 발생하는 경고도 전부 억제된다. 반면에 `@SuppressWarnings("unchecked")`를 사용하면 메서드를 선언하고 호출되는 곳마다 애너테이션을 붙여야한다.

`@SafeVarargs`는 unchecked 경고는 억제하지만 vargars 경고는 억제하지 않기 때문에 가능하다면 습관적으로 `@SafeVarargs`와 `@SuppressWarnings("vargars")`를 같이 붙여주는 것이 좋다.

## 애너테이션 정의하는 방법



---

## @Retention



---

## @Target



---

## @Documented



---

## 애노테이션 프로세서



---

## 참고자료

1. 남궁성. *Java의 정석 3판.* 도우출판, 2016.

2. Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.

3. https://docs.oracle.com/javase/specs/jls/se15/html/jls-17.html

4. https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.State.html

5. https://howtodoinjava.com/java/multi-threading/

6. http://www.tcpschool.com/java/java_thread_concept

7. https://www.baeldung.com/java-daemon-thread
