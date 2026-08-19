#Funksiyalar

# sales =    {
# "yanar": 16000,
# "fevral": 6000,
# "mart": 5000,
# "may": 20000
# }
#
# def max_oy(d):
#     return max(d, key=d.get)
#
# yuqori_oy = max_oy(sales)
# print(yuqori_oy)

#1.Berilgan ro‘yxatdan barcha juft sonlarni o‘chirib tashlang (faqat remove yoki pop ishlatib):

# sonlar = [1, 2, 3, 3,2, 4, 5, 6, 7, 8, 9, 10,11, 14,78,7,9]

# print(len(sonlar))

# for i in range( 0,len(sonlar), 2):   # orqadan oldinga
#     print(sonlar[i])
    # if sonlar[i] % 2 == 0:
    #     sonlar.pop(i)          # yoki sonlar.remove(sonlar[i])


# print(len(sonlar))
# print(sonlar)

# a = "\u0030"
# b = "\u0047"
#
# print(a.isdecimal())
# print(b.isdecimal())


# 1. "user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz.
# va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini
#
#   Ism: Alisher
#   Familiya: Olimov
#   Yosh: 27
#
# ko'rinishiga print qilib bersin.

# def user_data(first_name, last_name, age):
#     print(f"""
#     ----Siz haqingizda ma'lumot-----
#
#         First Name: {first_name}
#         Last name: {last_name}
#         Age: {age}
#
#     ====== R A H M A T =======
#
# """)
#
# # Tekshirib ko'ramiz
# print(user_data('Uchqun', 'Ashirov', 39))




# 2. "find_max" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (a, b, c).
# Input orqalik 3 ta son kiritamiz.
# va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# topib print qiladi.
#
#   Eng katta son - A = 10
#   yoki
#   Eng katta son - A va B = 10
#   yoki
#   Eng katta son - A va B va C = 10

# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return f"Eng katta son - A = {a}"
#     elif b >= a and b >= c:
#         return f"Eng katta son - B = {b}"
#     else:
#         return f"Eng katta son - C = {c}"
#
# # Tekshirib ko'ramiz:
# print(find_max(10, 30, 6))  # Natija: Eng katta son - A = 10

# 3. "find_letter_count" funksiyasini elon qilasizlar.
# Funksiyani 2 ta parametri bor (word, letter).
# Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
# va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# "find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
# "word" da "letter" nechi martda qatnashganini print qilsin.
# "Programing" so'zida "r" dan 2 ta.

# def find_letter_cont(word, harf):
#     soni = []
#     for i in word:
#         soni.append(i)
#     return soni.count(harf)
#
# print(find_letter_cont('saalommm', 'm'))

# 2-variant

# def find_letter_cont(word, harf):
#     return word.count(harf)
#
# print(find_letter_cont('Assalomu Alaykum', 'k'))


# 4. "list_sum" funksiyasi elon qilasizlar.
# Funksiyani 1 ta pametrni bor (myList).
# "myList" funksiyasini chaqirib unda argumentini berasizlar.
# uni ichida esa myList elementlarini yig'indisini print qilasizlar.
#
#   Listning elementlar yig'indisi = 32
