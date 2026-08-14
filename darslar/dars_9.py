# 9_dars mashqlar

# 1. Ob-havo Tavsifi: Foydalanuvchidan ob-havo haroratini inputda so'rang.
# Agar harorat 0 dan past bo'lsa, "Sovuq" deb print chiqaring.
# Agar 0 dan 20 gacha bo'lsa, "Salqin".
# Agar 21 dan 30 gacha bo'lsa, "Iliq".
# Agar 31 dan yuqori bo'lsa, "Issiq" deb chiqaring.


# tem = int(input("Haroratni kiriting: "))
# if tem <= 0:
#     print('Sovuq')
# elif tem > 0 and tem < 20:
#     print('Salqin')
# elif tem > 21 and tem < 31:
#     print('Iliq')
# else:
#     print('Issiq')





# 2. Internet-do'kon Chegirmasi: Foydalanuvchidan xarid summasini so'rang. Agar summa
# 50,000 so'mdan kam bo'lsa, chegirma yo'q. Agar 50,000 dan 100,000 so'mgacha bo'lsa,
# 5% chegirma. Agar 100,000 so'mdan yuqori bo'lsa, 10% chegirma hisoblang va yakuniy
# narxni chiqaring.

# summa =int(input('Summani kiriting: '))
#
# if summa < 50000 :
#   print('Chegirma yo\'q')
# elif summa > 50000 and summa <= 100000 :
#    print('5% chegirma ' + str(summa * 0.95))
# elif summa > 100000 :
#    print('10% chegirma ' + str(summa * 0.9))





# 3. Tizimga Kirish: Foydalanuvchidan login va parolni so'rang. Agar login "admin" va parol
# "12345" bo'lsa, "Xush kelibsiz, admin!" deb chiqaring. Agar login yoki parol noto'g'ri bo'lsa,
# "Login yoki parol xato" deb chiqaring.

# admin = "uchkun"
# password = "nobody"
# user_admin = input("Admin: ")
# user_password = input("Password: ")
# if user_admin == admin and user_password == password:
#     print("Xush kelibsiz, admin")
# else:
#     print("Login yoki parol xato")


# 4. Film Yosh Cheklovi: Foydalanuvchidan yoshini so'rang. Agar yosh 13 dan kichik bo'lsa,
# "Sizga ushbu film tavsiya etilmaydi" deb chiqaring. Agar 13 dan 17 gacha bo'lsa, "Siz filmni
# ota-onangiz bilan ko'rishingiz mumkin". Agar 18 va undan katta bo'lsa, "Siz filmni tomosha
# qilishingiz mumkin" deb chiqaring.

# yosh = int(input('Yosh: '))
# if yosh < 13:
#     print('Sizga ushbu film tavsiya etilmaydi')
# elif yosh > 13 and yosh < 17:
#     print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
# else:
#     print('Siz filmni tomosha qilishingiz mumkin')





# 5. Restoran Menyusi: Foydalanuvchiga menyudan taom tanlash imkoniyatini bering: 1 -
# "Osh", 2 - "Mastava", 3 - "Shashlik". Tanlovga qarab taomning narxi va tayyorlanish vaqtini
# chiqaring.

# print("Menyu")
# print("1 - Osh")
# print("2 - Mastava")
# print("3 - Shashlik")
#
# tanlov = int(input("Taomni tanlang (1-3): "))
#
# if tanlov == 1:
#     print("Osh")
#     print("Narxi: 30 000 so'm")
#     print("Tayyorlanish vaqti: 40 daqiqa")
#
# elif tanlov == 2:
#     print("Mastava")
#     print("Narxi: 25 000 so'm")
#     print("Tayyorlanish vaqti: 30 daqiqa")
#
# elif tanlov == 3:
#     print("Shashlik")
#     print("Narxi: 20 000 so'm")
#     print("Tayyorlanish vaqti: 20 daqiqa")
#
# else:
#     print("Bunday taom menyuda yo'q!")
#

# 6. Email Tekshiruvi: Foydalanuvchidan email manzilini inputda kiritishni so'rang. Agar
# emailda "@" belgisi va "." nuqtasi bo'lmasa, "Noto'g'ri email manzili" deb chiqaring. Aks
# holda, "Email qabul qilindi" deb chiqaring.
# Yordam: find() string metodidan foydalaning. Masalan if matn.find(“belgi”) == -1 bo’lsa
# demak belgi matnda topilmagan bo’ladi.

# email = input('Enter your email: ')
#
# if  email.find('@') != -1 and email.find('.') != -1:
#     print('Email qabul qilindi')
# else:
#     print('Noto\'g\'ri email manzili')





# 7. Talaba Baholash Tizimi: Foydalanuvchidan olgan ballini so'rang (0 dan 100 gacha).
# Quyidagi mezonlarga ko'ra bahoni print qiling:
# ● 86 dan 100 gacha: 5 baho
# ● 70 dan 85 gacha: 4 baho
# ● 55 dan 69 gacha: 3 baho
# ● 55 dan past: 2 baho

# baho = int(input('Baliningizni kiriting (1-100):  '))
# if baho >= 86 and baho<= 100 :
#     print('5 baho')
# elif baho > 70 and baho < 86 :
#     print('4 baho')
# elif baho >= 55 and baho <= 70 :
#     print('3 baho')
# else :
#     print('2 baho')


# 8. Bankomat Pul Yechish: Foydalanuvchidan kartasidagi summani va yechmoqchi
# bo'lgan summani so'rang. Ya’ni 2 ta input bo’ladi. Agar kartadagi puli yechiladigan puldan
# kam bo'lsa, "Hisobda yetarli mablag' mavjud emas" deb print chiqaring. Agar yechiladigan
# summa 5 000 so'mdan kam bo'lsa, "Minimal yechish summasi 5 000 so'm" deb chiqaring.
# Aks holda, "Pul muvaffaqiyatli yechildi" deb print chiqaring va kartadagi qolgan mablag'ni
# print qiling.

# kartadagi_pul = int(input("Kartadagi pul: "))
# chiqadigan_summa = int(input("Summani kiriting: "))
#
# if kartadagi_pul < chiqadigan_summa:
#     print("Hisobda yetarli mablag' mavjud emas")
# elif chiqadigan_summa < 5000:
#     print("Minimal yechish summasi 5 000 so\'m")
# elif kartadagi_pul >= chiqadigan_summa and chiqadigan_summa >= 5000:
#     print("Pul muvaffaqiyatli yechildi")
#     print(f'Kartadagi pul {kartadagi_pul-chiqadigan_summa}')



# 9. Ish Jadvalini Tekshirish: Foydalanuvchidan haftaning kunini so'rang (Dushanba,
# Seshanba, ... , Yakshanba). Agar kun "Shanba" yoki "Yakshanba" bo'lsa, "Bugun dam olish
# kuni" deb chiqaring. Aks holda, "Bugun ish kuni" deb chiqaring.

# kun = input("Hafta kunini kiriting: ")
# kun = kun.lower()
# if kun == 'yakshanba' or kun == 'shanba':
#     print("Bugun dam olish kuni")
# elif  kun == 'dushanba' or kun == 'seshanba' or kun == 'chorshanba' or kun == 'payshanba' or kun == 'juma':
#     print('Bugun ish kuni')
# else:
#     print('Hafta kunini kiriting!')





# 10. Mobil Tarif Tanlash: Foydalanuvchidan oyiga qancha internet trafikidan foydalanishini
# so'rang (GB da). Agar trafik 1 GB dan kam bo'lsa, "Sizga 'Mini' tarifi mos keladi" deb
# chiqaring. Agar 1 GB dan 5 GB gacha bo'lsa, "Sizga 'Standard' tarifi mos keladi". Agar 5
# GB dan yuqori bo'lsa, "Sizga 'Unlimited' tarifi mos keladi" deb chiqaring.

# tariff = int(input('Bir oyda qancha internet trafikidan foydalanish: '))
#
# if tariff == 1:
#     print("Sizga 'Mini' tarifi mos keladi")
# elif tariff > 1 and tariff < 5:
#     print("Sizga 'Standard' tarifi mos keladi")
# elif tariff > 5:
#     print("Sizga 'Unlimited' tarifi mos keladi")
# else:
#     print("Internetsiz ham hayot go\'zal!")






#Raqamlari bir xil uch xonali son

# son = input('Uch xonali son kiriting: ')
#
# if son[0]==son[1]  and son[0]==son[2]  and len(son)==3:
#     print('Oltin raqam')
# else:
#     print('Bir xil emas')
