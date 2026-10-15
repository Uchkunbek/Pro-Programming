# Recrusive funksiyalar. (O'zini-o'zi chaqiruvchi funksiyalar)

# def factorial(n):
#     if n == 0: #Base shart
#         return 1
#     return n * factorial(n-1) #funksiyani o'zini qayta chaqirish
# print(factorial(5))

# Tower of Hanoi o'yini

def hanoi(n, a, b, c):
    if n == 1:
        print(f"1-diskni {a} -> {c} ko'chiring")
        return

    # 1. Kichik disklarni yordamchi a -> b o'tkazish,
    # funksiya parametriga  a , c va b deb beramiz.
    hanoi(n - 1, a, c, b)

    # 2. Eng katta diskni a -> c o'tkazish
    print(f"{n}-diskni {a} -> {c} ga ko'chiring")

    # 3. Kichik disklarni b -> c o'tkazishda
    # shunchaki funksiyani parmetrlari joyini o'zgartirib qo'yamiz.
    hanoi(n - 1, b, a, c)


# Foydalanuvchidan disk sonini kiritishni so'raymiz
disklar_soni = int(input("Disklar sonini kiriting: "))

print(f"Siz eng kamida {2**disklar_soni-1}"
      f" marta 🤫 harakat qilib disklarni ko'chirishingiz kerak!!!")

# Disklarni A ustundan C ustunga o'tkazish.
hanoi(disklar_soni, "A", "B", "C")
