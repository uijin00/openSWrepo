def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

n1 = float(input("첫 번째 정수를 입력하세요 : "))
n2 = float(input("두 번째 정수(0을 제외한 정수)를 입력하세요 : "))

print("덧셈 : ", add(n1, n2), ", " "뺄셈 : ", sub(n1, n2))
print("곱셈 : ", mul(n1, n2), ", " "나눗셈 : ", div(n1, n2))