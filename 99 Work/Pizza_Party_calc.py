pizza = int(input("How many Pizzas coming? "))
students = int(input("How many students coming? "))
slices = int(pizza * 8)
slices_per_student = slices / students

print(f"Their are {slices} pizza slices and {students} students")

if slices_per_student >= 3:
    print("Pizza Overload!")
elif slices_per_student >= 2:
    print("Perfect amount of Pizza")
else:
    print("We need more pizza!!")
    