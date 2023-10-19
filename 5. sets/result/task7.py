m, n = int(input()), int(input())
math_stud = {input() for _ in range(m)}
inf_stud = {input() for _ in range(n)}

print(len(math_stud - inf_stud))