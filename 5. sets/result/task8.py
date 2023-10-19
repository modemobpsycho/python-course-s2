m, n = int(input()), int(input())
math_stud = {input() for _ in range(m)}
inf_stud = {input() for _ in range(n)}

if len(math_stud - inf_stud) + len(inf_stud - math_stud) != 0:
    print(len(math_stud - inf_stud) + len(inf_stud - math_stud))
else:
    print("NO")