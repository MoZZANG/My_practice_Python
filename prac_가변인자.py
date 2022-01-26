def profile(name, age, *langauge):
    print('이름 : {}, 나이 : {}'.format(name, age), end=" ")
    for lang in langauge:
        print(lang, end = " ")
    print()

profile('유재석', 20, 'Jave', 'python', 'lang1', 'lang2','lang3')
profile('김태호', 25, 'lang4', 'lang5')
print(profile)
    