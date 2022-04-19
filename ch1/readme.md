# python data model

> 언어 설계 미학에 대한 귀도의 감각은 놀라울 정도다. 아무도 사용하지 않을 이론적으로 아름다운 언어를 설계할 능력이 있는 훌륭한 언어 설계자를 많이 만났지만, 귀도는 이론적으로는 약간 덜 아름답지만 그렇기 때문에 프로그래밍하기 즐거운 언어를 설계할 수 있는 유례없는 능력자 중 한 사람이다. - Jim Hugunin (Jython, AspectJ, .NET DLR Architecture)

card.py

```py
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')

>> beer_card
Card(rank='7', suit='diamonds')
# [name]([key=value], [key=value])
```

이중 반복문

```py
def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
```

dunderbar(double underbar)

```py
def __len__(self):
    return len(self._cards)


def __getitem__(self, position):
    return self._cards[position]

>>> C = FrenchDeck()
>>> len(C)
>>> C[0]...C[51]
>>> C[::3] # slicing...1
[Card(rank='2', suit='spades'), Card(rank='5', suit='spades'), Card(rank='8', suit='spades'), Card(rank='J', suit='spades'), Card(rank='A', suit='spades'), Card(rank='4', suit='diamonds'), Card(rank='7', suit='diamonds'), Card(rank='10', suit='diamonds'), Card(rank='K', suit='diamonds'), Card(rank='3', suit='clubs'), Card(rank='6', suit='clubs'), Card(rank='9', suit='clubs'), Card(rank='Q', suit='clubs'), Card(rank='2', suit='hearts'), Card(rank='5', suit='hearts'), Card(rank='8', suit='hearts'), Card(rank='J', suit='hearts'), Card(rank='A', suit='hearts')]
>>> C[:3] # slicing...2
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
>>> for card in C: # itrator
...   print(card)
>>> Card('Q', 'hearts') in C # contains
True
>>> Card('F', 'beats') in C # !contains
False
```
