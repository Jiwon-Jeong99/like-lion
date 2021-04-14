import random
from random import sample

LOTTO = 1000
WIN_1ST = 5000000
WIN_2ND = 100000
WIN_3RD = 20000
WIN_4ST = 5000


def input_howmuch_lotto(): 
    input_word = input("구입금액을 입력해 주세요 : ")
    return input_word


def check_input_howmuch_word(): #문자열 입력시, 0 입력시 
    while True:
        input_word = input_howmuch_lotto()
        if input_word.isalpha() == 1:
            break
        print("숫자를 입력해주세요.")
    
        elif input_word == 0:
            break
        print("로또의 최소 가격은 1000원입니다.")
    return input_word
   

def buy_number_lotto(): #가격만큼 로또 구입
    number_lotto = get_check_input_howmuch_word() // 1000 #입력한 가격에서 1000나누면 나오는 장수 
    print(number_lotto, "장의 로또를 구입하셨습니다.")


def generate_random_numbers(): #로또 산 만큼 랜덤 리스트 반환
    for i in number_lotto:
        i += 1
        print(random.sample(range(1,46),6))


def 











