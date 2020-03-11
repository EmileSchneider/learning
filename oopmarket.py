class Buyer:
    def __init__(self,i):
        self.id=i
        self.maxBuyPrice = 150
        self['currentOffer'] = 50
        self['items'] = []

    def makeOffer(self, sellPrice):
        if sellPrice > self['currentOffer']:
            self.updateOffer(False)
            return False
        else:
            self.updateOffer(True)
            return True

    def updateOffer(self, accepted):
        if accepted:
            self['currentOffer'] = self['currentOffer'] - 10
        else:
            if self.maxBuyPrice > self['currentOffer']:
                self['currentOffer'] = self['currentOffer'] + 10


class Item:
    pass


class Seller:
    def __init__(self,i):
        self.id=i
        self.minSellPrice = 70
        self['currentOffer'] = 120
        self['items'] = [Item(), Item(), Item(), Item()]

    def talkWithCustomer(self, potentialBuyer):
        if len(self['items']) > 0:
            if potentialBuyer.makeOffer(self['currentOffer']):
                potentialBuyer['items'].append(self.items.pop())

    def updateOffer(self, accepted):
        if accepted:
            self['currentOffer'] = self['currentOffer'] + 10
        if self.maxBuyPrice > self['currentOffer']:
            self['currentOffer'] = self['currentOffer'] - 10


class Market:
    def __init__(self):
        self.buyers = [Buyer(x) for x in range(1,10)]
        self.sellers = [Seller(x) for x in range(1, 10)]

    def trade(self):
        for b in self.buyers:
            self.dump()
            for s in self.sellers:
                s.talkWithCustomer(b)

    def dump(self):
        co = [b['currentOffer'] for b in self.buyers]
        sco = [s['currentOffer'] for s in self.sellers]
        print("==")
        print(co)
        print("--")
        print(sco)

m = Market()

for i in range(1,10):
    m.trade()