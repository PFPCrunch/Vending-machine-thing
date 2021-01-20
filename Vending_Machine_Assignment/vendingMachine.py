'''
Objective: Make program that acts like a vending machine; have items that have individual prices,
have user input float representing an amount of money, user buys a thing if they have enough money input,
give change in fewest coins possible, if not enough money input, make fun of user for not having enough theoretical money.
'''

q = float(0.25)
d = float(0.10)
n = float(0.05)
p = float(0.01)
#menu_list = [2.49, 1.99, 1.99, 0.69, 2.99, 3.00, 0]
# coins ^

def displayMenu():
    print('Place Your Order:')
    print('A1: Dorotos $2.49     A2: Conk $1.99             A3: Bepis $1.99')
    print('B1: \"Chips\" $0.69     B2: Mountain Donk $2.99    B3: Hawt Sauce $3.00')
    print('C: no thanks.')
#displayMenu()

def insertCredit():
    print('Insert Credit:')
    credit = float(input())
    print('Remaining Credit: $' + str(credit))
    return credit
#insertCredit()


def placeOrder():
    displayMenu()
    order = input().lower()
    if order == ('a1'):
        print('Enjoy your Dorotos.')
    elif order == ('a2'):
        print('Enjoy your Conk.')
    elif order == ('a3'):
        print('Enjoy your Bepis.')
    elif order == ('b1'):
        print('Enjoy your \"Chips\".')
    elif order == ('b2'):
        print('Enjoy your Mountain Donk.')
    elif order == ('b3'):
        print('Enjoy your Hawt Sauce?')
    elif order == 'c':
        print('Goodbye.')
    else:
        print('That item is not recognized.')

        return order
#placeOrder(insertCredit())

def makeChange(payment, order):
    if order == 'a1':
        price = 2.49
    elif order == 'a2':
        price = 1.99
    elif order == 'a3':
        price = 1.99
    elif order == 'b1':
        price = 0.69
    elif order == 'b2':
        price = 2.99
    elif order == 'b3':
        price = 3.00
    elif payment > 0:

    if payment < price:
        print('You do not have enough credit to purchase this item.')
        remaining_credit = payment - price
        remaining_dollars = int(remaining_credit)
        if remaining_dollars > 0:
            remaining_coins = (round((remaining_credit % remaining_dollars), 2))
        else:
            remaining_coins = remaining_credit
        print('Here is your change: ' + str(remaining_dollars) + ' dollars and ')
        quarters = q / remaining_coins
        while int(quarters) > 0:
            print('q')
            quarters -= 1
            remaining_coins -= q
        dimes = d / remaining_coins
        while int(dimes) > 0:
            print('d')
            dimes -= 1
            remaining_coins -= d
        nickels = n / remaining_coins
        while int(nickels) > 0:
            print('n')
            nickels -= 1
            remaining_coins -= n
        pennies = p / remaining_coins
        while int(pennies) > 0:
            print('p')
            pennies -= 1
            remaining_coins -= p




makeChange(insertCredit(), placeOrder())