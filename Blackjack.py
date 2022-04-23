import random
import time

def dealing(list1, list2):

    for i in range(2):
        list1.append(random.choice(list(cards)))
        list2.append(random.choice(list(cards)))


def hit(handlist):
    while input(f"would you like another card?('y' or 'n')\n").lower() == "y":
        handlist.append(random.choice(list(cards)))
        if total(handlist) > 21 and handlist.count("A")<2:
            print(f"{handlist} \n You've lost, your total is {total(handlist)}")
            break
        elif total(handlist) > 21 and handlist.count("A")>1:
            cards["A"]=1
            print(f"{handlist} \n your new is total {total(handlist)}")

        else:
            print(f"{handlist} \n your new is total {total(handlist)}")


def dealer(handlist, handlist2):
    if total(handlist2)>21:
        return
    print(f"dealers turn \n {handlist}")
    time.sleep(1)
    if total(handlist) >= 17:
        if total(handlist) > total(handlist2):
            print(f"You've lost, dealer got {total(handlist)} while you've got {total(handlist2)}")
            return
        else:
            print(f"You've won, dealer got {total(handlist)} while you've got {total(handlist2)}")
            return
    while (total(handlist) < 17):
        if handlist.count("A")>1:
            cards["A"]=1
        handlist.append(random.choice(list(cards)))
        print(handlist)
        time.sleep(1)
    if total(handlist) >21 :
        print(f"You've won, dealer got {total(handlist)} and bust!")
    elif total(handlist) < total(handlist2):
        print(f"You've won, dealer got {total(handlist)} while you've got {total(handlist2)} total.")
    else:
        print(f"You've lost, dealer got {total(handlist)} while you've got {total(handlist2)} total.")



def total(handlist):
    suma = 0
    for i in handlist:
        suma += cards[i]
    return suma


cards = {
    "A": 11,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
Game = True
hand1 = []
hand2 = []


while Game:
    if input("would you like to play blackjack? ('y' or 'n')\n") == 'n':
        break
    hand1 = []
    hand2 = []
    dealing(hand1, hand2)
    print(f"Your hand is {hand1[0]} and {hand1[1]} totaling {total(hand1)}")
    print(f"Dealer's first card is {hand2[0]}")
    if total(hand1) == 21:
        time.sleep(1)
        dealer(hand2, hand1)
    else:
        hit(hand1)
        dealer(hand2, hand1)