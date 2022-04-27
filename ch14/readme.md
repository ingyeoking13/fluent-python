# 반복형, 반복자, 제너레이터

> 내 프로그램 안에 패턴이 보이면, 나는 이것을 문제의 징조라고 생각한다. 프로그램의 형태는 해결해야 할 문제만 반영해야 한다. 코드 안에 있는 그 외의 규칙성은 (적어도 나에게는) 너무 강하지 않게 추상화하고 있다는 징조다. 나는 작성해야 하는 매크로 확장의 일부를 수작업으로 하곤 한다. - 폴 그레이엄

데이터셋을 검색할 때는 항목들을 느긋하게 가져와야 한다. 한 번에 하나씩 그리고 필요할 때 가져와야한다. 이것이 반복자 패턴이 하는 일이다. 파이썬은 리스프와 달리 매크로가 없으므로, 반복자 패턴을 추상화할 수 있게 yield 키워드가 2001년 파이썬 2.2에 추가됨. yield 키워드는 반복자로 작동하는 제너레이터를 생성할 수 있게 해준다.  
모든 제너레이터는 반복자다. 제너레이터가 반복자 인터페이스를 완전히 구현하고 있기 때문이다. 반복자는 디자인패턴에서 정의한 대로 컬렉션에서 항목을 가져오지만, 제너레이터는 다음 항목을 생성할 수 있다. 반복자는 제너레이터가 아니다. 그렇기 때문에 피보나치 수열 제너레이터가 예제로 사용될 수 있다. 무한 수열을 컬렉션에 저장할 수 없기 때문이다. 그렇지만 왕왕 반복자와 제너레이터를 거의 동일시 하게 잘 못 사용하고 있다.  
파이썬의 컬렉션은 모두 반복형이며, 반복자 인터페이스를 활용한다.

`sentence.py`를 참조하시오. `Sentence` 클래스는 반복할 수 있다. 인덱스로 값을 가져올 수 있는 시퀀스이기 때문이다. 왜 시퀀스는 반복할 수 있을까?

sequence가 반복가능한 이유는 **iter()** 함수 때문이다. 파이썬 인터프리터가 x 객체를 반복해야 할 때는 언제나 **iter(x)**를 자동으로 호출한다. iter() 내장 함수의 동작 순서는 다음과 같다.

> 1. 객체가 **iter** 메서드를 구현하는지 확인하고, 이 메서드를 호출하여 반복자를 가져온다.
> 2. **iter** 메서드가 구현되어 있지 않지만 **getitem** 이 구현되어 있다면, 파이썬은 인덱스 0에서 시작해서 항목을 순서대로 가져오는 반복자를 생성한다.
> 3. 이 과정이 모두 실패하면 파이썬은 `TypeError: 'C' object is not iterable`이라는 메시지와 함께 TypeError가 발생한다. 여기서 C는 대상 객체의 클래스이다.

그렇기 때문에 모든 파이썬 시퀀스는 반복할 수 있다. 시퀀스가 **getitem**을 구현하고 있기 때문이다. 사실 표준 시퀀스는 **iter** 메서드도 구현하고 있으므로 여러분이 정의한 시퀀스도 언젠가는 지원 종료할 수 있는 **getitem** 대신 **iter**를 구현하여야 한다. 파이썬은 어떻게든 지원하려고 하는 적극적인 부분이 있어서, 정의에 있어 모호할 수 있어 앞으로는 **iter** 특별 메서드를 구현하는 객체만 반복형이라 간주하자. `abc.Iterable.py`를 참조하자. **iter** 특별 메서드를 구현한 `Foo` 클래스는 issubclass-abc.Iterable 테스트를 통과한다. 반면 앞서 만든 `sentence` 클래스는 통과하지 못 한다.

> 반복형 : iter() 내장 함수가 반복자를 가져올 수 있는 모든 객체. 또는 반복자를 반환하는 **iter** 특별 메서드를 구현한 객체.

`next.py`를 참조하자. **next()**는 다음에 사용할 항목을 반환한다. 더 이상 항목이 남아 있지 않으면 StopIteration을 발생시킨다.