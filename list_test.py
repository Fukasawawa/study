import numpy as np

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
print(list)
#print(list, 'aaaaa' in list)
print(np.any(list==['aaaaa']))

r = np.where(list[:, 0]=='fffff')
#r = np.any(['aaaaa'])
print(r)
print(r[0, 0])
'''
