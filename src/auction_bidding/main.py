def get_bidder(input: str):

    input_list = input.split(",")

    current_price = int(input_list[0])
    highest_bid = current_price
    highest_bidder = None

    for i in range(1, len(input_list), 2):
        bid = int(input_list[i + 1])

        if bid > highest_bid:
            current_price = highest_bid + 1
            highest_bid = bid
            highest_bidder = input_list[i]

        if highest_bidder is None:
            current_price = bid
            highest_bidder = input_list[i]

        elif bid > current_price:
            if bid == highest_bid:
                current_price = bid
            else:
                current_price = bid + 1

    return highest_bidder, current_price


if __name__ == "__main__":

    inputs = [
        "1,A,5,B,10,A,8,A,17,B,17",
        "1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,thebenil,57,fliegimandi,59,ev,61,philipp,64,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135",
        "1,cable,5,ente,10,karl,19,moehe,14,moehe,23,michbex,24,melloy,25,achi,26",
        "1,cable,5,ente,10,karl,19,moehe,23,michbex,24,melloy,29,achi,26",
        "15,urtyp,17,neuli,16,schlurchi,25,tokay,75,horni,35,sue,60,sue,70",
        "15,urtyp,15",
    ]

    for input in inputs:
        bidder, bid = get_bidder(input)
        print(f"{bidder},{bid}")
