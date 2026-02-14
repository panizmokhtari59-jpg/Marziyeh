def b_m_m(a,b):
    while a != b :
        if a>b :
            a=a-b
        else:
            b=b-a
    return a
num1=18
num2=12
result=b_m_m(num1,num2)
print(f"({num1},{num2})={result}")
        