m, n = int(input()), int(input())
stud_spis = [input() for _ in range(m + n)]
stud_set = set(stud_spis)
stud_less2 = len(stud_spis) - len(stud_set)

if len(stud_set) - stud_less2 == 0:
    print("NO")
else:
    print(len(stud_set) - stud_less2)
