## 프로그래밍 면접 이렇게 준비한다

### :one::zero: 장 동시성

<br>

:white_check_mark: 스레드

```
스레드는 애플리케이션의 실행에 있어서 가장 기본적인 단위이다. 기본적으로 스레드끼리는 파일 핸들이나 메모리 같은 자원을
공유한다. 따라서 공유 자원에 대한 접근을 제대로 제어하지 못하면 문제가 생긴다.
```

:white_check_mark: 뮤텍스

```
일종의 Locking 매커니즘이다. lock을 가지고 있을 경우에만 공유 데이터에 접근 가능하다. 일부 음식점들은 공용 화장실 
관리 차원에서 화장실을 잠궈두고(Locking) 다닌다.  손님들이 화장실에 가려면 주인에게 열쇠를 받은 후 가야한다.
물론 다음 손님이 화장실에 가려면 앞 손님이 열쇠를 반납해야 갈 수 있다. 
이렇게 열쇠가 있는-lock을 가지고 있는 경우-에만 공유자원(화장실)에 접근할 수 있다. 이게 바로 Mutex라고 보면 된다. 
유의할 점은 Lock에 대한 소유권이 있다는 점이다. 열쇠를 획득한 사람만 반납할 수 있다.
```

:white_check_mark: 세마포어
```
세마포어는 동시에 리소스에 접근할 수 있는 '허용 가능한 Counter의 갯수'를 가지고 있는 Counter로 보면 된다. 
예를 들면 107호 병실에 방문객용 의자가 5개 있다고 치자. 간호사는 이 병실에 방문자가 5명만 들어갈 수 있도록 허용하고 
나머지 방문객들은 밖에서 대기하도록 한다. Counter 갯수만큼 공유자원(병실)에 접근할 수 있다. 
이 세마포어 Counter의 갯수에 따라 1개의 경우 Binary Semaphore, 2개 이상의 경우 Counting Semaphore라고 불린다. 
Binary Semaphore의 경우 개념적으로 Mutex와 같다고 볼 수 있다.
```

:white_check_mark: 모니터
```
Mutex(Lock)와 Condition Variables(Queue라고도 함)을 가지고 있는 Synchronization 메카니즘이다. 
예를 들어 자바에서 모든 객체는 Object 클래스를 상속 받는다. 이 Object 클래스에는 wait(), notifyAll(), notify()
메소드를 가지고 있는데  이게 바로 Condition Variables 역할이라고 보면 된다. 고로 모든 자바 객체는 Monitor를 가지고 있다. 
자바에서는 Mutual Exclusion 해결을 위한 구현체로 Synchronized 키워드가 있다. 
예를 들어 Synchronized가 메소드에 선언되어있고, 쓰레드A가 이미 Lock을 획득해서 Critical Section(메소드)을 수행중이라고 가정하자.
쓰레드B가 동일한 메소드를 수행하기 위해 해당 Object의Lock을 획득해야 할 것이다. 
이 Lock이 반환될 때까지 대기를 해야하는데 그 때 사용되는게 바로 Monitor다. 쓰레드A가 Lock을 반환하면 쓰레드B는 기다렸다가 Lock을 획득하게 된다. 
그리고 Critical Section인 메소드를 수행할 수 있게 된다. 물론 Synchronized 키워드를 사용했을 때 자동적으로 수행되는 내부 동작이고, 
별도로 명시적인 Monitor를 구현할 수도 있다.아무튼 Monitor는 이렇게 Mutex(Lock)과 Condition Variables을 이용해서 
Mutual Exclustion을 해결하고 있다. 그 외 Monitor의 다른 정의로는 공유자원에 안전하게 접근하기 위해 
Mutual Exclusion가 랩핑된 Thread-Safe한 클래스, 객체, 모듈들을 의미하기도 한다.
```

:white_check_mark: 컨디션 변수
```
Condition Variable은 특정 조건을 만족하기를 기다리는 변수라는 의미이다.
따라서 이를 이용하여 주로 thread간의 신호 전달을 위해 사용한다.
하나의 thread가 waiting 중이면 조건을 만족한 thread에서 변수를 바꾸고 signaling을 통해 깨우는 방식이다.
```

:white_check_mark: 모니터와 세마포어와 뮤텍스
```
1. 뮤텍스와 세마포어의 차이점 
뮤텍스는 공유자원을 접근할 수 있는 키가 하나인 세마포어랑 같다. 키가 하냐 쓸수 있냐? 여러개 쓸수 있냐의 차이다.

2.세마포어와 모니터의 차이
세마포어에 비해서 모니터 쪽이 공유자원에 접근할 수 있는 키의 획득과 해제를 모두 처리해서 간단하다. 세마포어는 직접 키해제와 공유자원 접근 처리를 해주어야한다.
```

:white_check_mark: 데드락
```
두 스레드가 서로 상대방이 쥐고 있는 자물쇠가 풀리기만을 기다리면서 서로 가로막고 있는 상황. 
두 개의 서로 다른 스레드에서 서로 상대방이 필요로 하는 자원에 대한 락을 가지고 있는 경우에 일어난다. 
이 경우 꼼짝할 수 없는 상태가 되기 때문에 데드락이라는 이름이 붙었다.
```

:white_check_mark: 스레딩 구문 in Java
```java
void someMethod(){
  synchronized(this){
    //보호해야 할 코드
  }
}
```

출처: https://about-myeong.tistory.com/34 [명찌의 포스트잇]





