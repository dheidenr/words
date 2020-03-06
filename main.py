import numpy as np
import pandas as pd
import codecs as cd

print('Hello')

data = pd.read_csv('/Users/dheidenr/PycharmProjects/worls/russian_utf8.txt', sep='\n')
print(data)
print(len(data))
print(data.info())
print(data.columns)
print(data.index)
print(data[(data['привет'] == 'п')])

print('data.values[0][0][0]', data.values[0][0][0])
print('data.values.shape', data.values.shape)

# for ch in data.values:
#     if ch[0][0] == 'п':
#         print(ch)



# print(data[data == 'п'] and data[data[0][1] == 'р'] and data[data[0][2] == 'и'])

# # create utf-8
# f = cd.open('russian_surnames.txt', 'r', 'cp1251')
# u = f.read()
# out = cd.open('russian_surnames_utf8.txt', 'w', 'utf-8')
# out.write(u)

#  d.decode('cp1251').encode('utf8')

