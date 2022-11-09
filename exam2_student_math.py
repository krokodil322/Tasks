
math, inf = int(input()), int(input())
students = {"".join(input()) for _ in range(inf + math)}
math, inf = {num for num in range(1, math + 1)}, {num for num in range(1, inf + 1)}
students = {num for num in range(1, len(students) + 1)}

student_only_math_inf = len(students.difference(math)) + len(students.difference(inf))
print(student_only_math_inf if student_only_math_inf != 0 else "NO")
