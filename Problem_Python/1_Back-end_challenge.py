'''
         Imagine you are building a backend for an ecommerce website.
         One of the functions in your backend in resposible for updating
         the shopping cart based on user actions.
         Users can add items from the cart, or change the quantity of the
         items they've added.

         You are provided a function names 'update_shopping_cart' which accepts
         two arguments:
         (1) cart: A dictionary where the keys are product IDs (string) and
         the values are the number of that product currently in the cart(integer).

         (2) action: A dictionary representing the user's action.
          It has two keys:
           -- type: A string that can be either 'add', 'remove', or 'change'.
           -- product_id: The product ID the action is referring to.
           -- quantity: (only when the type is 'add' or 'change') the quantity
            to add or the new quantity to set.


        Your task is to modify the update_shopping_cart function to handle
        the user action and return the updated cart correctly.
        The current implementation has several logical errors which you need to correct.

        Example input:
        cart={
            'product_1': 2,
            'product_2': 1
        }

        action = {
            'type': 'add',
            'product_id': 'product_3',
            'quantity': 3
        }


        Example output:

        {
            'product_1': 2,
            'product_2': 1,
            'Product_3', 3
        }

'''

def update_shopping_cart(cart, action):
    product_id = action.get('product_id')
    act_type = action['type']
    act_num = action['quantity']

    if act_type == 'add':
        if product_id not in cart.keys():
            cart[product_id] = act_num
        else:
            cart[product_id] += act_num
    elif act_type == 'remove':
        if product_id in cart.keys():
            cart.pop(product_id)
    elif act_type == 'change':
        if product_id in cart.keys():
            cart[product_id] = act_num

    return cart



cart1 = {
        'product_1': 2,
        'product_2': 1
        }

action1 = {
        'type': 'add',
        'product_id': 'product_3',
        'quantity': 3
        }

action1 = {
        'type': 'change',
        'product_id': 'product_1',
        'quantity': 100
        }


action1 = {
        'type': 'remove',
        'product_id': 'product_1',
        'quantity': 100
        }

print(update_shopping_cart(cart1, action1))














