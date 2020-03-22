a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def get_mail(s):
	## 여기에 코딩을 해주세요
    b = s.split('@')
    # ['spartacodingclub', 'gmail.com']
    c = b[1].split('.')
    # ['gmail', 'com']
    return c[0]
#결과값
print(get_mail(a))

#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
	## 여기에 코딩을 해주세요
    b = {}
    for fruit in a_list:
        existed_fruit = b.get(fruit, 0)
        b[fruit] = existed_fruit + 1
    return b

#결과값
print(count_list(a))