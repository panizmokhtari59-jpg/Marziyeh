# وارد کردن کتابخانه‌های مورد نیاز
import random
import matplotlib.pyplot as plt
import numpy as np

# قدم اول: شبیه‌سازی پرتاب تاس

# تعداد پرتاب‌ها
num_throws = 10000

# لیست 6 عضوی برای نگهداری تعداد دفعات آمدن هر عدد
counts = [0] * 6

# شبیه‌سازی پرتاب تاس
print(f"در حال شبیه‌سازی {num_throws} پرتاب تاس...")
for i in range(num_throws):
    # تولید عدد تصادفی بین 1 تا 6
    dice_roll = random.randint(1, 6)
    # افزایش شمارنده مربوطه
    counts[dice_roll - 1] += 1

    # نمایش پیشرفت برای پرتاب‌های بزرگ
    if num_throws >= 10000 and (i+1) % 2000 == 0:
        print(f"  {i+1} پرتاب انجام شد...")

print("شبیه‌سازی کامل شد!\n")

# محاسبه فراوانی نسبی
frequencies = [count / num_throws for count in counts]

# نمایش نتایج
print("نتایج شبیه‌سازی:")
print("-" * 40)
print(f"تعداد کل پرتاب‌ها: {num_throws:,}")
print()
for i in range(6):
    print(f"عدد {i+1}: {counts[i]:,} بار ({frequencies[i]*100:.2f}%)")
print("-" * 40)

# محاسبه انحراف از مقدار مورد انتظار
expected_probability = 1/6
expected_count = num_throws / 6
deviations = [abs(count - expected_count) for count in counts]
max_deviation = max(deviations)
max_deviation_percent = (max_deviation / expected_count) * 100

print(f"\nتعداد مورد انتظار برای هر عدد: {expected_count:,.1f}")
print(f"بیشترین انحراف از مقدار مورد انتظار: {max_deviation:.1f} ({max_deviation_percent:.2f}%)")

# قدم دوم: رسم نمودار با matplotlib

# ایجاد نمودار با دو زیرنمودار
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# نمودار ۱: نمودار میله‌ای تعداد مطلق
numbers = [1, 2, 3, 4, 5, 6]
ax1.bar(numbers, counts, color='skyblue', edgecolor='black', alpha=0.7)
ax1.axhline(y=expected_count, color='red', linestyle='--', linewidth=2, label=f'مقدار مورد انتظار: {expected_count:.0f}')
ax1.set_xlabel('عدد تاس', fontsize=12)
ax1.set_ylabel('تعداد دفعات', fontsize=12)
ax1.set_title(f'تعداد دفعات آمدن هر عدد در {num_throws:,} پرتاب', fontsize=14, fontweight='bold')
ax1.set_xticks(numbers)
ax1.grid(axis='y', alpha=0.3)
ax1.legend()

# افزودن مقادیر روی میله‌ها
for i, count in enumerate(counts):
    ax1.text(i+1, count + (0.01 * max(counts)), f'{count:,}', ha='center', va='bottom', fontsize=10)

# نمودار ۲: نمودار میله‌ای درصدها
ax2.bar(numbers, frequencies, color='lightcoral', edgecolor='black', alpha=0.7)
ax2.axhline(y=expected_probability, color='red', linestyle='--', linewidth=2, label=f'احتمال مورد انتظار: {expected_probability*100:.2f}%')
ax2.set_xlabel('عدد تاس', fontsize=12)
ax2.set_ylabel('فراوانی نسبی', fontsize=12)
ax2.set_title(f'فراوانی نسبی هر عدد در {num_throws:,} پرتاب', fontsize=14, fontweight='bold')
ax2.set_xticks(numbers)
ax2.grid(axis='y', alpha=0.3)
ax2.legend()

# افزودن مقادیر روی میله‌ها
for i, freq in enumerate(frequencies):
    ax2.text(i+1, freq + 0.005, f'{freq*100:.2f}%', ha='center', va='bottom', fontsize=10)

# تنظیمات کلی
plt.suptitle('تحلیل آماری پرتاب تاس: بررسی یکنواختی احتمال اعداد', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

# نمایش نمودار
plt.show()

# نمودار ۳: نمودار خطی برای نمایش همگرایی به سمت مقدار مورد انتظار
print("\nدر حال ایجاد نمودار همگرایی...")

# شبیه‌سازی مرحله‌ای برای نمایش همگرایی
step_size = 100 if num_throws > 1000 else 10
steps = list(range(step_size, num_throws + 1, step_size))
if num_throws % step_size != 0:
    steps.append(num_throws)

# ایجاد لیست برای ذخیره نتایج مرحله‌ای
convergence_data = {i: [] for i in range(6)}

# شبیه‌سازی مرحله‌ای
current_counts = [0] * 6
for throw_num in range(1, num_throws + 1):
    dice_roll = random.randint(1, 6)
    current_counts[dice_roll - 1] += 1
    
    # ذخیره نتایج در نقاط مشخص
    if throw_num in steps:
        for i in range(6):
            convergence_data[i].append(current_counts[i] / throw_num)

# ایجاد نمودار همگرایی
plt.figure(figsize=(12, 6))
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
for i in range(6):
    plt.plot(steps, convergence_data[i], label=f'عدد {i+1}', color=colors[i], linewidth=2, alpha=0.8)

plt.axhline(y=expected_probability, color='black', linestyle='--', linewidth=2, label=f'احتمال مورد انتظار: {expected_probability:.4f}')
plt.xlabel('تعداد پرتاب‌ها', fontsize=12)
plt.ylabel('فراوانی نسبی', fontsize=12)
plt.title('همگرایی فراوانی نسبی به سمت مقدار مورد انتظار با افزایش تعداد پرتاب‌ها', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.xscale('log')  # استفاده از مقیاس لگاریتمی برای نمایش بهتر
plt.tight_layout()

plt.show()

# تحلیل نتایج و نتیجه‌گیری
print("\n" + "="*60)
print("تحلیل نتایج و نتیجه‌گیری:")
print("="*60)

# محاسبه انحراف معیار
std_dev = np.std(frequencies)
print(f"\nانحراف معیار فراوانی نسبی: {std_dev:.6f}")

# آزمون کای-دو برای بررسی یکنواختی
chi_square = sum([(count - expected_count)**2 / expected_count for count in counts])
print(f"مقدار آماره کای-دو: {chi_square:.4f}")

# درجه آزادی = 6-1 = 5
# مقدار بحرانی کای-دو با درجه آزادی 5 و سطح معناداری 0.05 ≈ 11.07
critical_value_95 = 11.07
critical_value_99 = 15.09

print(f"\nمقدار بحرانی کای-دو (درجه آزادی=5):")
print(f"  - سطح اطمینان 95%: {critical_value_95:.2f}")
print(f"  - سطح اطمینان 99%: {critical_value_99:.2f}")

if chi_square < critical_value_95:
    print(f"\n✅ نتیجه: مقدار کای-دو ({chi_square:.4f}) از مقدار بحرانی 95% ({critical_value_95:.2f}) کمتر است.")
    print("   بنابراین، با اطمینان 95% می‌توان گفت که تاس منصفانه است و احتمال آمدن همه اعداد برابر است.")
elif chi_square < critical_value_99:
    print(f"\n⚠️ نتیجه: مقدار کای-دو ({chi_square:.4f}) بین مقادیر بحرانی 95% و 99% قرار دارد.")
    print("   بنابراین، با اطمینان 95% تاس منصفانه نیست، اما با اطمینان 99% نمی‌توان این ادعا را کرد.")
else:
    print(f"\n❌ نتیجه: مقدار کای-دو ({chi_square:.4f}) از مقدار بحرانی 99% ({critical_value_99:.2f}) بیشتر است.")
    print("   بنابراین، با اطمینان 99% می‌توان گفت که تاس منصفانه نیست.")

print(f"\nمشاهده بصری: با نگاه به نمودارها می‌بینیم که:")
print(f"  1. درصد هر عدد به حدود {expected_probability*100:.2f}% نزدیک است.")
print(f"  2. بیشترین انحراف از مقدار مورد انتظار {max_deviation_percent:.2f}% است.")
print(f"  3. با افزایش تعداد پرتاب‌ها (نمودار همگرایی)، مقادیر به سمت احتمال نظری همگرا می‌شوند.")

print("\n" + "="*60)