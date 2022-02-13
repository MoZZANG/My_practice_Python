# print('자바', '파이썬', '스크립트', sep="vs")
# print('자바', '파이썬', '스크립트', sep="vs", end="?")
# print('뭐가 더 재밌니?')

# 시험성적
# scores = {'수학' : 0, '영어' : 50, '코딩' : 100}
# for subject, score in scores.items():
#     print(subject.ljust(6), str(score).rjust(4), sep=" : ")


#대기번호
# 001, 002, 003 ...
for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))

## input으로 값을 받으면 모두 str 타입으로 받게되는 것이다!