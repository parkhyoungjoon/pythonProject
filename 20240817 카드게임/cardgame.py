from card import Card
from player import Player
from gamedealer import GameDealer

def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")
    dealer = GameDealer()
    first_card_count = 10
    idx = 3
    card_count=4
    
    dealer.make_deck()
    player1.add_card_list(dealer.give_card(first_card_count))
    player2.add_card_list(dealer.give_card(first_card_count))
    dealer.dealer_view(first_card_count)
    player1.display_two_card_lists()
    player2.display_two_card_lists()

    input('[2]단계: 다음 단계 실행을 위해 Enter를 누르세요!')
    player1.check_one_pair_card()
    player1.display_two_card_lists()
    player2.check_one_pair_card()
    player2.display_two_card_lists()

    while True:
        input(f'[{idx}]단계: 다음 단계 실행을 위해 Enter를 누르세요!')
        player1.add_card_list(dealer.give_card(card_count))
        player2.add_card_list(dealer.give_card(card_count))
        dealer.dealer_view(card_count)
        player1.check_one_pair_card()
        player1.display_two_card_lists()
        player2.check_one_pair_card()
        player2.display_two_card_lists()
        idx += 1
        if 0 in [len(dealer.deck),len(player1.holding_card_list),len(player2.holding_card_list)] :
            break
        
if __name__ == '__main__':
    play_game()