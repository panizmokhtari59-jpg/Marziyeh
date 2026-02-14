def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
    # دریافت اعداد از کاربر (با فاصله جدا کنید)
numbers = list(map(int, input().split()))
print(sum_numbers(*numbers))