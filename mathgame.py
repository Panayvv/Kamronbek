# # import random
# # import time
# # import json
# #
# #
# # def save_data(data):
# #     """O'yin malumotlarini filega yozadi"""
# #     with open('game.data.json', 'w') as file:
# #         json.dump(data, file)
# #
# #
# # def get_data():
# #     """O'yin malumotlarini filedan oqib oladi"""
# #     with open('game.data.json', 'r') as file:
# #         data = json.load(file)
# #         return data
# #
# #
# # def generate_problems(level):
# #     amallar = ['+', '-', '*', '//', '**']
# #     amal = random.choice(amallar)
# #     a = random.randint(1, level * 5)
# #     b = random.randint(1, level * 5)
# #     if amal == '//':
# #         a *= b
# #     elif amal == '**':
# #         a = random.randint(1, level * 10)
# #         b = random.randint(1, 3)
# #     return f"{a}{amal}{b}"
# #
# #
# # def generate_problems_for_a(level):
# #     amallar = ['+', '-', '*', '//', '**']
# #     amal = random.choice(amallar)
# #     a = random.randint(1, level * 5)
# #     b = random.randint(1, level * 5)
# #     if amal == '//':
# #         a *= b
# #     elif amal == '**':
# #         a = random.randint(1, level * 10)
# #         b = random.randint(1, 3)
# #
# #     masala = f"{a}{amal}{b}"
# #     javob = eval(masala)
# #     return f"a{amal}{b}={javob}"
# #
# #
# # data = get_data()
# # level = 1
# # bal = 0
# # record = data['record']
# #
# time_limit = 10
# counter = 0
# print(f"Joriy rekord:{record}")
# while True:
#     counter += 1
#     masala = generate_problems(level)
#     togri_javob = eval(masala)
#     print(f"{counter}){masala}=", end='')
#     start_time = time.time()  # masala berilgan vaqt
#     javob = int(input())
#     end_time = time.time()  # masalaga javob berilgan vaqt
#
#     if javob == togri_javob:
#         bal += 1
#         data['bal'] = bal
#         time_limit += 2 if time_limit + 2 <= 10 else 0
#         print(f"To'g'ri!!! balingiz: {bal}", f"time limit:{time_limit}")
#     else:
#         bal -= 1
#         time_limit -= 3
#         print(f"Xato!!! to'g'ri javob:{togri_javob}  balingiz: {bal}", f"time limit:{time_limit}")
#     if bal % 5 == 0:
#         level += 1
#         print(f"Sizning darajangiz oshdi daraja={level}")
#     if bal > record:
#         record = bal
#         data['record'] = record
#         print(f"Siz rekordni yangilandingiz  rekord={record}")
#     save_data(data)
#     if end_time - start_time > time_limit:
#         print(f"Sizning vaqtingiz tugadi! Joriy bal:{bal}")
#         break