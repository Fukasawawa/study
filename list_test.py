import numpy as np
'''
list = np.array([['aaaaa', 100, '朝', '春'],
        ['bbbbb', 100, '朝', '夏'],
        ['ccccc', 500, '昼', '春'],
        ['ddddd', 500, '夜', '秋'],
        ['eeeee', 1000, '昼', '冬'],
        ['aaaaa', 1000, '夜', '夏']])
#追加データ
add = [input()]
add.append(int(input()))
add.append(input())
add.append(input())

#add = ['text', 500, '朝', '冬']

#配列にそのデータがなければ
if(np.any(list==add[0]) == False):
    #データ追加
    list = np.insert(list, 0, add, axis=0)
print(list)
'''

#list = np.array([])
list = np.array([['あんこ', 'aaaa', 'aaaa', 'aaa']])
list = np.insert(list, 1, ['1asf', '5', '3', 'A'], axis=0)
list = np.insert(list, 1, ['あんこ', '35', '6','ASD'], axis=0)
add = ['aaa', 'かｓ', 'わか', 'ああ']
list = np.insert(list, 1, add, axis=0)
print(np.delete(list, 0, 0))

'''
list = [["aaa", "aaa", "aaa", "aaa"]]
add = ["bbb", "bbb", "bbb"]
add.append("bbb")
list.append(add)
if((list in ["aaa"]) == True):
    print(list)
else:
    print("zannnenn")
'''

'''
day = '2018年5月12日 20:01'
a = day.split('年')[1].split('月')[0]#.split('日').split(' ').split(':')
b = day.split(' ')[1].split(':')[0]
print(a, b, int(a)+int(b))
'''

'''
print(list)
#print(list, 'aaaaa' in list)
print(np.any(list==['aaaaa']))

r = np.where(list[:, 0]=='fffff')
#r = np.any(['aaaaa'])
print(r)
print(r[0, 0])
'''
