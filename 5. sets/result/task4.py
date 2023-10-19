m, n = int(input()), int(input())
mybook = {input() for i in range(m)}

for i in range(n):
    if input() in mybook:
        print("YES")
    else:
        print("NO")