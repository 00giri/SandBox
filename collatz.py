a = int(input())

cnt = 0
num = [a]
while a != 1:
    cnt +=1
    if a%2:
        a *=3
        a+=1
    else:
        a //=2
    num.append(a)
num.sort()
print(num)
print(f"cnt:{cnt}")
