# Copy va Dictionary

# Shallow va deepcopy


# Dictionary yaratish usullari

# CRUD - Creat, Read, Update, Delete

# 1-usul. Python sintaks orqali
# 2-usul. Funksiya orqali orqali
# 3-usul. Tuple dict  orqali orqali

# Vazifalar

# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}

# def str_counter(listlar):
#     natija = {}
#     for i in listlar:
#         soni = len(i)  # listdagi item character soni
#         natija.update({soni: i})
#     return natija
#
#
# print(str_counter(['shaftoli', 'qulupnay', 'maymunjon', 'qalampirmunchoq']))

# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
# M: list_1 = ["a", "b", "c"]
#    list_2 = [1, 2, 3]
#    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}
#
# def merge_list(l1, l2):
#     yangi = {}
#     for item in range(len(l1)):
#         yangi[l1[item]] = l2[item]
#
#     return yangi
#
#
# print(merge_list(["a", "b", "c"], [1, 2, 3]))


# Buil-in methodlar orqali
# dict va zip methodlar
# def merge_list(l1, l2):
#     return dict(zip(l1, l2))
#
#
# print(merge_list(["a", "b", "c"], [1, 2, 3]))


# enumerate() orqali, bu funksiya listning ham indexni va itemni qaytaradi
def merge_list(l1, l2):
    yangi = {}
    for index, item in enumerate(l1):
        yangi[item] = l2[index]
    return yangi


print(merge_list(["a", "b", "c"], ["amma", "xola", "jiyan"]))

# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
#
#
# 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga
# olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.
#
#
# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}
#
