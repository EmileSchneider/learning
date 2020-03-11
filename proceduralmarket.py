def makebuyer(baseoffer, mp):
    return {"currentOffer": baseoffer, "maxPrice": mp, "items": []}


def makeseller(baseoffer, mp):
    return {"currentOffer": baseoffer, "minPrice": mp, "items": [i for i in range(0, 4)]}


def trade(buyer, seller):
    if buyer['currentOffer'] > seller['currentOffer']:
        buyer['items'].append(seller['items'].pop())
        didbuy(buyer)
        didsell(seller)
    else:
        didnotbuy(buyer)
        didnotsell(seller)


def didnotsell(seller):
    if seller['currentOffer'] > seller['minPrice']:
        seller['currentOffer'] = seller['currentOffer'] - 10


def didsell(seller):
    seller['currentOffer'] = seller['currentOffer'] + 10


def didnotbuy(buyer):
    if buyer['currentOffer'] < buyer['maxPrice']:
        buyer['currentOffer'] = buyer['currentOffer'] + 10


def didbuy(buyer):
    buyer['currentOffer'] = buyer['currentOffer'] - 10


buyers = [makebuyer(i*10, 180) for i in range(1, 20)]
sellers = [makeseller(i*15, 50) for i in range(1, 15)]

soldout = []
print(buyers)
print(sellers)
print(soldout)
for b in buyers:
    for s in sellers:
        trade(b,s)
        if len(b['items']) == 0:
            soldout.append(buyers.pop(buyers.index(b)))

print(buyers)
print(sellers)
print(soldout)