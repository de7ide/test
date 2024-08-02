# def do_some(num: int, word: str) -> str:
#     word = word.capitalize()
#     print( word * num)

# do_some(15, 'capi')
#----------------------------
# class User:
#     def __init__(self, user_id, name, age, email):
#         self.user_id = user_id
#         self.name = name
#         self.age = age
#         self.email = email


# def get_user_info(user: User) -> str:
#     return f"The user's age is {user.name} - {user.age}, "\
#         f"a email - {user.email}"


# user_1: User = User(233452, "Sergei", 54, 'ser@gmail.com')
# print(get_user_info(user_1))
# ----------------------------------------

# from dataclasses import dataclass


# @dataclass
# class User:
#     user_id: int
#     name: str
#     age: int
#     email: str


# def get_user_info(user: User) -> str:
#     return f"The user's age is {user.name} - {user.age}, "\
#         f"a email - {user.email}"


# user_1: User = User(233452, "Sergei", 54, 'ser@gmail.com')
# print(get_user_info(user_1))
#--------------------------------