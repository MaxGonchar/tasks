# Дана строка. Провести с ней следующие манипуляции:
# выведите третий символ этой строки.
# выведите предпоследний символ этой строки.
# выведите первые пять символов этой строки.
# выведите всю строку, кроме последних двух символов.
# выведите все символы с четными индексами.
# выведите все символы с нечетными индексами строки.
# выведите все символы в обратном порядке.
# выведите все символы строки через один в обратном порядке, начиная с последнего.
# выведите длину данной строки.

s = 'I got sick of coming up with lines'

print(s[2])

print(s[-2])

print(s[0:5])

print(s[0:-2])

print(s[0::2])

print(s[1::2])

print(s[-1::-1])

print(s[-1::-2])

print(len(s))
