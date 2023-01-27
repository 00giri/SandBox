def f(num, num2, u, d):
    if len(d) == 5:
        global ans1
        global ans2
        ans1.append("".join(map(str, u)))
        ans2.append("".join(map(str, d)))
        return
    memo = num2.copy()
    for i in memo:
        num.discard(i)
        num2.discard(i)
        if len(d) == 0:
            f(num, num2, u, [i])
        else:
            tmp = d[-1]+i
            if tmp in num:
                btmp = tmp in num2
                num.discard(tmp)
                num2.discard(tmp)
                f(num, num2, u+[tmp], d+[i])
                num.add(tmp)
                if btmp: num2.add(tmp)
        num.add(i)
        num2.add(i)

ans1 = []
ans2 = []
f({i for i in range(1, 10)}, {i for i in range(1, 9)}, [], [])
for i in range(len(ans1)):
    print(f"{ans1[i]}:{ans2[i]}")
