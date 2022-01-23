from random import *
id = range(1, 21) # 1부터 21직전까지
# print(type(id))
id = list(id)
shuffle(id)
winners = sample(id, 4)


print('-- 당첨자 발표--')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('-- 축하합니다--')
