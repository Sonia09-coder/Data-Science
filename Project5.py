# Blind auction program:--
from art_auditlogo import logo
print(logo)

bids={}
biding_finished=False

def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not biding_finished:
    name=input("What is your name? \n")
    price=int(input("What is your bid? $"))
    bids[name]=price
    should_continue=input("Are there are any biders? Type yes or no: ")
    if should_continue=="no":
        biding_finished=True
        highest_bidder(bids)
    