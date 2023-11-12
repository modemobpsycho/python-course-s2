students = []

for i in range(int(input())):
    students.append(any(['5' in input() for q in range(int(input()))]))


print("YES" if all(students) else "NO")
