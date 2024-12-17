import time
import random

sozlar = ["banana",
    "apple",
    "orange",
    "pear",
    "kiwi",
    "watermelon",]

def word():
    soz = random.choice(sozlar)
    a = list(soz)
    random.shuffle(a)
    return "".join(a), soz
bal=0
rekord=0
time_limit=10
while True:
    masala, asl_soz = word()
    print(masala)
    start_time = time.time()
    javob = input("Javob: ")
    end_time = time.time()

    if javob == asl_soz:
        bal+=1
        time_limit += 2 if time_limit + 2 <= 10 else 0
        rekord+=1
        print(f"To'g'ri balingiz {bal}")
    else:
        bal-=1
        time_limit -= 3
        print(f"Xato balingiz: {bal}")
    if rekord>10:
        print(f"yangi rekord {rekord}")
    if end_time - start_time > time_limit:
        print(f"Sizning vaqtingiz tugadi! Joriy bal:{bal}")
        break