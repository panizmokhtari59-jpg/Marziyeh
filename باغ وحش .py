# ۱. مقدمه بر شی‌گرایی (OOP Introduction)
class Animal:
    # ویژگی کلاس (zoo_name) - بخش ۳
    zoo_name = "باغ‌وحش تهران"
    
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    # ۲. ویژگی‌ها و کلاس‌ها (Attributes and Class Keyword)
    def make_sound(self):
        print(f"{self.name} می‌گوید: {self.sound}")
    
    # ۳. ویژگی‌های کلاس و متدها (Class Object Attributes and Methods)
    def info(self):
        print(f"نام: {self.name}")
        print(f"گونه: {self.species}")
        print(f"سن: {self.age} سال")
        print(f"صدای حیوان: {self.sound}")
        print(f"باغ‌وحش: {Animal.zoo_name}")
    
    # ۵. متدهای جادویی (Magic/Dunder Methods)
    def __str__(self):
        return f"حیوان: {self.name} | گونه: {self.species} | سن: {self.age} | صدا: {self.sound} | باغ‌وحش: {Animal.zoo_name}"


# ۴. ارث‌بری و چندریختی (Inheritance and Polymorphism)
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        # فراخوانی سازنده کلاس والد
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
    
    # بازنویسی متد make_sound (چندریختی)
    def make_sound(self):
        print(f"{self.name} (پرنده) آواز می‌خواند: {self.sound} چهچه چهچه")
    
    # بازنویسی متد info برای نمایش اطلاعات اضافی
    def info(self):
        super().info()
        print(f"اندازه بال: {self.wing_span} سانتی‌متر")
    
    # بازنویسی متد __str__
    def __str__(self):
        return f"پرنده: {self.name} | گونه: {self.species} | سن: {self.age} | اندازه بال: {self.wing_span} | باغ‌وحش: {Animal.zoo_name}"


# آزمایش کد
if __name__ == "__main__":
    print("=" * 50)
    print("بخش ۱ و ۲: ایجاد شیء شیر")
    print("=" * 50)
    
    # ایجاد شیء شیر
    lion = Animal("شیر", "پستاندار", 5, "غرّش")
    lion.make_sound()
    
    print("\n" + "=" * 50)
    print("بخش ۳: نمایش اطلاعات با متد info")
    print("=" * 50)
    
    lion.info()
    
    print("\n" + "=" * 50)
    print("بخش ۴: ارث‌بری و چندریختی (کلاس Bird)")
    print("=" * 50)
    
    # ایجاد شیء پرنده
    eagle = Bird("عقاب", "پرنده شکاری", 3, "جیر جیر", 180)
    eagle.make_sound()
    eagle.info()
    
    print("\n" + "=" * 50)
    print("بخش ۵: متد جادویی __str__")
    print("=" * 50)
    
    # نمایش با متد __str__
    print(lion)
    print(eagle)
    
    print("\n" + "=" * 50)
    print("ایجاد حیوانات بیشتر برای آزمایش")
    print("=" * 50)
    
    # ایجاد حیوانات بیشتر
    animals = [
        Animal("ببر", "پستاندار", 4, "خرخر"),
        Animal("فیل", "پستاندار", 10, "شیپور"),
        Bird("طوطی", "پرنده", 2, "سلام", 30),
        Bird("شترمرغ", "پرنده", 6, "صدای خاص", 200)
    ]
    
    for animal in animals:
        print(animal)
        animal.make_sound()
        print("-" * 30)