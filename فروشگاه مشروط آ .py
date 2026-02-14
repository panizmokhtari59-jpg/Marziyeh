# دریافت مبلغ خرید از کاربر
amount = int(input("مبلغ خرید را وارد کنید (تومان): "))

if amount > 50000:
    discount = amount * 0.20
    final_amount = amount - discount
    print(f"مبلغ نهایی پس از ۲۰٪ تخفیف: {final_amount} تومان")
elif 20000 <= amount <= 50000:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"مبلغ نهایی پس از ۱۰٪ تخفیف: {final_amount} تومان")
else:
    print(f"مبلغ نهایی (بدون تخفیف): {amount} تومان")