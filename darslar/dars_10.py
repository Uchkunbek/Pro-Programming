# mevalar = ["olma", 'olcha', 'anor', 'uzum', 'olcha', 'shaftoli',"olma", 'olcha', 'anor', 'uzum', 'olcha', 'shaftoli']

# for meva in mevalar:
#     if meva == 'olcha':
#         continue
#     print(meva)

# O'ziming urinishim birdaniga setga assign qilib quymoqchi edim.
# m = {}
# m = mevalar.copy()

# uMevalar = list(set(mevalar)   )  # list(set(mevalar)) unik list qiladi lekin tarib avtomatik bdi.
# unikMevalar = list(dict.fromkeys(mevalar)) # list(dict.fromkeys(mevalar)) unik qilib, tartib saqlandi.
#
# # qo'lda taxlash
# emptyList = []
# for i in mevalar:
#     if i not in emptyList:
#         emptyList.append(i)
#
# print(emptyList) #qo'lda qilingan bunda ham tartib bo'lamas ekan
# print(unikMevalar) #list(set((mevalar))
# print(uMevalar) # list(dict.fromkeys(mevalar))

# ! Faktorialni hisoblash

# son = int(input("Son: "))
# natija = 1
# for i in range(1, son+1):
#     natija = natija*i
#
# print(natija)

#Tubsonni topish

# import math
#
# son = int(input("Son: "))
#
# if son < 2:
#     print("Tub son emas")
# elif son == 2:
#     print("Tub son")
# elif son % 2 == 0:
#     print("Tub son emas")
# else:
#     for i in range(3, math.isqrt(son) + 1, 2):
#         if son % i == 0:
#             print("Tub son emas")
#             break
#     else:
#         print("Tub son")

# x= 0
# for i in range(1,4):
#     x = x+i
#     print(x)