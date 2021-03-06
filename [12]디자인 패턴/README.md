## 프로그래밍 면접 이렇게 준비한다

### :one::two: 장 디자인 패턴

<br>
:white_check_mark: static 변수와 메소드<br>

#### static 변수 <br>
- 메모리에 고정적으로 할당되어, 프로그램이 종료될 때 해제되는 변수
```java
public class Person {
    private String name = "MangKyu";
	    
	public void printName() {
	    System.out.println(this.name);
	}
}
```
위와 같은 클래스를 통해 100명의 Person 객체를 생성하면, "MangKyu"라는 같은 값을 갖는 메모리가 100개나 중복해서 생성되게 된다. 이러한 경우에 static을 사용하여 여러 객체가 하나의 메모리를 참조하도록 하면 메모리 효율이 더욱 높아질 것이다. 또한 "MangKyu"라는 이름은 결코 변하지 않는 값이므로 final 키워드를 붙여주며, 일반적으로 Static은 상수의 값을 갖는 경우가 많으므로 public으로 선언을 하여 사용한다. 이러한 이유로, 일반적으로 static 변수는 public 및 final과 함께 사용되어 public static final로 활용 된다.
```java
public class Person {
    public static final String name = "MangKyu";
         
    public static void printName() {
        System.out.println(this.name);
    }
}
```

#### static 메소드 <br>
```java
public class Test {
    private String name1 = "MangKyu";
    private static String name2 = "MangKyu";
 
    public static void printMax(int x, int y) {
        System.out.println(Math.max(x, y));
    }
         
    public static void printName(){
       // System.out.println(name1); 불가능한 호출
       System.out.println(name2);
    }
}
```
우리는 두 수의 최대값을 구하는 경우에 Math클래스를 사용하는데, static 메소드로 선언된 max 함수를 초기화 없이 사용한다. 하지만 static 메소드에서는 static이 선언되지 않은 변수에 접근이 불가능한데, 메모리 할당과 연관지어 생각해보면 당연하다. 우리가 Test.printName() 을 사용하려고 하는데, name1은 new 연산을 통해 객체가 생성된 후에 메모리가 할당된다. 하지만 static 메소드는 객체의 생성 없이 접근하는 함수이므로, 할당되지 않은 메모리 영역에 접근을 하므로 문제가 발생하게 된다. 그러므로 static 메소드에서 접근하기 위한 변수는 반드시 static 변수로 선언되어야 한다.


:white_check_mark: 디자인 패턴이란 무엇인가?

객체지향 프로그래밍에서 공통적인 디자인 문제를 찾아내고 해결하는 가이드라인을 디자인 패턴이라고 부른다. 실제 코드를 제공하는 건 아니고 특정 유형의 프로그래밍 문제를 해결하느 방식 제공

:white_check_mark: 디자인 패턴을 쓰는 이유

- 공통적인 소프트웨어 디자인 문제를 해결하는 데 도움이 될 수 있게 만들어놓은 것이기 때문이다.
- 디자인 문제와 그 해결책을 논할 때 디자인 패턴이 간결한 용어모음을 제공한다.

:white_check_mark: 일반적인 디자인 패턴

#### 싱글톤
애플리케이션이 시작될 때, 어떤 클래스가 최초 한 번만 메모리를 할당(static)하고 해당 메모리에 인스턴스를 만들어 사용하는 패턴
생성자가 여러번 호출되도, 실제로 생성되는 객체는 하나이며 최초로 생성된 이후에 호출된 생성자는 이미 생성한 객체를 반환시키도록 만드는 것이다
(java에서는 생성자를 private으로 선언해 다른 곳에서 생성하지 못하도록 만들고, getInstance() 메소드를 통해 받아서 사용하도록 구현한다)
- 사용 이유 <br>
먼저, 객체를 생성할 때마다 메모리 영역을 할당받아야 한다. 하지만 한번의 new를 통해 객체를 생성한다면 메모리 낭비를 방지할 수 있다.
또한 싱글톤으로 구현한 인스턴스는 '전역'이므로, 다른 클래스의 인스턴스들이 데이터를 공유하는 것이 가능한 장점이 있다.

- 싱글톤이 정적 메서드보다 나은 이유?
```
1. 싱글톤은 객체다. 베이스 클래스로부터 상속을 받고 인터페이스를 구현 가능
2. 다수 객체로 전환 가능
3. 동적 바인딩. 싱글톤을 생성하기 위해 실제로 사용하는 클래스를 컴파일할 때가 아닌 실행할 때 결정할 수 있다.
```
- 단점 <br>
객체 지향 설계 원칙 중에 개방-폐쇄 원칙이란 것이 존재한다.
만약 싱글톤 인스턴스가 혼자 너무 많은 일을 하거나, 많은 데이터를 공유시키면 다른 클래스들 간의 결합도가 높아지게 되는데, 이때 개방-폐쇄 원칙이 위배된다.
결합도가 높아지게 되면, 유지보수가 힘들고 테스트도 원활하게 진행할 수 없는 문제점이 발생한다.
또한, 멀티 스레드 환경에서 동기화 처리를 하지 않았을 때, 인스턴스가 2개가 생성되는 문제도 발생할 수 있다.
어플리케이션이 끝날 때까지 파괴되지 않기 때문에 자원을 필요한 것보다 오래 점유하고 있을 수도 있다.
따라서, 반드시 싱글톤이 필요한 상황이 아니면 지양하는 것이 좋다고 한다. (설계 자체에서 싱글톤 활용을 원활하게 할 자신이 있으면 괜찮음)

#### 빌더
객체가 어떤 식으로 구축되는지에 대해 모르는 상황에서 단계별로 객체를 생성하는 패턴. 객체를 직접 생성하는 대신 빌더의 인스턴스를 만들고 빌더에서 객체를 대신 만들도록 하는 방식이다.
```
객체를 초기화하는 데 여러 생성자 매개변수가 필요한 경우 유용하다.
```

```java
Window w=new Window(false,true,true);//매개변수가 헷갈린다.
```
```java
Window w=new WindowBuilder().setVisible(false).setModal(true).setDialog(true).build();
//와 같이 빌더인스턴스를 써서 새 객체의 초기 상태를 정의하는 식이다.
```

#### 팩토리 메서드
객체를 만드는 부분을 서브클래스에 맡기는 패턴

#### 추상 팩토리
팩토리의 구현과 그 팩토리를 사용하는 코드를 갈라주는 패턴. 보통 어떤 추상 클래스로부터 상속된 일련의 팩토리 클래스로 구현된다. 구현된 여러 팩토리 중에서 어떤 것을 사용할지 결정하고 나면 애플리케이션에서는 실제 클래스가 아닌 추상 클래스를 통해서만 그 팩토리를 참조.

#### 반복자
반복자 패턴을 쓰면 어떤 자료구조에 있는 모든 원소를 종주할 수 있으며, 이 때 각 원소가 어떤 식으로 저장되고 표현되는지에 대해서는 특별히 신경 쓰지 않아도 되고 아예 몰라도 된다.

#### 옵저버
옵저버 패턴은, 한 객체의 상태가 바뀌면 그 객체에 의존하는 다른 객체들에게 연락이 가고, 자동으로 정보가 갱신되는 1:N 관계(혹은 1대1)를 정의한다.
인터페이스를 통해 연결하여 느슨한 결합성을 유지하며, Publisher와 Observer 인터페이스를 적용한다.
안드로이드 개발시, OnClickListener와 같은 것들이 옵저버 패턴이 적용된 것 (버튼(Publisher)을 클릭했을 때 상태 변화를 옵저버인 OnClickListener로 알려주로독 함)

#### 데코레이터
한 객체를 그 객체와 같은 베이스 클래스로부터 파생된, 그리하여 원래 객체와 같은 메서드를 제공하는 다른 객체로 감싸서 객체의 행동을 바꿔주는 패턴이다.
래퍼 패턴이라고 부르기도 한다.

:white_check_mark: 싱글톤 구현
```
어떤 애플리케이션에서 콘솔에 디버깅 메시지를 출력하기 위한 로거 클래스를 사용한다. 
싱글톤 패턴을 써서 이런 로그 기능을 구현하는 방법을 제시해보라.
```

```java
public class Logger{
	//싱글톤 생성하고 저장
	private static final Logger instance=new Logger();
	//다른 사람은 아무도 이 클래스 생성 못하도록 함
	private Logger(){}
	//싱글톤 인스턴스 리턴
	public static Logger getInstance(){return instance;}
	public void log(String msg){
		System.out.printIn(System.currentTimeMillis()+":"+msg);
	}
}
```
Logger 클래스의 인스턴스가 여러 개 생길 수 있는 경우와 이를 예방(클로닝과 객체 직렬화를 생각해본다.)

```
애플리케이션에서 싱글톤을 쓰는데, 꼭 그게 필요한 것도 아니고 초기화 비용이 너무 많이 든다. 
이런 상황을 개선할 수 있는 방법은?
```
클래스를 불러올 때 싱글톤 인스턴스를  무조건 만들어야 하는 것은 아니다. '게으른 초기화'를 사용한다.

```java
public class Logger{
	private static Logger instance=null; //final 키워드 빠짐
	private Logger(){}
	public static Logger getInstance(){
		if(instance==null){
			instance=new Logger();
		}
		return instance;
	}
}
```

위와 같이 코딩하면, 두 스레드에서 getInstance를 동시에 호출 시, 둘다 instance가 아직 초기화되지 않은 것으로 생각하고 각각 인스턴스를 만들려고 할 것이다. 싱글톤에서는 일어나면 안된다.

```java
public synchronized static Logger getInstance()
	{if(instance==null){
		instance=new Logger();
	}
	return instance;
}
```
위와 같이, 동기화를 해줘야한다. 성능의 저하는 있다.

:white_check_mark: 데코레이터 vs 상속
```
상속 대신 데코레이터 패턴을 써야 하는 이유는 무엇인가?
```
데코레이터는 동적으로 행동을 바꿀 수 있다.

:white_check_mark: 효율적인 옵저버 업데이트
```
옵저버 패턴에서 옵저버를 효율적으로 업데이트하기 위해 어떤 전략을 취해야 할까?
```
가장 흔한 문제가 상태가 너무 자주 바뀔 때 옵저버들을 업데이트하느라 시간을 한참 쓴다.
잠시 업데이트를 멈추고 바꿀 걸 다 바꾼 다음 업데이트를 다시 켜고 모든 옵저버에게 필요한 내용을 한번에 알려준다.
옵저버에서 모델의 어떤 부분이 바뀌었는지 알 수 있어야 한다. 옵저버가 대상에게 무엇이 바뀌었는지 다시 물어보는 것보다는 대상에서 업데이트를 알리면서 그 정보까지 넘겨주면 더 낫다.
