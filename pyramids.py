
# 1. Pyramid
print("Normal Pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f"{x:^10}")

# 2. Invert Pyramid
print("Invert Pyramid")
for i in range(5):
    x="*"
    x=x*(5-i)
    print(f"{x:^10}")

# 3. Left sided Pyramid
print("Left Sided Pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f"{x:<10}")

# 4. Right sided Pyramid
print("Right Sided Pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f"{x:>10}")
    