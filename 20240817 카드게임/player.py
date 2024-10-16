from card import Card
class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()
    def add_card_list(self, card_list):
        for card in card_list:
            self.holding_card_list.append(card)

    def display_two_card_lists(self):
        print('='*60)
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        print(*self.open_card_list)
        print('')
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        print(*self.holding_card_list)
        print('')
    def check_one_pair_card(self):
        card_all_count = len(self.holding_card_list)-1
        card_count = 0
        while True:
            front_count = card_count + 1
            while True:
                if self.holding_card_list[card_count].number == self.holding_card_list[front_count].number :
                    self.open_card_list.append(self.holding_card_list.pop(card_count))
                    self.open_card_list.append(self.holding_card_list.pop(front_count-1))
                    card_all_count -= 2
                front_count +=1
                if front_count > card_all_count : break
            card_count+=1
            if card_count >= card_all_count : break

        print('='*60)
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')