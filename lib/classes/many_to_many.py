class Coffee:
    def __init__(self, name):
        self.name = name

    @property # GETTER
    def name(self):
        return self._name

    @name.setter # SETTER
    def name(self, new_name):
        if hasattr(self, "_name"):
            print("Cannot change name of Customer")
            # raise Exception("Cannot change name of Customer")
        else:
            # is it a string greater or equal to 3 characters
            if isinstance(new_name, str) and len(new_name) >= 3:
                self._name = new_name    # mocha_latte.average_price()

            else:
                print("Name must be a string at least 3 characters long")
        
    def orders(self):
        return [ order for order in Order.all if order.coffee == self ]
    
    def customers(self):
        return list( set( [ order.customer for order in self.orders() ] ) )
    
    def num_orders(self):
        return len( self.orders() )
    
    # Returns the average price for a coffee based on its orders
    # Returns 0 if the coffee has never been ordered
    # Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders

    def average_price(self):
        # create list of all prices for this coffee
        prices = [ order.price for order in self.orders() ]
        # sum them up
        # divide by number of orders        
        return sum(prices) / self.num_orders()


class Customer:

    all = []

    # Customer is initialized with a name
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)


    # Customer property name
    # Returns customer's name

    @property # GETTER
    def name(self):
        return self._name
    
    # Names must be of type str
    # Names must be between 1 and 15 characters, inclusive
    # Should be able to change after the customer is instantiated

    @name.setter # SETTER
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            print("Name must be a string between 1 and 15 characters long")

    def orders(self):
        return [ order for order in Order.all if order.customer == self ]
    
    def coffees(self):
        return list( set( [ order.coffee for order in Order.all if order.customer == self ] ) )
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def total_spent_on_coffee(self, coffee):
        return sum( [order.price for order in Order.all if order.customer == self and order.coffee == coffee] )
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.customers():
            return None
        else:
            high_total = 0
            big_spender = None

            for customer in Customer.all:
                customer_total = customer.total_spent_on_coffee(coffee)
                if customer_total > high_total:
                    high_total = customer_total
                    big_spender = customer

            return big_spender

    # Receives a coffee object argument
    # Returns the Customer instance that has spent the most money on the coffee instance provided as argument.
    # Returns None if there are no customers for the coffee instance provided.
    # hint: will need a way to remember all Customer objects
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        # type(self).all.append(self)

    # Returns the price for the order

    @property
    def price(self):
        return self._price

    # Prices must be of type float
    # Price must be a number between 1.0 and 10.0, inclusive
    # Should not be able to change after the order is instantiated
    # hint: hasattr()

    @price.setter
    def price(self, new_price):
        if not hasattr(self, "_price"):
            if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
                self._price = new_price
            else:
                print("Price must be a float between 1.0 and 10.0")
        else:
            print("Price cannot be changed")

    # Returns the customer object for that order

    @property
    def customer(self):
        return self._customer
    
    # Must be of type Customer

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            print("Not a customer GET OUT")

    # Returns the coffee object for that order

    @property
    def coffee(self):
        return self._coffee
    
    # Must be of type Coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            print("Not a coffee DONT SERVE IT")

# my_new_customer = Customer("Bob the Raccoon")

# order1.customer = my_new_customer

# order2.customer = 1235789




# ### FOCUS LIST ### #
# lists & lists comprehension
# readme deliverables
# getters & setters
# sum & len
# reading test errors
# when to use if not vs if

# Customer

# Coffee

# Order - single source of truth

# Customer --< Order >-- Coffee