url = 'http://naver.com'
rule1 = url.replace('http://', "")
# print(rule1)
rule2 = rule1[:5]
# print(rule2)
password = rule2[:3] + str(len(rule2)) + str(url.count('e')) + "!"
print(password)

print('----------')
# 모범답안
url = 'http://naver.com'
url = 'http://goolge.com'
rule1 = url.replace('http://', "")
rule2 = rule1[:rule1.index('.')] # 처음부터 rule1의 '.' 까지 출력
password = rule2[:3] + str(len(rule2)) + str(rule1.count('e')) + "!"
print('{0}의 비밀번호는 {1}입니다.'.format(url, password))