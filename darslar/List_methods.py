#Dictionary Methods

#1. clear()	Removes all the elements from the dictionary

xodimlar = {
    "Ism": "Uchqun",
    "Yosh": 39,
    "Kasbi": "Dasturchi",
    "Maoshi": 5000
}

# xodimlar.clear()
# print(xodimlar)

#2. copy()	Returns a copy of the dictionary

# xodimlar2 = xodimlar.copy()
# print(xodimlar2)

#3. fromkeys()	Returns a dictionary with the specified keys and value
# x = {
#     "Ism": "Uchqun",
#     "Yosh": 39,
#     "Kasbi": "Dasturchi",
#     "Maoshi": 5000
# }
# y = 'xurmo+'
#
# yangi_dict = dict.fromkeys(x, y)
# print(yangi_dict)


#4. get()	Returns the value of the specified key

# x = xodimlar.get("Ism") # Agar berilgan key bo'lamasa None qaytaradi.
# y = xodimlar["Ism"]  # Key/index murojaat qilganda topilmasa Key Error beradi.

# xodimlar['Ism']
# da esa
# print(x)
# print(y)


#5. items()	Returns a list containing a tuple for each key value pair

# x  = xodimlar.items()
# print(x) #dict_items([('Ism', 'Uchqun'), ('Yosh', 39), ('Kasbi', 'Dasturchi'), ('Maoshi', 5000)])

"""" Kichik amaliyotcha"""

# # Mevalar va ularning narxlari (so'mda)
# mevalar = {
#     "Olma": 12000,
#     "Banan": 25000,
#     "Uzum": 40000,
#     "Anor": 30000
# }
#
# # 1. Lug'atdagi barcha elementlarni chiqarish
# print("--- Mevalar va narxlar ---")
# for meva, narx in mevalar.items():
#     print(f"{meva}: {narx} so'm")
#
# # 2. Narxi 20,000 so'mdan qimmat mevalarni topish
# print("\n--- Qimmat mevalar (20,000 dan yuqori) ---")
# for meva, narx in mevalar.items():
#     if narx > 20000:
#         print(f"{meva} - {narx} so'm")


#6. keys()	Returns a list containing the dictionary's keys
# mevalar = {
#     "Olma": 12000,
#     "Banan": 25000,
#     "Uzum": 40000,
#     "Anor": 30000
# }
#
# print(mevalar.keys())
#
# print('------MEVALAR------')
# for key in mevalar.keys():
#     print(key)

#7. pop()	Removes the element with the specified key
# Xarid savatchasi
# savat = {
#     "telefon": 300,
#     "quloqchin": 50,
#     "g'ilof": 15,
#     "soat": 120
# }
#
# print("Boshlang'ich savat:", savat)
#
# # 1. Elementni o'chirish va uning qiymatini olish
# ochirilgan_narx = savat.pop("quloqchin")
# print(f"\nO'chirilgan mahsulot narxi: {ochirilgan_narx}$")
# print("O'chirishdan keyingi savat:", savat)
#
# # 2. Mavjud bo'lmagan kalit bilan pop() ishlatish (Xatolik oldini olish)
# # Ikkinchi argument sifatida standart xabar ko'rsatiladi
# noma_lum = savat.pop("noutbuk", "Mahsulot topilmadi")
# print(f"\nNoutbuk narxi: {noma_lum}")
#
# discount = savat.pop("soat")
# print(f"Soat: {discount} so'm edi, tugadi")
#
# print(f"\nDiscount: {discount}")

# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary