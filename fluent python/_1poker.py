import collections
Card=collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spade diamonds clubs hearts'.split()

    def __init__(self):
        self._card=[Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

suit_values = dict(spade=3,hearts=2,diamonds=1,clubs=0)
def spade_card(card):
    rank_value=FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values)+suit_values[card.suit]

deck=FrenchDeck()
for card in sorted(deck,key=spade_card):
    print([card,spade_card(card)])


print(len(deck))
# for x in deck:
#     print(x)
# print(deck[:3])
# print(deck[12::13])


# from random import choice
# print(choice(deck))
# for x in deck:
#     print(x)
# a=type(deck)
# print(a)
