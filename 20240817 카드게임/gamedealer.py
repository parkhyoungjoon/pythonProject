from card import Card
import random
class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = [Card(suit,number) for suit in card_suits for number in card_numbers]
        random.shuffle(self.deck)

    def give_card(self, card_num):
        return [self.deck.pop(random.randint(0,len(self.deck))-1) for _ in range(card_num)]
    
    def dealer_view(self, card_num):
        i = 0
        print('='*60)
        print(f'카드 나누어 주기: {card_num}장')
        print('-'*60)
        print('[GameDealer] 딜러가 가진 카드 수:',len(self.deck))
        for card in self.deck:
            print(card,end=' ')
            i+=1
            if not i % 13:print()
        print('')