def f1():
    for i in range(1, 100):
        a = i
        cnt = 0
        while a != 1:
            cnt +=1
            if a%2:
                a *=3
                a+=1
            else:
                a //=2
        print(f"{i}:{cnt}")
def f2(r):
    maxi = -1
    for i in range(1, r):
        a = i
        cnt = 0
        while a != 1:
            cnt +=1
            if a%2:
                a *=3
                a+=1
            else:
                a //=2
        if maxi < cnt:
            maxi = cnt
            print(i)

f2(100000)
