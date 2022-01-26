# customer = "토르"
# index = 5
# while index >=1:
#     print("{}, 주문하신 메뉴 나왔습니다. {}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print('주문하신 메뉴가 폐기되었습니다.')

customer = '토르'
person = 'Unknown'

while person != customer:
    print("{}님, 주문하신 메뉴 나왔습니다.".format(customer))
    person = input('이름이 어떻게 되세요?')