import random as rd
# randomly choose two nums and swap.
def shuffle(cards):
    for i in xrange(len(cards)):
        k = (int)(rd.random() * i)
        tmp = cards[k]
        cards[k] = cards[i]
        cards[i] = k

    print cards

shuffle([1,2,3,4,5,6,7,8,9,10,11])
