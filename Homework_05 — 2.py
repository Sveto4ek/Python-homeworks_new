# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

f = open('file_02')
lines = f.readlines()
print(f'В файле {len(lines)} строк(-и)')
for i, st in enumerate(lines):
    words = st.count(' ', 0, len(st))+1
    print(f'В строке {i+1} количество слов - {words}')
f.close()
