cards_seq = "23456789TJDKA"


def poker(lst):
    retlist = []
    h_list = []
    for i in lst:
        hand = PokerHand(i)
        h_list.append(hand)
    h_list = sorted(h_list, key = lambda h: h.result, reverse=True)
    for i in range(len(h_list)):
        if i == 0:
            retlist.append(h_list[i].cards)
            maxvar = h_list[i].result
        else:
            if h_list[i].result == maxvar:
                retlist.append(h_list[i].cards)
            else:
                break
    return retlist


class PokerHand():
    def __init__(self, cards):
        self.cards = cards
        self.ranks = [0 for i in range(13)]
        self.one_suit = True
        for i in cards:
            idx = cards_seq.find(i[0])
            self.ranks[idx] += 1
            if i[1] != cards[0][1]:
                self.one_suit = False
        # check for sequence 5 card
        card_str = ""
        for i in self.ranks:
            card_str += str(i)
        if card_str.find("11111") != -1:
            self.seq = True
        else:
            self.seq = False

        idx4 = card_str.find("4")
        idx3 = card_str.find("3")
        idx2 = card_str.find("2")
        idx2_2 = card_str.rfind("2")
        idx1 = card_str.find("1")

        # straight flush = 90000 + high card
        if self.one_suit and self.seq:
            self.result = 90000 + card_str.rfind("1")
        # four of kind = 80000 + high card
        elif idx4 != -1:
            self.result = 80000 + idx4
        # full house = 70000 + high triplet * 13 + pair
        elif idx3 != -1 and idx2 != -1:
            self.result = 70000 + idx3 * 13 + idx2
        # flush = 60000 + high card
        elif self.one_suit:
            self.result = 60000 + card_str.rfind("1")
        # Straight = 50000 + high card
        elif self.seq:
            self.result = 50000 + card_str.rfind("1")
        # Three of kind = 40000 + high triplet
        elif idx3 != -1:
            self.result = 40000 + idx3
        # Two pairs = 30000 + high pair * 13 + low pair + alone
        elif idx2 != -1 and idx2_2 != -1 and idx2 != idx2_2:
            self.result = 30000 + idx2_2 * 13 * 13 + idx2 * 13 + idx1
        # One pair = 20000 + pair card
        elif idx2 != -1:
            self.result = 20000 + idx2
        # High card = 10000 + card
        else:
            self.result = 10000 + card_str.rfind("1")
