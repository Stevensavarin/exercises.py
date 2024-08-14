""" Currency Exchange"""
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    
    return budget / exchange_rate

result = exchange_money(127.5, 1.2)
print(result)

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value
    
result = get_change(127.5, 120)
print(result)


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills
    
result = get_value_of_bills(128, 5)
print(result)


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination
    
result = get_number_of_bills(127.5, 5)
print(result)
    


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination
    
result = get_number_of_bills(127.5, 20)
print(result)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    extra_fee = exchange_rate * (spread/100) # 1.20 * (10 / 100 ) = 0.12
    total_fee = exchange_rate + extra_fee # 1.20 + 0.12 = 1.32
    exchange_fee = budget/total_fee # 127.25 / 1.32 = 96.40151515151514
    number = exchange_fee//denomination # 96.40151515151514 // 5 = 19.0
    return number * denomination # 19 * 5 = 95
    