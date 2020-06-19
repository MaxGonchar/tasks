# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.
# Используйте для решения задачи метод count.

s = '  I got sick of coming up with lines    '

print('quantity of words is ', s.strip().count(' ') + 1)
