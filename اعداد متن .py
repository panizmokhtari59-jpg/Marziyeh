import re

def sum_numbers_in_file(filename):
    """
    اعداد را از فایل متنی استخراج کرده و جمع می‌زند
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # الگوی regex برای تشخیص اعداد
        pattern = r'\b\d+(?:\.\d+)?\b'
        numbers = re.findall(pattern, content)
        
        print(f"تعداد اعداد یافت شده: {len(numbers)}")
        print(f"اعداد: {numbers}")
        
        total = 0.0
        for i, num_str in enumerate(numbers, 1):
            num = float(num_str)
            total += num
            print(f"{i}: {num_str} -> {num}")
        
        return total
        
    except FileNotFoundError:
        print(f"خطا: فایل '{filename}' یافت نشد.")
        return None
    except Exception as e:
        print(f"خطا در پردازش فایل: {e}")
        return None

# اجرای برنامه
result = sum_numbers_in_file("tigers.txt")
if result is not None:
    print(f"\nمجموع تمام اعداد: {result}")
    print(f"مجموع (گرد شده): {round(result, 2)}")