a = "abc"
# str
a = list(a)
# list
a = ''.join(a)
# str
a = bytes(a, encoding='utf-8')
# bytes
a = str(a, encoding='utf-8')
# str
print(a)
print(type(a))

some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list, start=2):
    mapping[v] = i
print(mapping)
# enumberate函数

mapping1 = {}
for i, v in enumerate(some_list):
    mapping1[v] = i
print(mapping1)
# enumberate函数

seq1 = ['one', 'two', 'three']
zipped = zip(some_list, seq1)
print(list(zipped))
# zip组合函数，将多个列表、元组或其他序列成对组合成一个元组列表

seq2 = [True, False]
print(list(zip(some_list, seq1, seq2)))
# zip元素个数取决于最短的序列

for i, (a, b) in enumerate(zip(some_list, seq1)):
    print('{0}: {1}, {2}'. format(i, a, b))
# zip与enumberate

name_list = [('Chris', 'Jay'), ('Jaguar', 'Benz'), ('BMW', 'Audi')]
first_names, last_names = zip(*name_list)
print('Zip解压：\n', first_names, last_names)
# *zip的解压

a1 = [5, 4, 9, 10, 5, 8, 9, 12]
a1.sort()
print('a1:\n', a1)
# .sort()直接返回原list
a2 = sorted(a1)
print('a2:\n', a2)
print('list4-6:\n', a1[3:6])

a3 = ['saw', 'small', 'as', 'asda', 'he', 'one']
a3.sort(key=len)
print('sort词组长度排序：\n', a3)

print('sorted字符排序：\n', sorted('undertaker boom'))
# 字符排序

print('reversed逆迭代：\n', list(reversed(range(15))))
# reversed从后向前迭代

empty_dict = {}
d1 = {'a': 'some values', 'b': [1, 2, 3, 4, 5]}
d1['a'] = [1]
d1['c'] = 'an integer'
print('字典选择元素：\n', d1['a'])

d1['d'] = 'some values'
d1[5] = 'dummy variable'
del d1[5]
print('del删除关键值：\n', d1)

ret = d1.pop('d')
print('pop删除关键值：\n', d1)

print(list(d1.keys()))
print(list(d1.values()))
d1.update({'b': 'foo', 7: 12})
print('update:函数:\n', d1)

mapping2 = {}
key_list = ['value', 'pop', 9]
value_list = [1, 'str', 'maps']
for key, value in zip(key_list, value_list):
    mapping2[key] = value
print('mapping2组合序列为字典：\n', mapping2)

words =['apple', 'orange', 'pineapple', 'pen', 'atom', 'corn']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)

by_letter2 = {}
for word in words:
    letter2 = word[0]
    by_letter2.setdefault(letter2, []).append(word)
print('by_letter2:\n', by_letter2)

from collections import defaultdict
by_letter1 = defaultdict(list)
for word in words:
    by_letter1[word[0]].append(word)
print('by_letter1:\n', by_letter1)
# 根据首字建立索引

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print('两种合并取两集合中不重复的元素的方法：', a.union(b), a | b)

print('两种取两集合中交集的方法：', a.intersection(b), a & b)

strings = ['a', 'b', 'c', 'as', 'van', 'python']
X = [x.upper() for x in strings if len(x) > 2]
print(X)

unique_lengths = {len(x) for x in strings}
print(unique_lengths)
mapping3 = set(map(len, strings))
print(mapping3)


strings1 = [['a', 'b', 'c', 'as', 'van', 'python']]
names_of_interest = []
for names in strings1:
    enough_es = [name for name in names if name.count('a') >= 1]
    names_of_interest.extend(enough_es)
print(names_of_interest)

result = [name for names in strings1 for name in names if name.count('a') >= 1]
print(result)

states = ['   Alabama	',	'Georgia!',	'Georgia',	'georgia',	'FlOrIda', 'south carolina##',	'West virginia?']

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

print(clean_strings(states))

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

print('函数修改字段：', clean_strings(states, clean_ops))

for x in map(remove_punctuation, states):
    print(x)

def squares(n=10):
    print('Generating squares from 1 to {0}')
    for i in range(1, n+1):
        yield i ** 2
gen = squares()
for x in gen:
    print(x, end='')

gen = (x ** 2 for x in range(100))
for x in gen:
    print(x, end='')

x1 = sum(x ** 2 for x in range(100))
for

dict1 = dict((i, i ** 2) for i in range(5))
for i in dict1:
    print(i)
