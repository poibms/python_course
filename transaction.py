from collections import OrderedDict

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount


    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recioient', self.recipient), ('amount', self.amount )])