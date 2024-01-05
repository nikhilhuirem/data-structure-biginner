'''
    Problem Statement: My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

    I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

    Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

    To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

    The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
    The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
    Each customer order (from either register) as it was finished by the kitchen. (served_orders)
'''

def FIFO(t,d,s):
    k=[]     
    k1=[]     
    for i in range(len(t)):         
        k.append(s.index(t[i]))     
        for j in range(len(d)):         
            k1.append(s.index(d[i]))     
            if sorted(k)==k and sorted(k1)==k1:         
                return True     
            return False  #main  print(FIFO([1,3,5],[2,4,6],[1,2,4,6,5,3])) print(FIFO([17,8,24],[12,19,2],[17,8,12,19,24,2])) 
print(FIFO([1,3,5],[2,4,6],[1,2,4,6,5,3]))