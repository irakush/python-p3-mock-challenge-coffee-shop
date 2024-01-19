class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, "name"):
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_cost = sum([order.price for order in Order.all if order.coffee is self])
        return total_cost / self.num_orders()


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def total_payed(self):
        return sum([order.price for order in self.orders()])

    def payd_by_coffee(self, coffee):
        return sum([order.price for order in Order.all if order.coffee is coffee])

    @classmethod
    def all_customers(cls):
        print([customer.name for customer in cls.all])

    @classmethod
    def all_payed(cls, coffee, customer):
        return [
            order.price
            for order in Order.all
            if order.customer is customer and order.coffee is coffee
        ]

    # @classmethod
    # def most_payd(cls, coffee):
    #     customers_dict = []

    #     for each_c in cls.all:
    #         customers_dict.append({each_c.name: sum(cls.all_payed(coffee, each_c))})

    #     max_payed = 0
    #     customer_payed = ""
    #     for obj in customers_dict:
    #         for key in obj.keys():
    #             if obj[key] > max_payed:
    #                 max_payed = obj[key]
    #                 customer_payed = key

    #     print(customers_dict)
    #     print(customer_payed)

    @classmethod
    def get_customer_by_name(cls, customer_name):
        return [customer for customer in cls.all if customer.name == customer_name]

    @classmethod
    def most_aficionado(cls, coffee):
        customers_dict = []

        for each_c in cls.all:
            customers_dict.append({each_c.name: sum(cls.all_payed(coffee, each_c))})

        max_payed = 0
        customer_payed = ""
        for obj in customers_dict:
            for key in obj.keys():
                if obj[key] > max_payed:
                    max_payed = obj[key]
                    customer_payed = key

        print(customers_dict)
        print(customer_payed)
        return cls.get_customer_by_name(customer_payed)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
