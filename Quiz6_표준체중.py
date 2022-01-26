# 모범답안(?)
# def std_weight(height, gender):
#     if gender == '남':
#         return height/100 * height/100 * 22
#     else:
#         return height/100 * height/100 * 21
    

# height = 175 # cm단위
# gender = '남'
# weight = round(std_weight(height, gender), 2)
# print('키 {}cm {}자의 표준체중은 {}kg 입니다.'.format(height, gender, weight))


#내가 한거
def std_weight(height, gender):
    if gender == '남':
        weight = height/100 * height/100 * 22
    else:
        weight =  height/100 * height/100 * 21
    print('키 {}cm {}자의 표준체중은 {}kg 입니다.'.format(height, gender, round(weight, 2)))

height = 175 # cm단위
gender = '남'
std_weight(height, gender)
