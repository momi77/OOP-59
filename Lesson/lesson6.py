# ДЕКОРАТОР
# Big O натация
# (Что такое декоратор?)Декоратор - это функция, которая принимает другую функцию
# как аргумент и возвращает новую функуцию,
# обычно обернутую в дополнительную функциональность

#                        def say_hello 2 шаг
# def simple_decorator(func):
#     def wrapper():
#         print("До выполнения!!") #3 шаг
#         func()           #4 шаг say_hello
#         print("После выполнения!!") # 5 шаг
#     return wrapper
#
# # simple_decorator(say_hello) - 1 шаг
# @simple_decorator
# def say_hello():
#     print('Hello')
#
# say_hello()
#
#              #def_greeting()
# def greeting_decorator(func):
#     def wrapper(name):
#         func(name)
#         print(f"{name} how are u?")
#     return wrapper
#
# # greeting_decorator(greeting)
# #     def wrapper(name)
# @greeting_decorator
# def greeting(name):
#  print(f"{name} hello")
# greeting("Ardager") #шаг 1 def greeting_decorator(greeting())
#                        #def wrapper("Ardager")
#
# # Декоратор который может принимать параметры
# def repeat_decorator(n):
#     def decorator(func):
#         def wrapper(name):
#             for i in range(n):
#                 func(name)
#         return wrapper
#     return decorator
#
# @repeat_decorator(4)
# def say_name(name):
#     print(f"momi")
#
# say_name("Ardager") #repeat_decorator(4)
#                 # def decorator(def say_name())
#                 # def wrapper("Ardager")
#                 # for i in range(4)
#                 #def say_name()
#
#             #class OldClass
# def class_decorator(cls):
#     class NewClass(cls):
#         def new_method(self):
#             return "Я новый метод!!!"
#     return NewClass
#
# @class_decorator
# class OldClass:
#
#     def old_method(self):
#         return "Я старый метод!!!"
#
# obj_1 = OldClass()
#
# print(obj_1.old_method())
#
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
# ardager = User("Ardager", "admin")
#
# def is_admin(func):
#     def wrapper(user, command):
#         if user.role == "admin" and command == "ban":
#             func(user, command)
#         else:
#             print("Вы не админ или такой команды нет!!!")
#     return wrapper
#
# @is_admin
# def ban(user, command):
#     print(f"Выполнен бан")
#     # print(f'{user.name} забанил пользователя!!) то есть можно крч и так написать
#     # ban(ardager, "ban")


# 2 part of lesson
# 1 exemple
# def find_element(array, target):
#     print(array[target])
#     # for num, ind in enumerate(array):
#     #     if target == ind:
#     #         print('find')
#     #     else:
#     #         print('not find')
#
# find_element([1,2,45,6,54,3], 3)

# 2 exemple
# O (n)
# O (long n)
def find_element(array, target):
    left, right = 0, len(array) -1

    while left <= right:
        mid = (left + right) // 2
        print(f'LEFT: {left} == RIGHT: {right} ')
        print(mid)
        if array[mid] == target:
            return print('find')
        elif array[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return print('not find')
    # for i in array:
    #     if i == target:
    #         print('find')
    #     else:
    #         print('not find')

find_element([1,2,45,6,54,3], 3)
