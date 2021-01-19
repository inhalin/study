# 자바 라이브 스터디 10주차

#### 목표

```
자바의 멀티쓰레드 프로그래밍에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- 🟡 Thread 클래스와 Runnable 인터페이스
- 🟢 쓰레드의 상태
- ⚪ 쓰레드의 우선순위
- 🟡 Main 쓰레드
- 🟡 동기화
- ⚪ 데드락

<!-- 
필수 - runnable, thread 무슨 메서드이고 무슨 상태인지 우선순위는 어떻게 되는지
      main thread, 동기화란, 어떻게 처리되나
      lock으로 쓰는 obj, lock의 개념, lock을 잡는다?, 종류, deadlock
선택 - callable, threadpool
      ForkJoinPool https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html
 -->


---

## 프로세스와 쓰레드

프로세스는 프로그램을 실행하면 필요한 메모리와 데이터 등의 자원을 할당받고 쓰레드는 이 자원을 이용해 실제로 작업을 수행한다. 모든 프로세스는 최소한 하나 이상의 쓰레드가 존재하고 둘 이상의 쓰레드를 가진 프로세스를 **멀티쓰레드 프로세스**라고 한다. 

지금까지 공부한 내용들은 한번에 하나의 작업만 실행하는 싱글 쓰레드에 대해 보았는데, JVM은 한번에 여러 쓰레드가 작업하는 것을 지원한다. 멀티쓰레드는 공유 주기억 장치에 있는 값과 객체에 대해 작동하는 각각의 코드를 실행한다. 멀티쓰레드는 여러개의 하드웨어 프로세서를 갖거나, 하나의 하드웨어 프로세서를 시간분할하거나, 여러개의 하드웨어 프로세서를 시간분할 함으로써 지원될 수 있다.

쓰레드를 만들기 위해서는 반드시 `Thread` 클래스의 객체를 만들어야 한다. 쓰레드는 해당하는 `Thread` 객체에서 `start()` 메서드를 호출할때 작업을 시작한다.

멀티쓰레드의 동작은 특히나 제대로 동기화 되지 않았을때 헷갈릴 수 있다. 멀티쓰레드에서 업데이트된 공유자원의 read에 의해 어떤 값이 보일 것인지에 대한 규칙이 있다. 

### 멀티쓰레딩의 장단점

멀티쓰레딩의 장점은 다음과 같다

- CPU의 사용률을 향상시킨다.
- 자원을 보다 효율적으로 사용할 수 있다.
- 사용자에 대한 응답성이 향상된다.
- 작업이 분리되어 코드가 간결해진다.

여러 사용자에게 서비스를 해주는 서버 프로그램의 경우 멀티쓰레드로 작성하는 것은 필수적이다. 하나의 서버 프로세스가 여러개의 쓰레드를 생성해서 쓰레드와 사용자의 요청이 일대일로 처리되도록 프로그래밍해야 한다.

그러나 멀티쓰레드 프로세스는 여러 쓰레드가 같은 프로세스 내에서 자원을 공유하며 작업하기 때문에 동기화(synchronization), 교착상태(deadlock)와 같은 문제가 있을 수 있어서 신중하게 프로그래밍해야 한다.

---

## Thread 클래스와 Runnable 인터페이스

쓰레드를 구현하는 방법은 Thread 클래스를 상속받는 방법과 Runnable 인터페이스를 구현하는 방법 두가지가 있다. Thread를 상속받으면 다른 클래스를 상속받을 수 없기 때문에 Runnable 인터페이스를 구현하는 방법이 일반적이다. 또한 Runnable 인터페이스를 구현하면 재사용성이 높고 코드의 일관성을 유지할 수 있기 때문에 더 객체지향적이다. 

Runnable 인터페이스를 구현하는 것은 쓰레드의 동작을 특별히 바꾸는 것이 아니라 그저 쓰레드가 동작시킬 무언가를 전달하는 것 뿐이다. Thread 클래스를 상속받은 자식클래스는 어떤 동작을 하든 쓰레드 안에서 이루어진다. 

만약 JDK4나 그 이하버전에서 작업을 한다면 `start()` 메서드를 실행하지 않은 쓰레드가 있다면 그 쓰레드 메모리 누수가 생긴다. (http://bugs.java.com/bugdatabase/view_bug.do;jsessionid=5869e03fee226ffffffffc40d4fa881a86e3:WuuT?bug_id=4533087)

Java 1.5부터 버그가 고쳐졌지만 1.4 이하에서는 여전히 버그가 생긴다. 이 문제는 프로그램을 빌드할 때 쓰레드가 내부 쓰레드 테이블의 참조리스트에 추가되는데, `start()` 메소드가 완료될까지 이 리스트에서 지워지지 않고 쓰레드가 그 참조에 있는 한 가비지 컬렉션이 일어나지 않기 때문에 발생하는 것이다.

```java
public class ThreadAndRunnable {
    public static void main(String[] args) {
        // 1. Thread의 자손클래스 인스턴스 생성
        MyThread t1 = new MyThread(); 
        
        // 2. Runnable을 구현한 클래스의 인스턴스 생성
        MyRunnable r = new MyRunnable();  
        Thread t2 = new Thread(r);  // 생성자 Thread(Runnable target)
        
        // 3. 두번째 방법을 줄여쓴 코드
        Thread t3 = new Thread(new MyRunnable()); 

        t1.start();
        t2.start();
        t3.start();
    }
}

// Thread 클래스 상속
class MyThread extends Thread {

    public void run(){
        System.out.println("MyThread is " + getName()); 
        // getName() -> Thread 클래스의 메서드 직접 호출 가능
    }
}

// Runnable 인터페이스 구현
class MyRunnable implements Runnable {

    @Override
    public void run() {
        System.out.println("MyRunnable is " + Thread.currentThread().getName());  
        // Thread.currentThread().getName() 
        //   -> Thread 클래스의 static 메서드인 currentThread()를 호출해서 쓰레드에 대한 참조를 얻어야 메서드 호출 가능

    }
}
```

> 결과

```
MyThread is Thread-0
MyRunnable is Thread-1
MyRunnable is Thread-2
```

#### 쓰레드 이름 지정/변경

쓰레드의 이름은 `Thread(Runnable target, String name)`, `Thread(String name)`, `void setName(String name)`과 같은 생성자나 메서드를 통해 지정하거나 변경할 수 있다.

```java
public class SettingThreadName {
    public static void main(String[] args) {
        NamedThread t1 = new NamedThread();
        Thread t2 = new Thread(new NamedRunnable(), "my first named runnable");

        t1.start();
        t2.start();
    }
}

class NamedThread extends Thread {
    public void run() {
        setName("my first named thread");
        System.out.println("This is " + getName());
    }
}

class NamedRunnable implements Runnable {
    public void run(){
        System.out.println("This is " + Thread.currentThread().getName());
    }
}
```

---

## 쓰레드의 상태

모든 운영시스템은 쓰레드에 대한 관점이 있는데 세부적으로 조금씩 다를 수 있다. 자바는 이런 세부사항을 최대한 추상화시키기 위해 `Thread.State`라고 불리는 enum을 갖고 있다. `Thread.State`의 값은 쓰레드 생애주기의 전체적인 개요를 보여준다. 쓰레드는 특정 순간에 단 하나의 상태만 가질 수 있다.

- `NEW` : 쓰레드가 생성되었지만 `start()` 메서드는 호출하지 않은 상태이다. 모든 쓰레드는 이 상태에서 시작한다.
- `RUNNABLE` : 쓰레드 스케줄링되면 실행될 수 있는 상태이거나 쓰레드가 실행중인 상태이다. JVM에서 실행되는 쓰레드가 이 상태이다.
- `BLOCKED` : 쓰레드가 실행중이 아니고 동가화된 메서드나 block에 들어갈 수 있게 임계영역의 lock을 잡으려고 기다리는 상태이다.
- `WAITING` : 쓰레드가 `Object.wait()` 또는 `Thread.join()` 메서드를 호출해서 다른 쓰레드가 특정 행동을 할때까지 무기한 대기중인 상태이다.
- `TIMED_WAITING` : 쓰레드가 시간값이 있는 `Thread.sleep()`메서드나 `Object.wait()`, `Thread.join()` 메서드를 호출해서 그 시간이 지날 때까지 대기중인 상태이다.
- `TERMINATED` : 쓰레드의 `run()` 메소드가 정상적으로 종료되었거나 예외를 던지면서 모든 동작을 끝낸 상태이다. 

![자바의 쓰레드 라이프사이클](img/week10/thread-lifecycle-java.jpg)

이미지 출처 : https://www.baeldung.com/wp-content/uploads/2018/02/Life_cycle_of_a_Thread_in_Java.jpg

#### `NEW` , `RUNNABLE`

```java
public class NewState {
    public static void main(String[] args) throws InterruptedException {
        Runnable runnable = new NewRunnable();
        Thread t = new Thread(runnable);
        System.out.println(t.getState());   // NEW

        t.start();
        System.out.println(t.getState());   // RUNNABLE
    }
}

class NewRunnable implements Runnable{
    @Override
    public void run() {}
}

```

#### `BLOCKED`

```java
public class BlockedState {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new BlockedRunnable());
        Thread t2 = new Thread(new BlockedRunnable());

        t1.start();
        t2.start();

        Thread.sleep(1000);

        System.out.println(t2.getState());  // BLOCKED
        System.exit(0);
    }
}

class BlockedRunnable implements Runnable {
    @Override
    public void run() {
        commonResource();
    }

    public static synchronized void commonResource() {
        while(true) {
            // t1이 이 메서드를 벗어나지 않았는데 t2가 실행하려고 하는 상황을 만들어 주기 위한 무한루프
        }
    }
}
```

#### `WAITING`

```java
public class WaitingState implements Runnable{
    public static Thread t1;

    public static void main(String[] args) {
        t1 = new Thread(new WaitingState());
        t1.start(); // WAITING
    }

    public void run(){
        Thread t2 = new Thread(new WaitingRunnable());
        t2.start();
        try {
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class WaitingRunnable implements Runnable {
    public void run() {
        System.out.println(WaitingState.t1.getState());
    }
}
```

#### `TIMED_WAITING`

```java
public class TimedWaitingState {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new TimedWaitingRunnable());
        t.start();
        Thread.sleep(1000);
        System.out.println(t.getState()); // TIMED_WAITING
    }
}

class TimedWaitingRunnable implements Runnable{
    @Override
    public void run() {
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

#### `TERMINATED`

```java
public class TerminatedState implements Runnable{
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new TerminatedState());
        t.start();
        Thread.sleep(1000); // 쓰레드 t가 실행되고 끝나는 텀 만들기 위함
        System.out.println(t.getState()); // TERMINATED
    }

    @Override
    public void run() {

    }
}
```

---

## 쓰레드의 우선순위



---

## Main 쓰레드

main 메서드의 작업을 수행하는 쓰레드를 main 쓰레드라고 한다. 프로그램을 실행하면 기본적으로 하나의 쓰레드를 생성하고 그 쓰레드가 main 메서드를 호출해서 작업을 수행하는 것이다.

main 메서드가 수행을 마쳤더라고 다른 쓰레드가 아직 작업을 마치지 않았다면 프로그램이 종료되지 않는다. 즉, 실행중인 사용자 쓰레드가 하나도 없을때만 프로그램이 종료된다. 

---

## 동기화

자바는 쓰레드간에 정보를 전달하기 위한 여러가지 방법을 갖고 있다. 가장 기본적인 방법이 바로 임계영역을 이용해 구현되는 동기화이다. 자바에서 각각의 객체는 쓰레드가 lock하거나 unlock 할 수 있는 임계 영역과 관계되어 있다. 한번에 단 하나의 쓰레드만 임계영역의 lock를 잡을 수 있다. 그 외 다른 쓰레드는 임계영역의 lock을 잡을 수 있을 때까지 block된다. 하나의 쓰레드는 특정 임계영역의 lock을 여러번 잡을 수 있다. 각각의 unlock은 lock 동작 하나의 효과를 반전시킨다.

멀티쓰레드 프로세스에서 여러 쓰레드가 같은 프로세스 내의 자원을 공유해서 작업하기 때문에 서로의 작업에 영향을 주게 되는데 그러다보면 원래의 의도와는 다른 결과를 얻을 수 있다. 이를 방지하기 위해 한 쓰레드가 특정 작업을 끝마칠때까지 다른 쓰레드에 방해받지 않도록 막을 필요가 있는데 이것을 쓰레드의 동기화라고 한다.

### synchronized를 이용한 동기화

#### 특정영역을 임계영역으로 지정

메서드 내의 코드 일부를 블럭으로 감싸고 그 앞에 `synchronized(참조변수)`붙여서 사용할 수 있다. 이때 참조변수는 락을 걸고자 하는 객체를 참조해야 한다. 이 블럭을 synchronized 블럭이라고 하고 이 객채의 블럭이 임계영역이 된다. 쓰레드는 임계영역에 대해 lock을 얻고 동기화된 명령문의 바디 부분을 실행한다. 바디 부분의 동작이 정상적이든 예외를 뱉든 완료된다면 해당 임계영역은 자동으로 unlock된다.

#### 메서드를 임계영역으로 지정

메서드 앞에 `synchronized`를 붙여 동기화된 메서드를 만들 수 있고 그렇게 하면 메서드 전체가 임계영역으로 설정된다. 동기화된 메서드가 호출되면 해당 메서드가 포함된 객체의 lock을 얻는다. 만약 동기화된 메서드가 인스턴스 메서드라면 메서드가 호출된 인스턴스가 있는 임계영역을 잠근다. 만약 동기화된 메서드가 static 이라면 그 메서드가 정의된 클래스를 나타내는 클래스 객체의 임계영역을 잠근다. 메서드의 바디 부분이 정상적이든 예외를 뱉든 완료된다면 해당 임계영역은 자동으로 unlock된다.



자바는 deadlock을 감지하는 것을 방지하거나 요구하지 않는다. 만약 필요하다면 여러개의 객체에 대해 (직간접적으로) lock을 잡는 쓰레드가 있는 프로그램에는 deadlock이 생기지 않는 자바 기본타입을 사용하는 등의 방법을 사용해야 한다.

volatile 변수를 읽고 쓰거나 `java.util.concurrent` 패키지의 클래스를 사용하는 등의 다른 방법들로도 동기화를 구현할 수 있다.

---

## 데드락

교착상태(deadlock)란 두 쓰레드가 자원을 점유한 상태에서 서로 상대편이 점유한 자원을 사용하려고 기다리느라 진행이 멈춰 있는 상태를 말한다.

---

## 참고자료

1. 남궁성. *Java의 정석 3판.* 도우출판, 2016.

2. Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.

3. https://docs.oracle.com/javase/specs/jls/se15/html/jls-17.html

4. https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.State.html

5. https://howtodoinjava.com/java/multi-threading/

6. http://www.tcpschool.com/java/java_thread_concept
