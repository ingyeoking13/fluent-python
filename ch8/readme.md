# 객체 참조, 가변성, 재활용

- 객체의 정체성

```py
charles = { 'name' : 'charles', 'born': 1832 }
lewis = charles
print( lewis == charles )
print( lewis is charles )
darwin = { 'name' : 'charles', 'born': 1832 }
print( darwin == charles )
print( darwin is not charles )
```

== 연산자는 객체의 값을 비교. is 는 객체의 정체성 비교.

- tuple은 내부 객체의 값은 변경될 수 있다. 정체성(id)는 유지한다.

```py
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print (t1 == t2)
print (id(t1[-1]))
t1[-1].append(99)
print (t1)
print (id(t1[-1]))
print (t1 == t2)
```
