# users = {'Uchqun': 'root', 'Baxa': 'root2', 'Ben': 'root3'}
#
# print(users["Baxa"])

# i = 10
# while i > 5:
#     print(i)
#     i -= 2


# 11-dars mashqlari

#1. While siklidan fordalanib print qiling.
"""
1
22
333
4444
55555
"""
# num = 1
# while num <=5:
#     print(str(num) * num)
#     num += 1

#2. While loopdan foydalanib raqamlay yig'indisini hisoblaydigan dastur tuzing.

# while True:
#     son = input('Uch xonali son kiriting:  ')
#     print(int(son[0]) + int(son[1]) + int(son[2]))
#     break


# 3.While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing

# for loop bilan 1 dan 100 gacha toq sonlar yig'indisi

# son = []
# for i in range(1,100,2):
#     son.append(i)
# print(sum(son))

# 1 dan 100 gacha toq sonlar yig'indisi print bilan
# print(sum(range(1,100,2))

# while  loop bilan 1 dan 100 gacha toq sonlar yig'indisi
# jami = 0
# i = 1
# while i < 100:
#     jami += i
#     i += 2
# print(jami)

# 4. While orqali ro'yxatdagi eng katta sonni topuvchi dastur yozing

# son = []
# i=1
# while  i < len(son):

# sonlar = [3, 8, 2, 15, 7, 56]
#
# eng_katta = sonlar[0]
# i = 1
#
# while i < len(sonlar):
#     if sonlar[i] > eng_katta:
#         eng_katta = sonlar[i]
#     i += 1

# print(eng_katta)

# print(max(sonlar))

# Listdagi ikkinchi eng katta sonni topish

# sonlar = [3, 8, 2, 15, 7, 56, 58]
#
# eng_katta = sonlar[0]
# ikkinchi = sonlar[0]
# i = 0
#
# while i < len(sonlar):
#     if sonlar[i] > eng_katta:
#         ikkinchi = eng_katta
#         eng_katta = sonlar[i]
#     elif ikkinchi > sonlar[i] and ikkinchi < eng_katta:
#         ikkinchi = sonlar[i]
#     i += 1
#
# print(eng_katta)
# print(ikkinchi)

