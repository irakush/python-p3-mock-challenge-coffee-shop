#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == "__main__":
    print("HELLO! :) let's debug")

    coffee_1 = Coffee("Americano")
    coffee_2 = Coffee("Latte")

    customer_1 = Customer("John")
    customer_2 = Customer("Anna")
    customer_3 = Customer("Boris")

    order_1 = Order(customer_1, coffee_1, 2.0)
    order_2 = Order(customer_2, coffee_1, 5.0)
    order_3 = Order(customer_1, coffee_2, 5.0)
    order_4 = Order(customer_3, coffee_2, 3.0)
    order_2 = Order(customer_1, coffee_1, 5.0)

    ##########################################
    ##########################################
    ############### * TOTAL * ################
    ##########################################
    ##########################################
    all_customers = [customer_1, customer_2, customer_3]

    def total():
        total = 0
        for each_c in all_customers:
            total += each_c.total_payed()
            print(f"Customer: {each_c.name} :: Total Payed: {each_c.total_payed()}")

        print(f"Total: {total}")

    ipdb.set_trace()
