t1 = (1, 2, 3, 4, 5, True, "Hello", 0)
t2 = (1, 5, True, "Hello", False)
t3 = (0.5, 99, True, "Hello")
print(f"1st tuple. {all(t1)}")
print(f"2nd tuple. {all(t2)}")
print(f"3rd tuple. {all(t3)}")