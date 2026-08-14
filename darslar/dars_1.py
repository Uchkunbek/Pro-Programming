# String methodlar ustida mashqlar

matn = 'muborak'
daraxt = 'terak'
baho = '5647853a'

# 1 .capitalize()
matn = matn.capitalize()
print(matn)

# 2 .title()
matn = matn.title()
print(matn)

# 3 .upper()
matn = matn.upper()
print(matn)

# 4 .lower()
matn = matn.lower()
print(matn)

# 5 .split()
matn = matn.split()
print(matn)

# 6 .isidentifier()
daraxt = daraxt.isidentifier()
print(daraxt)

# 7  .isdigit()
baho = baho.isdigit()
print(baho)

#8 .isdecimal()
baho ='shalgom'
matn = baho.isdecimal()
print(matn)

#9 .isnumeric()
rejaBajarilishi = '29797'
reja = rejaBajarilishi.isnumeric()
print(reja)

#10 .isalnum()
bilet =  '@sllk6789'
bilet = bilet.isalnum()
print(bilet)

#11 .join()
shaharlar = ("Samarqand", 'Damashq', 'Buxoro')
shahar = '***'.join(shaharlar)
print(shahar)

#12 .center()
txt = 'mavzu'
t = txt.center(20 ,'-')
print(t)

#13 .ljust()
txt = 'mavzu'
t = txt.ljust(20 ,'-')
print(t)

#14 .rjust()
txt = 'mavzu'
t = txt.rjust(6,'-')
print(t)

#15 .zfill() #agar zfill ga kiritilgan qiymat stringing lengths
# qiymatidan katta bo'lsa, string oldiga yetmagan qiymatga mos 0 zero qo'yib chiqaradi. string lengthdan kichik
#bo'lsa stingni o'zini qaytaradi.
txt = 'mavzu'
y_txt = txt.zfill(8) #000mavzu

#16 .translate()
javal = {66: 77} # B ni M ga aylantiradi
txt = 'Bobo Kolon'
y_txt= txt.translate(javal)
print(y_txt) # Momo Kolon

#17 .maketans()
mahsulot = 'moy'
myjadval = str.maketrans('m', 'T')
print(mahsulot.translate(myjadval)) #Toy

#18 .replace()
txt = "salom"
txt = txt.replace("s","S")
print(txt) #Salom

#19 .casefold()
txt = "BIR"
txt = txt.casefold()
print(txt)

#20 .encode()
t= 'am@mo'
t= t.encode()
print(t)

#21. .endswith()	Returns true if the string ends with the specified value
suz = 'olma'
txt = suz.endswith('b')
print(txt) #False

#22 .expandtab()
matn = """Asaka\tmashina\tishlab\tchiqarish\tzavodi"""
matn=matn.expandtabs(5)
print(matn) #Asaka     mashina   ishlab    chiqarish zavodi

#23 .split()
txt = """Vantan vodiysi"""
txt = txt.split()
print(txt) #['Vantan', 'vodiysi']

#24 .strip()
txt = "   Dasurlash sirlari haqida ertak"
txt = txt.strip()
print(txt) #Dasurlash sirlari haqida ertak

#25 .splitlines()
txt = 'Lorem20\nipsum'
t= txt.splitlines()
print(t) #['Lorem20', 'ipsum']

#26 .rindex()
txt = "Mi casa, su casa."
x = txt.rindex("sa")
print(x) #14

#27 .partition() argumentga kiritilgan strindan bo'lib, tuple qaytaradi. Agar argumet bo'sh bo'lsa 0 indexda sting
# va ikkita bo'sh sting tuple qaytaradi.

parcha = "Quyosh yer yuzini qizdiradi"
t = parcha.partition('yer')
print(t) #('Quyosh ', 'yer', ' yuzini qizdiradi')

#28 .isupper() Stindagi barcha harflar katta harf bo'lsa True qaytaradi
txt = "SALOm"
t = txt.isupper()
print(t) #False

#29 .ljust()
txt = "Sahara sahrosi"
t = txt.ljust(30,">" )
print(t)

#30 .rpartition()
my_matn = "Donolar donasi degan ekan, nima degan ekan"
t = my_matn.rpartition("degan")
print(t) #('Donolar donasi degan ekan, nima ', 'degan', ' ekan')

#31 .isprintable() stingda barcha belgilar ko'rinsa True qaytaradi \n, \t bo'lsa Falsa chiqaradi
kitob = "Samarqand tarixiy\n shahar"
print(kitob.isprintable()) #False

#32 .format()
ariza = """  Hurmatli {ism} aka sizni to'yga taklif qilamiz"""
print(ariza.format(ism = 'Uchqun').strip())

txt = "The binary version of {0} is {0:b}"

print(txt.format(123))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#33 .format.map()

person = {
    "name": "Temur",
    "age": 14,
    "job": "Dasturchi",
    "city": "Samarkand",
    "hobby": 'Swimming'
}

text = "{name} {age} yoshda. U {job} bo'lib ishlaydi va {city}da yashaydi. Bo'sh vaqtida {hobby} bilan shug'ullanadi"

print(text.format_map(person))

#34 .isspace() methodi string ichida faqat oq joy (probel) tashlangan bo'lsa True qaytaradji aks holda False, bo'sh
# string bo'lsa ham True qaytaradi

txt = " "
print(txt.isspace())

#35 .startwith()

txt = "Hush kelibsiz!"

x = txt.startswith("Hush")

print(x)





