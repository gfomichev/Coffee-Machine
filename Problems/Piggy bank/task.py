class PiggyBank:
    def __init__(self, deposit_dollars, deposit_cents):
        self.dollars = deposit_dollars
        self.cents = deposit_cents

    def add_money(self, _dollars, _cents):
        new_cents = self.cents + _cents
        self.dollars += _dollars + new_cents // 100
        self.cents = new_cents % 100
