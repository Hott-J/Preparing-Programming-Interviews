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
