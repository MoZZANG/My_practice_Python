# 집합(set)
# 중복 안됨, 순서 없음
set = {1,2,3,3,3}
print(set)

java = {'유재석', '조세호', '김태호'}
python = {'유재석', '김종국'}

# 교집합 (java랑 python을 다 할 수 있는 사람)
print(java & python)

# 합집합 (java를 할 수 있거나 python을 할 수 있는 사람)
print(java | python)

# 차집합 (java는 할 수 있지만 python은 못하는 사람)
print(java - python)

#python 할 수 있는 사람이 늘어남
python.add('조세호')
print(python)

# java를 잊었어요.
java.remove('김태호')
print(java)