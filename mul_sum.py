def mul_sum(a, b):
    mul = a * b
    if mul <= 1000:
        return mul
    else:
        return a + b
result = mul_sum(20, 30)
print("The result is", result)

result = mul_sum(40, 30)
print("The result is", result)




