s = "1,A,5,B,10,A,8,A,17,B,17"
args = s.split(",")

price = args[0]
max_bid = None
max_bidder = None
for i in range(1, len(args), 2):
    bidder = args[i]
    bid = int(args[i+1])

    if max_bid is None:
        max_bid = bid
        max_bidder = bidder
    elif bid > max_bid:
        price = max_bid + 1
        max_bid = bid
        max_bidder = bidder
    elif bid == max_bid:
        price = bid
    else:
        price = bid + 1

    print(max_bidder, price, max_bid)
