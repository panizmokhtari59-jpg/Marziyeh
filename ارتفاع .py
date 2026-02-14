def skyline(*args):
    # اگر هیچ ارتفاعی داده نشده بود، صفر برگردان
    if not args:
        return 0
    # در غیر این صورت، بلندترین ارتفاع را برگردان
    return max(args)
numbers = list(map(int, input().split()))
print(skyline(*numbers))