'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_TOTAL = 1e6
def validorder(order: Order):
    payment_total = Decimal(0)
    product_total = Decimal(0)
    for item in order.items:
        if item.type == 'payment':
            if type(item.amount) == int or type(item.amount) == float:
                payment_total += Decimal(str(item.amount))
        elif item.type == 'product':
            if (type(item.amount) == int or type(item.amount) == float) and  \
            (type(item.quantity) == int and item.quantity >= 1):
                product_total += Decimal(str(item.amount)) * Decimal(item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if payment_total > MAX_TOTAL or product_total > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if payment_total != product_total:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment_total - product_total)
    else:
        return "Order ID: %s - Full payment received!" % order.id