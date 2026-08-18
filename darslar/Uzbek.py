def uzbek_number(num):
    ones = ['bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
    tens = ['', 'o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
    if num == 0:
        return "nol"
    if num < 10:
        return ones[num-1]
    elif num < 20:
        return 'o\'n ' + ones[num % 10-1]
    elif num < 100:
        return tens[num // 10] + (' ' + ones[num % 10-1] if num % 10 != 0 else '')
    elif num < 1000:
        return ones[num // 100-1] + ' yuz ' + uzbek_number(num % 100)
    elif num < 1_000_000:
        return uzbek_number(num // 1_000) + ' ming ' + uzbek_number(num % 1_000)
    elif num < 1_000_000_000:
        return uzbek_number(num // 1_000_000) + ' million ' + uzbek_number(num % 1_000_000)
    elif num < 1_000_000_000_000:
        return uzbek_number(num // 1_000_000_000) + ' milliard ' + uzbek_number(num %
    1_000_000_000)
    else:
        return 'Xato raqam'

son = uzbek_number(656689221435)
print(son)