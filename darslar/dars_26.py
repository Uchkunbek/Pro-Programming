import json

"""Kim millioner bo'lmoqchi o'yini"""

ism = ""
harflar = ["A", "B", "C", "D"]
togri_javoblar_soni = 0
natijalar = {}

#Dastur boshlanishida saqlangan natijalarni json filidan o'qish.
try:
    with open("natijalar.json", "r", encoding="utf-8") as file:
        natijalar = json.load(file)
except FileNotFoundError:
    natijalar = {}

while True:
    #Bosh menu doim chiqib turadi
    print("Kim millioner bo'lmoqchi o'yini")

    print("Buyruqni tanlang")

    print("1. O'ynash")
    print("2. Rayting")
    print("0. Chiqish")

    choice = input("Tanlovingiz: ")

    if choice == "1":
        #foydalanuvchidan ism kiritishini so'rash, va ism mavjudligini tekshirish
        ism = input("Ismingizni kiriting: ").lower().capitalize()
        if not ism:
            print("Ismingizni kiritishingiz kerak!")
            continue

        #Foydalanuvchi ismini va urinishlar sonini chiqarish
        if ism and ism in natijalar:
            print(f"O'yinchi: {ism}")
            print(f"Jami o'yinlar: {natijalar[ism]['games_played']}")

        #test.json filidan ma'lumot olish
        with open("tests.json", "r", encoding="utf_8") as file:
            tests = json.load(file)

        #Nechanchi savoldan nechanchisi ekanini ko'rsatish print("Savol: 1/10")
        for savol_raqami, test in enumerate(tests, start=1):
            print(f"Savol: {savol_raqami}/{len(tests)}")

            # barcha savollar ketma-ket chiqarish uchun test savollarini ham shu loopga solamiz
            print(test["question"])

            # Javob variantlarini A, B, C, D harflari bilan chiqaramiz
            for i, answer in enumerate(test["answers"]):
                print(f'{harflar[i]}) {answer["key"]}')

            # javob - foydalanuvchidan javob variantini so'rash
            javob = input("Javobingiz (A/B/C/D): ").upper()

            # savol javoblari orasidan to'g'ri javobni topish
            for i, answer in enumerate(test["answers"]):
                if answer["isTrue"]:
                    # togri_javob - JSON fayldan topilgan to‘g‘ri harf.
                    togri_javob = harflar[i]

            # foydalanuvchi kiritgan javob bilan to'g'ri javobni tekshirish.
            if togri_javob == javob:
                print("javob togri")
                togri_javoblar_soni += 1
                print(f"To'g'ri javoblar soni: {togri_javoblar_soni}")
            else:
                print("notogri javob")
                break
        else:
            #Agar o'yinchi barcha javoblarga to'liq javob bersa forni else ishlaydi.
            print("Tabriklaymiz! Barcha savollarga to'g'ri javob berdingiz!")
            print(f"To'g'ri javoblar soni: {togri_javoblar_soni}")

        # Natijalarni hisoblash va dict qilib  saqlash.
        if ism in natijalar:
            natijalar[ism]["games_played"] += 1

            if togri_javoblar_soni > natijalar[ism]["best_score"]:
                natijalar[ism]["best_score"] = togri_javoblar_soni
        else:
            natijalar[ism] = {
                "games_played": 1,
                "best_score": togri_javoblar_soni
            }

        #Natijani JSON file qilib saqlash.
        with open("natijalar.json", "w", encoding="utf-8") as file:
            json.dump(natijalar, file, ensure_ascii=False, indent=4)
    elif choice == "2":
        print("Ism    | O'yinlar soni | Best score")

        for ism, natija in natijalar.items():
            print(f"{ism} | {natija['games_played']} | {natija['best_score']}")
    elif choice == "0":
        break
