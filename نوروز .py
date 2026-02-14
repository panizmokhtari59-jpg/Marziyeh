import os
from twilio.rest import Client

# خواندن شماره‌ها از فایل
def read_phone_numbers(filename):
    phone_numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                number = line.strip()
                if number:  # جلوگیری از خطوط خالی
                    # فرمت کردن شماره به صورت بین‌المللی (با +)
                    if not number.startswith('+'):
                        if number.startswith('0'):
                            number = '+98' + number[1:]  # برای ایران
                        else:
                            number = '+' + number
                    phone_numbers.append(number)
        return phone_numbers
    except FileNotFoundError:
        print(f"خطا: فایل '{filename}' یافت نشد.")
        return []

# ارسال پیام تبریک
def send_nowruz_greetings(account_sid, auth_token, from_number, phone_numbers):
    if not phone_numbers:
        print("هیچ شماره‌ای برای ارسال وجود ندارد.")
        return
    
    client = Client(account_sid, auth_token)
    
    message_body = """
🎉 عید نوروز مبارک! 🌸
نوروزتان پیروز، سالی پر از سلامتی، شادی و موفقیت داشته باشید.
بهار طبیعت، بهار زندگی‌تان باد!
با بهترین آرزوها 🌺
"""
    
    success_count = 0
    failed_numbers = []
    
    for number in phone_numbers:
        try:
            message = client.messages.create(
                body=message_body.strip(),
                from_=from_number,
                to=number
            )
            print(f"✅ پیام به {number} ارسال شد. (ID: {message.sid})")
            success_count += 1
        except Exception as e:
            print(f"❌ خطا در ارسال به {number}: {str(e)}")
            failed_numbers.append(number)
    
    print(f"\n📊 گزارش نهایی:")
    print(f"تعداد ارسال موفق: {success_count}")
    print(f"تعداد ارسال ناموفق: {len(failed_numbers)}")
    if failed_numbers:
        print(f"شماره‌های ناموفق: {', '.join(failed_numbers)}")

# بخش اصلی برنامه
def main():
    # اطلاعات Twilio (باید از محیط یا فایل تنظیمات خوانده شود)
    # برای امنیت بهتر، از متغیرهای محیطی استفاده می‌شود
    ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    FROM_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
    
    # اگر متغیرهای محیطی تنظیم نشده‌اند
    if not all([ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER]):
        print("لطفاً ابتدا متغیرهای محیطی Twilio را تنظیم کنید:")
        print("""
        در لینوکس/Mac:
        export TWILIO_ACCOUNT_SID='your_account_sid'
        export TWILIO_AUTH_TOKEN='your_auth_token'
        export TWILIO_PHONE_NUMBER='your_twilio_number'
        
        در ویندوز (PowerShell):
        $env:TWILIO_ACCOUNT_SID='your_account_sid'
        $env:TWILIO_AUTH_TOKEN='your_auth_token'
        $env:TWILIO_PHONE_NUMBER='your_twilio_number'
        """)
        
        # ورودی دستی برای تست (در محیط واقعی استفاده نکنید)
        use_test_mode = input("آیا می‌خواهید در حالت تست بدون ارسال واقعی ادامه دهید؟ (y/n): ").lower()
        if use_test_mode == 'y':
            print("\n🔶 حالت تست فعال شد - پیام‌ها واقعاً ارسال نمی‌شوند")
            # ایجاد شماره‌های تستی
            test_numbers = [
                "+989121234567",
                "+989123456789",
                "+989125678901",
                "+989127890123",
                "+989129012345"
            ]
            # ذخیره شماره‌های تست در فایل
            with open('phone_numbers.txt', 'w', encoding='utf-8') as f:
                for num in test_numbers:
                    f.write(num + '\n')
            print("فایل 'phone_numbers.txt' با شماره‌های نمونه ایجاد شد.")
            print("\n📝 محتوای پیام تبریک:")
            message = """
            🎉 عید نوروز مبارک! 🌸
            نوروزتان پیروز، سالی پر از سلامتی، شادی و موفقیت داشته باشید.
            بهار طبیعت، بهار زندگی‌تان باد!
            با بهترین آرزوها 🌺
            """
            print(message.strip())
            return
    
    # نام فایل حاوی شماره‌ها
    FILENAME = "phone_numbers.txt"
    
    # خواندن شماره‌ها از فایل
    phone_numbers = read_phone_numbers(FILENAME)
    
    if len(phone_numbers) < 3:
        print(f"خطا: حداقل ۳ شماره در فایل '{FILENAME}' لازم است.")
        print(f"تعداد شماره‌های یافت شده: {len(phone_numbers)}")
        print("لطفاً فایل را با فرمت زیر ایجاد کنید:")
        print("""
        09121234567
        09123456789
        09125678901
        """)
        return
    
    print(f"✅ تعداد {len(phone_numbers)} شماره از فایل خوانده شد.")
    
    # تایید قبل از ارسال
    print("\n📋 لیست شماره‌ها:")
    for i, number in enumerate(phone_numbers, 1):
        print(f"{i}. {number}")
    
    confirm = input(f"\nآیا می‌خواهید پیام تبریک به {len(phone_numbers)} شماره ارسال شود؟ (y/n): ")
    
    if confirm.lower() == 'y':
        send_nowruz_greetings(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, phone_numbers)
    else:
        print("ارسال لغو شد.")

if __name__ == "__main__":
    main()