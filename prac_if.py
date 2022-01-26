# weather = input('오늘 날씨는 어때요? ')
# if weather == '비' or weather == '눈':
#     print('우산을 챙기세요.')
# elif weather == '미세먼지':
#     print('마스크를 챙기세요.')
# else:
#     print('준비물이 필요없어요.')


temp = int(input('오늘의 기온은? ')) # 기온은 숫자지만 input은 항상 문자열로 값을 받기때문에
if temp < 0:
    print('날씨가 추우니 코트를 챙기세요.')
elif 0 <= temp < 20:
    print('날씨가 쌀쌀하니 겉옷을 챙기세요')
elif 20<= temp < 25:
    print('오늘은 기온이 적당해요')
else:
    print('오늘은 더워요')