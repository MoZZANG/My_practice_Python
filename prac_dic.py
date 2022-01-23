cabinet = {'A-1' : '유재석', 'B-3' : '조세호'} 
# print(cabinet['A-1'])
# print(cabinet.get('C-2', "사용가능"))
# print(cabinet.get('A-1', "사용중")) # 안된다.

# print('A-1' in cabinet)
# print('C-2' in cabinet)

#새 손님
cabinet['C-5'] = '김종국'
print(cabinet)

#간 손님
del cabinet['A-1']
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# 모두 출력
print(cabinet.items())

# 목욕탕  폐점
cabinet.clear()
print(cabinet)