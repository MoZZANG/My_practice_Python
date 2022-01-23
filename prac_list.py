subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호가 몇번째 칸에 타고 있는지
print(subway.index('조세호'))

# 하하가 다음 정류장에서 탐
subway.append('하하')
print(subway)

# 정형돈을 유재석과 조세호 사이에 태워 봄
subway.insert(1, '정형돈')
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# 지하철에 같은 이름 사람이 몇명타고 있는지
# subway.append('유재석')
# print(subway)
# print(subway.count('유재석'))

# 정렬도 가능
number = [5, 3, 2, 4, 1]
number.sort()
print(number)

#거꾸로
number.reverse()
print(number)

#모두 지욱
number.clear()
print(number)

#리스트 확장
num_list = [1, 2, 3, 4]
mix_list = ['조세호', 20, True]
num_list.extend(mix_list)
print(num_list)