# وارد کردن کتابخانه‌های لازم
import random
import matplotlib.pyplot as plt

# قدم اول: تولید اعداد تاس و نگهداری نتایج

# تعداد دفعات پرتاب تاس
num_rolls = 10000

# ایجاد لیست 6 عضوی برای شمارش نتایج (همه مقادیر ابتدا صفر هستند)
# اندیس 0 مربوط به عدد 1 تاس است، اندیس 1 مربوط به عدد 2 تاس و به همین ترتیب
results = [0] * 6

# شبیه‌سازی پرتاب تاس
for i in range(num_rolls):
    # تولید یک عدد تصادفی بین 1 تا 6
    roll = random.randint(1, 6)
    # افزایش شمارنده مربوط به آن عدد
    results[roll - 1] += 1

# محاسبه فراوانی نسبی (احتمال تجربی)
probabilities = [count / num_rolls for count in results]

# نمایش نتایج خام
print("نتایج شبیه‌سازی پرتاب تاس:")
print("=" * 50)
for i in range(6):
    print(f"عدد {i+1}: {results[i]} بار ({probabilities[i]*100:.2f}%)")
print("=" * 50)
print(f"مجموع پرتاب‌ها: {sum(results)}")
print(f"احتمال مورد انتظار برای هر عدد: {100/6:.2f}%")

# قدم دوم: رسم نمودار با matplotlib

# ایجاد نمودار با دو زیرنمودار (ساب‌پلات)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# نمودار 1: نمودار میله‌ای فراوانی مطلق
numbers = ['1', '2', '3', '4', '5', '6']
bars1 = ax1.bar(numbers, results, color='skyblue', edgecolor='black')

# اضافه کردن مقادیر روی نمودار میله‌ای
for bar, count in zip(bars1, results):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 30,
             f'{count}', ha='center', va='bottom', fontweight='bold')

ax1.set_xlabel('عدد تاس', fontsize=12)
ax1.set_ylabel('تعداد پرتاب‌ها', fontsize=12)
ax1.set_title(f'توزیع فراوانی مطلق اعداد تاس\n(تعداد کل پرتاب‌ها: {num_rolls})', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# نمودار 2: نمودار میله‌ای فراوانی نسبی (احتمال تجربی)
expected_probability = 1/6  # احتمال نظری هر عدد
expected_line = [expected_probability * 100] * 6

bars2 = ax2.bar(numbers, probabilities, color='lightcoral', edgecolor='black', alpha=0.7)
ax2.axhline(y=expected_probability * 100, color='green', linestyle='--', linewidth=2, label=f'احتمال نظری: {expected_probability*100:.2f}%')

# اضافه کردن مقادیر روی نمودار میله‌ای
for bar, prob in zip(bars2, probabilities):
    height = bar.get_height() * 100  # تبدیل به درصد
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height:.2f}%', ha='center', va='bottom', fontweight='bold')

ax2.set_xlabel('عدد تاس', fontsize=12)
ax2.set_ylabel('احتمال (%)', fontsize=12)
ax2.set_title('احتمال تجربی اعداد تاس در مقایسه با احتمال نظری', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# تنظیمات کلی نمودار
plt.suptitle('بررسی توزیع احتمال اعداد تاس با شبیه‌سازی', fontsize=16, fontweight='bold')
plt.tight_layout()

# نمایش نمودار
plt.show()

# تحلیل نتایج
print("\n" + "=" * 60)
print("تحلیل نتایج:")
print("=" * 60)

# محاسبه انحراف از مقدار مورد انتظار
deviations = []
for i in range(6):
    expected = num_rolls / 6
    deviation = abs(results[i] - expected) / expected * 100
    deviations.append(deviation)
    print(f"انحراف عدد {i+1} از مقدار مورد انتظار: {deviation:.2f}%")

print(f"\nمیانگین انحراف: {sum(deviations)/len(deviations):.2f}%")

# نتیجه‌گیری
print("\n" + "=" * 60)
print("نتیجه‌گیری:")
print("=" * 60)
print("با توجه به نتایج شبیه‌سازی:")
print(f"1. احتمال تجربی هر عدد تقریباً نزدیک به احتمال نظری ({100/6:.2f}%) است.")
print("2. انحراف‌های مشاهده شده عمدتاً ناشی از ماهیت تصادفی پرتاب تاس است.")
print("3. با افزایش تعداد پرتاب‌ها (مثلاً به ۱۰۰٬۰۰۰ بار)، این انحراف‌ها کوچک‌تر می‌شوند.")
print("\n✅ نتیجه: احتمال آمدن اعداد مختلف تاس در عمل نیز تقریباً برابر است و تاس استاندارد می‌باشد.")