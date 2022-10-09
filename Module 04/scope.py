balance = 580


def total_cost(price, quantity):
    global balance
    cost = price * quantity
    # remaining = balance - cost
    # balance = remaining
    # print(remaining)
    balance = cost
    return cost


pay = total_cost(10, 3)
print(f"Please Pay {pay}")
print(balance)
