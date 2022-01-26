# def profile(name, age, main_lang):
#     print('name : {}, age : {}, main_lang : {}'.format(name, age, main_lang))

# profile('유재석', 20, '파이썬')
# profile('김태호', 25, '자바')


def profile(name, age = 17, main_lang = 'java'):
    print('name : {}\tage : {}\tmain_lang : {}'.format(name, age, main_lang))

profile('유재석')
profile('김태호')