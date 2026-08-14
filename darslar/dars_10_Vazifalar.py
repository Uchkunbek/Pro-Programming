
# 1. Elektron Pochta Manzillarini Tekshirish:
# Email manzillar ro'yxati berilgan:
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for sikli va string metodlari yordamida har bir email manzilida "@" belgisi
# bor-yo'qligini tekshiring: Agar bo'lmasa, "Noto'g'ri email: email_manzi" deb
# chiqaring.


# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
#
# for email in pochtalar:
#     if email.find("@") != -1 and email.find(".") != -1:
#         print(f"To'g'ri email: {email}")
#     else:
#         print(f"Noto'g'ri email: {email}")


#2. Parol Kuchini Tekshirish:
# Foydalanuvchilarning parollar ro'yxati berilgan (masalan,
# ["password123", "Qwerty!", "admin", "StrongPass1!"]).
# ○ for sikli va shart operatorlari yordamida har bir parolni tekshiring:
# ■ Agar uzunligi 8 dan kam bo'lsa, "Juda qisqa"
# ■ Agar raqam yoki maxsus belgilar bo'lmasa, "Kuchsiz parol"
# ■ Aks holda, "Kuchli parol"

# paswords = ["password123", "Qwerty!", "admin", "StrongPass1!", "AssalomAlaykum"]
#
# for password in paswords:
#     if len(password) < 8:
#         print(f"Juda qisqa password: {password}")
#     elif  password.find("@") == -1 and password.find("!") == -1 and password.isdigit() == False:
#         print(f"Kuchsiz password: {password}")
#     else:
#         print(f"Kuchli password: {password}")


# 3. Ob-havo Ma'lumotlarini Tahlil Qilish:
# Bir hafta davomida kundalik haroratlar ro'yxati berilgan (masalan, [20,
# 22, 19, 24, 25, 23, 21]).
# ○ for sikli yordamida o'rtacha haroratni hisoblang va har bir kun uchun
# agar harorat 22 dan yuqori bo'lsa, "Iliq kun", aks holda "Salqin
# kun" deb chiqaring.


# haroratlar  = [20, 22, 19, 24, 25, 23, 21]
#
# for harorat in haroratlar:
#     if harorat  > 22:
#         print(f"Iliq kun")
#     else:
#         print(f"Salqin kun")

# 4. Restoran Buyurtmalari:
# ● Mavjud taomlar ro'yxati berilgan (masalan, ["Osh", "Shashlik", "Manti",
# “Lag’mon” ]).
# ● Foydalanuvchidan buyurtma kiritishni so'rang.
# ● for sikli yordamida foydalanuvchi kiritgan buyurtma mavjud taomlarga mos
# keladimi-yo'qligini tekshiring:
# ○ Agar mos kelsa, "Buyurtmangiz qabul qilindi" deb chiqaring.
# ○ Aks holda, "Kechirasiz, bunday taom yo'q" deb chiqaring.

# taom = ['Osh', 'Shashlik', 'Manti', 'Chuchvara']
#
# buyurtma = input("Buyurtma qiling: ")
#
# for x in taom:
#     if buyurtma == x:
#         print('Buyurtma qabul qilindi')
#         break
# else: #!!! Juda zo'r narsa o'rgandim , elsni forga tegishli qilish shunda for
#      # listni barcha itemni aylandi va elsni har safar ishlatmaydi
#
#         print("Kechirasiz bunday toam mavjud emas!")

# 5. Anketa Tahlili:
# ● Foydalanuvchilarning yoshlari ro'yxati berilgan (masalan, [16, 21, 17,
# 30, 25]).
# ● for sikli yordamida har bir foydalanuvchining yoshini tekshiring:
# ○ Agar yosh 18 dan kichik bo'lsa, "Yosh chegarasiga yetmagan"
# deb chiqaring.
# ○ Aks holda, "Xush kelibsiz" deb chiqaring

# anketa = [16, 21, 17,30, 25]
#
# for i in anketa:
#     if i < 18:
#         print("Yosh chegarasiga yetmagan")
#     else:
#         print("Xush kelibsiz")

# 6. Mobil Ilova Bildirishnomalari: Bildirishnomalar sarlavhalari ro'yxati berilgan
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish
# mavjud"]).
# for sikli yordamida agar sarlavha "Batareya past" bo'lsa, "Telefoningizni
# quvvatlang" deb print chiqaring.

# xabarlar= ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
#
# for x in xabarlar:
#     if x == "Batareya past":
#         print( "Telefoningizni quvvatlang")
#         break


# 7. Fayllarni guruhlash:
# fayllar = [ “kitob.jpg”, “ko_ jiguli.mp3”, “tabiat.jpg”, “malohat.mp3”, “iphone16.jpg”]
# musiqalar=[ ] va rasmlar=[ ] nomli listlar yarating. Fayllar ustida sikl aylantirib “.jpg”
# larni rasmlar listiga, “.mp3” larni musiqalar listiga qo’shing. Yordam: find() string
# metodi va append() list metodidan foydalaning.


fayllar = [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]

musiqalar = []
rasmlar = []

for x in fayllar:
    if x in fayllar and x.endswith(".jpg") :
        rasmlar.append(x)
    elif x in fayllar and x.endswith(".mp3") :
        musiqalar.append(x)

print(rasmlar)
print(musiqalar)