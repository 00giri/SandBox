#2個の0,3個の1,4個の2をそれぞれ隣り合わないように並べたものを全列挙

ans = set()
fruits = {0:2, 1:3, 2:4}

def find(cnt, num, prev):
    if cnt == 9:
        global ans
        ans.add(prev)
    else:
        cnt += 1
        for i in range(3):
            if num[i] and (cnt == 1 or i != int(prev[-1])):
                num[i] -= 1
                find(cnt, num, prev+str(i))
                num[i] += 1

find(0, fruits, "")
print(f"Num of Case: {len(ans)}")
print(ans)
