'''
    Problem Statement: My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

    I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

    Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

    To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

    The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
    The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
    Each customer order (from either register) as it was finished by the kitchen. (served_orders)
'''


# in this code we take a time Complexity of O(1)  but Space complexity of O(n) because we use recursive function

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders)-> bool:
    # chech whether the served orders is empty if it is return true else contiue
    if len(served_orders) == 0:
        return True
    
    # if the first order in served_order is same as the first order in take_out_orders
    # make sure the take_out _orders is not empty
    if len(take_out_orders) and served_orders[0] == take_out_orders[0]:
        # take the first order off take_out-order and served_order and recurse
        return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])

    # if the first order in served_order is same as the first order in dine_in_orders 
    # make sure the dine-in-orders is not empty
    elif len(dine_in_orders) and served_orders[0] == dine_in_orders[0]:
        # take the first order off dine-in-order and served_orders and recurse
        return is_first_come_first_served(take_out_orders, dine_in_orders[1:],served_orders[1:])
    # if first order in served order doesn't match the first in takeout and dine in orders hten we know it is not first come first serve
    else:
        return False

take_out = [1, 3, 5]
dine_inn = [2, 4, 6]
served_order =  [1, 2, 4, 6, 3, 5]
print(is_first_come_first_served(take_out, dine_inn, served_order))

