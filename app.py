#! /usr/bin/env python3


class House():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

        # amount per year in rent
        self.rental_yield = price/10

    def get_price(self):
        return self.price

    def __str__(self):
        return 'House. Price:{}, owner {}, yield {}'.format(self.price, self.owner, self.rental_yield)

    def __repr__(self):
        return repr(self.name)


class Yearable():
    def do_year(self):
        pass


class Person(Yearable):
    def __init__(self, name, opening_balance, age=18, salary=0):
        self.name = name
        self.balance = opening_balance
        self.houses = []
        self.age = age
        self.salary = salary

    def buy(self, house):
        self.houses.append(house)
        self.balance = self.balance - house.get_price()
        if not house.owner:
            print('it was unowned')
            house.owner = self
        else:
            print('it was owned by {}'.format(house.owner))
            house.owner = self

    def rent(self, house):
        self.rented_house = house

    def __str__(self):
        return 'Person {}, age {}, cash {}, houses {}'.format(self.name, self.age, self.balance, self.houses)

    def do_year(self):
        self.age += 1
        self.balance = self.balance + self.salary
        if self.rented_house:
            self.balance -= self.rented_house.rental_yield


def create_houses():
    houses = []
    house = House('The Mews', 100)
    house2 = House('The Parsonage', 200)
    houses.append(house)
    houses.append(house2)
    return houses


def create_people():
    people = []
    person = Person(name='Anthony', opening_balance=1000, salary=80000)
    people.append(person)

    person2 = Person(name='Mary', opening_balance=2000, salary=90000)
    people.append(person2)

    house = House('The Mews', 450000)
    person.rent(house)
    person2.rent(house)
    return people


def run_year(people, iters=10):
    counter = 0
    while counter < iters:
        counter += 1
        for person in people:
            person.do_year()


people = create_people()
run_year(people=people, iters=5)
for person in people:
    print(person)
