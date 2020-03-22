# 여기는 주석 부분이예요
a = 3
b = 2
sparta_coding = 10
c = a + b
c = a - b
c = a * b
c = a / b
c = a % b

a = "Sparta Coding"
a = 10.3
a = True
b = False
a = [10, 'Sparta', True, 11]
b = {
    'Sparta': 10,
    "Coding": True
}
c = a[0]
d = b["Sparta"]

a = []
a.append(10)
# js에서는 a.push(10)
b = {}
b["sparta"] = 10
# b = {
#   "sparta" : 10
# }

# 반복문
# [JS]
# for(let i = 0; i < 10; i++) {
# }
for i in range(10):
    print(i)

# 조건문
# [JS]
# if (....) {
# }
if a > 10:
    print(a)
elif b > 10:
    print(b)
else:
    print(c)

# 함수
# [JS]
# function test {
# }
def test(a = 10):
    print(a)

test(20)


if a is not True:
    print(a)
else:
    print(b)

a = "10"
if a == 10:
    print(a)
else:
    print(b)


