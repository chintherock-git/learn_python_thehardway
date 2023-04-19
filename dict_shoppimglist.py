if __name__=="__main__":
    supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}            
              }
    customers = ["Frank", "Mary", "Paul"]
    shopping_lists = { 
   "Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
   "Mary":  [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), 
             ('bananas', 4), ('oranges', 1), ('cherries', 4)],
   "Paul":  [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), 
             ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies', 4)]}
    
    cart={}
    for customer in customers:
        cart[customer]=[]
        for article,qty in shopping_lists[customer]:
            if article in supermarket:
                if supermarket[article]["quantity"]<qty:
                    qty=supermarket[article]["quantity"]
                if qty:
                    supermarket[article]["quantity"]-=qty
                    cart[customer].append((article,qty))
    for customer,shopping in cart.items():
     print(f"{customer} has shopping cart as {shopping}")
        
    for customer in customers: 
        total_cart_receipt=0
        for article,qty in cart[customer]:
            total_cart_receipt=total_cart_receipt+qty*supermarket[article]["price"]
        print(f"{customer} has total cart cost as {total_cart_receipt}")
                    
                    
         