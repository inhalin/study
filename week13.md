# [자바 라이브 스터디] 13주차 - I/O

> I/O(Input/Output, 입출력) : 컴퓨터 내부 또는 외부의 장치와 프로그램간의 데이터를 주고받는 것을 말한다.

#### 목표

```
자바의 Input과 Output에 대해 학습하세요.
```

#### 학습할 것

`🟢 completed` `🟡 in progress` `⚪ not done`

- ⚪ 스트림 (Stream) / 버퍼 (Buffer) / 채널 (Channel) 기반의 I/O
- ⚪ InputStream과 OutputStream
- ⚪ Byte와 Character 스트림
- ⚪ 표준 스트림 (System.in, System.out, System.err)
- ⚪ 파일 읽고 쓰기

---

## 자바 표준 I/O vs. New I/O

### Standard I/O

자바 프로그래밍에서 I/O 클래스는 스트림을 사용해 수행되었다. 모든 입출력은 스트림이라는 개채를 통해 한번에 하나씩 단일 바이트의 이동으로 표시된다. 스트림 입출력은 외부세계와의 연결에 사용된다. 내부적으로는 객체를 바이트로 변환하고 그것을 다시 객체로 변환하는 데에 사용되는데 이것을 직렬화와 역직렬화라고 한다.

#### 스트림

자바에서 입출력을 수행할 때 두 대상을 연결하고 데이터를 전달할 수 있게 해주는 통로역할을 하는 것이 스트림이다. 스트림은 한쪽 방향으로만 흐른다. 즉 단방향 통신만 가능하다는 뜻이다. 그래서 입출력을 동시에 처리하려면 입력스트림과 출력 스트림이 각각 필요하다. 

input stream은 소스에서 데이터를 읽을때 사용하고 output stream은 목적지에 데이터를 쓸때 사용한다. 스트림은 프리미티브 값과 오브젝트 등 모든 종류의 데이터를 처리할 수 있다. 

![input stream](img/week13/input-stream.png)

![output stream](img/week13/output-stream.png)

스트림은 한번에 하나의 데이터만 처리할 수 있고 중간에 건너뜀 없이 연속적으로 데이터를 주고받는다. 

데이터의 소스나 목적지는 데이터를 사용하거나 생성하는 어떤 것이라도 될 수 있다. 즉 데이터를 입출력할 소스나 목적지가 디스크 파일 뿐만 아니라 다른 프로그램이나 네트워크 소켓, 또는 배열이 될 수도 있다는 뜻이다.

### New I/O

자바의 NIO는 개인이 커스텀한 네이티브 코드를 작성하지 않고도 고속의 입출력 작업을 구현할 수 있도록 하기 위해 만들어졌다. NIO는 시간에 가장 많이 걸리는 입출력 작업(즉 배퍼를 주입하고 배출하는 작업)을 운영체제 안으로 다시 이동시키기 때문에 속도가 크게 향상된다. 

NIO에서는 클래스가 데이터를 보관하고 그 데이터를 블록 단위로 처리하게 하는 방식을 사용했기 때문에 네이티브 코드 없이도 기존의 `java.io` 패키지에서 할수 없었던 저수준의 최적화를 이용할 수 있는 것이다.

#### 버퍼

버퍼 클래스는 `java.nio`가 만들어지는 데 있어서 가장 중요한 기반이다.

- 버퍼는 고정된 양의 데이터를 위한 컨테이너라고 할 수 있다. 버퍼는 데이터를 저장하고 나중에 찾아올 수 있는 임시 준비 영역 또는 홀딩 탱크의 역할을 한다.
- 버퍼는 채널과 연동된다. 채널은 I/O 전송이 수행되는 실질적인 포털이고 버퍼는 그 데이터 전송의 소스 또는 대상이 된다.
- 외부 전송의 경우 우리가 보내려는 데이터를 버퍼에 위치시키면 버퍼가 아웃 채널에 전달된다.
- 내부 전송의 경우 채널은 우리가 제공하는 버퍼 안에 데이터를 저장한다. 그러면 데이터가 버퍼에서 인 채널로 복사된다.
- NIO API에서 데이터를 효율적으로 처리하는 핵심이 바로 이런 상호협력하는 객체 사이에서의 버퍼의 이동이다.

#### 채널

<!-- 전체적으로 무슨말인지 모르겠다. -->
채널은 `java.nio`에서 버퍼 다음으로 중요하다. 채널은 바이트 버퍼와 반대편 끝의 엔티티(일반적으로 파일이나 소켓) 사이에 데이터를 효율적으로 전송해주는 매체로 I/O 서비스에 직접 연결된다.

일반적으로 채널은 운영체제의 [파일 디스크립터](https://en.wikipedia.org/wiki/File_descriptor)와 일대일 관계를 가진다. 채널 클래스는 플랫폼 독립성을 유지하는 데 필요한 추상화를 제공하면서도 최신 운영 체제의 기본 I/O 기능을 모델링한다.

채널은 운영 체제의 기본 I/O 서비스에 최소한의 오버헤드로 액세스할 수 있는 게이트웨이이며, 버퍼는 채널이 데이터를 송수신하는 데 사용하는 내부 종점이다.

---

## InputStream과 OutputStream

<!-- 시작 -->
바이트단위로 데이터를 전송하는 스트림은 `InputStream`과 `OutputStream`이 있다. 어떤 대상에 대해 입력과 출력 중 어떤 작업을 할 것인지에 따라 해당 스트림을 선택해서 사용하면 된다. 

| 입력스트림 | 출력 스트림 | 입출력 대상 종류 |
|---|---|---|
| FileInputStream | FileOutputStream | 파일 |
| ByteArrayInputStream | ByteArrayOutputStream | 메모리(byte배열) |
| PipedInputStream | PipedOutputStream | 프로세스(프로세스간의 통신) |
| AudioInputStream | AudioOutputStream | 오디오장치 |

---

## Byte와 Character 스트림

<!-- 시작 -->
### Byte Streams

자바는 8-bit 바이트의 입출력을 수행하기 위해 바이트 스트림을 사용한다. 모든 바이트 스트림 클래스는 `InputStream`과 `OutputStream`의 하위 클래스이다. 

#### 바이트 스트림 사용하기

파일 입출력 바이트 스트림인 `FileInputStream`과 `FileOutputStream`을 사용해서 `lorem.txt` 파일을 읽어들여서 파일 내용을 `ipsum.txt`로 복사하는 프로그램을 만들어서 바이트 스트림이 어떻게 동작하는지 살펴보았다. 다른 바이트 스트림도 구성된 방식에서 차이가 있어도 사용되는 방식은 거의 동일하다.

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyBytes {
    public static void main(String[] args) throws IOException {

        FileInputStream in = null;
        FileOutputStream out = null;

        try {
            in = new FileInputStream("lorem.txt");
            out = new FileOutputStream("ipsum.txt");
            int c;

            while ((c = in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
}
```

> 결과

![CopyBytes](img/week13/copybytes.png)

#### 스트림은 항상 닫아준다

더 이상 사용하지 않는 스트림을 닫아주는 것은 굉장히 중요하다. 혹시 에러가 발생하더라도 스트림이 반드시 닫힐 수 있도록 finally block을 사용히면 심각한 리소스 누수를 피할 수 있다.

#### 바이트 스트림을 사용해선 안되는 경우

CopyBytes 프로그램은 일반적으로는 사용해선 안되는 저수준의 I/O를 보여준다. `lorem.txt`는 문자 데이터가 포함되어 있기 때문에 문자 스트림을 사용하는 것이 좋다. 더 복잡한 데이터타입을 위한 스트림도 있다. 바이트 스트림은 가장 원시적인 I/O에만 사용해야 한다.

### Character Streams

#### 문자 스트림 사용하기




---

## 표준 스트림 (System.in, System.out, System.err)

<!-- 시작 -->

---

## 파일 읽고 쓰기

<!-- 시작 -->

---


## 참고자료

1. 남궁성. *Java의 정석 3판.* 도우출판, 2016.

2. Evans, Benjamin J. and David Flanagan. *Java in a Nutshell.* O'Reilly Media, 2019.

3. https://docs.oracle.com/javase/tutorial/essential/io/index.html

5. https://howtodoinjava.com/java-io-tutorial/

6. http://www.tcpschool.com/java/java_thread_concept

7. https://www.baeldung.com/java-daemon-thread
