# class Hero:
#     def __init__(self, name, lvl, classname):
#         self.name = name
#         self.lvl = lvl
#         self.classname = classname
#
#     def __str__(self, name):
#         return self.name
#
#     def action(self):
#         return f"Hero: {self.name}\nlvl:{self.lvl}\nclassname:{self.classname}"
#
#     test = Hero(123)
# class money:
#     def __init__(self, money, currently):
#         self.money = money
#         self.currently = currently
#
#     def __add__(self, other):
#         print(self.currently)
#         print(other.currently)
#         print(self.currently + other.currently)
#
#     def __del__(self):
#         print(self.currently)
#
#     def __getitem__(self, item):
#         print(self.currently)
#
#     def __len__(self):
#         print(self.currently)
#
#     def __ge__(self, other):
#         print(self.currently)
#
#     def __new__(cls, *args, **kwargs):
#         print(cls.__name__)
#
#     def __call__(self):
#         print(self.currently)
#
# Som = money(100, 'SOM')
# USD = money(100, 'USD')
#
# new_object = Som+USD
#
# class Test:
#     name = "class name"
#
#     def __init__(self, value):
#         self.value = value
#
#     def test(self):
#         pass
#
#     def __test(self):
#         pass
#
#     def test2(self):
#         print(f"{self.value} i am working")
#
#     @staticmethod
#     def static_method():
#         print('i am static method')
#
#     @classmethod
#     def class__method(cls):
#         print(cls.name)
#
#     @property
#     def property_method(self):
#         return 'atrebut'
#
# test = Test('test')
# test.test2()
# Test.static_method()
# Test.class__method()
# print(test.property_method)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

Momi = User('momi', 'white')
print(Momi.full_name)