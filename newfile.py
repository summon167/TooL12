import os
import time
import sys
import random
import socket 
import string 
from collections import deque

# --- الإعدادات والثوابت ---
MY_NAME = "ILYASS ADARBAZ"
TOOL_NAME = "TooL12"

# قائمة الألوان ANSI للترمينال
COLORS = [
    "\033[91m",  # أحمر
    "\033[92m",  # أخضر
    "\033[93m",  # أصفر
    "\033[94m",  # أزرق
    "\033[95m",  # بنفسجي
    "\033[96m",  # سماوي
    "\033[0m"    # إعادة ضبط اللون (ضروري في النهاية)
]
HEADER_COLOR_RESET = "\033[0m"
MENU_COLOR = "\033[97m" # أبيض ساطع
PROMPT_COLOR = "\033[93m" # أصفر
ERROR_COLOR = "\033[91m" # أحمر
INFO_COLOR = "\033[96m"  # سماوي
SUCCESS_COLOR = "\033[92m" # أخضر

# لتخزين أحدث 20 سطرًا من الإخراج (للتحديث السلس للشاشة الرئيسية)
output_buffer = deque(maxlen=20)

# --- وظائف مساعدة للواجهة ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header_only(name_color_index):
    # وظيفة لطباعة الرأس فقط دون مسح الشاشة بالكامل
    # تستخدم عند الحاجة لتحديث بسيط أو في بداية الأداة
    print(f"{COLORS[name_color_index]}############################################{HEADER_COLOR_RESET}")
    print(f"{COLORS[name_color_index]}  {MY_NAME} - {TOOL_NAME} (Cybersecurity Toolkit)   {HEADER_COLOR_RESET}")
    print(f"{COLORS[name_color_index]}############################################{HEADER_COLOR_RESET}")
    print("\n")

def add_to_buffer(message, color=MENU_COLOR):
    output_buffer.append(f"{color}{message}{HEADER_COLOR_RESET}")

def display_main_menu(name_color_index):
    clear_screen()
    print_header_only(name_color_index) # طباعة الرأس
    
    # تفريغ وعرض محتوى الـ buffer (للقائمة الرئيسية)
    for line in output_buffer:
        print(line)
    output_buffer.clear() # مسح الـ buffer بعد العرض
    print("\n")

def populate_menu_buffer():
    # تقوم هذه الوظيفة بملء الـ buffer بالقائمة الرئيسية
    add_to_buffer(f"{MENU_COLOR}اختر أداة من القائمة:")
    add_to_buffer(f"{MENU_COLOR}1. فحص المنافذ (Port Scanner)")
    add_to_buffer(f"{MENU_COLOR}2. تحليل الثغرات (Vulnerability Analyzer)")
    add_to_buffer(f"{MENU_COLOR}3. مولد كلمات المرور (Password Generator)")
    add_to_buffer(f"{MENU_COLOR}4. أداة التشفير/فك التشفير (Encryption/Decryption Tool)")
    add_to_buffer(f"{MENU_COLOR}5. أداة الهندسة العكسية (Reverse Engineering Tool)")
    add_to_buffer(f"{MENU_COLOR}6. الخروج")
    add_to_buffer("") 

# --- وظائف أدوات الأمن السيبراني (تم تصحيح الأخطاء بها) ---

# 1. فحص المنافذ (Port Scanner)
def port_scanner(name_color_index):
    clear_screen() # امسح الشاشة تمامًا قبل بدء الأداة
    print_header_only(name_color_index) # اطبع الرأس
    print(f"{INFO_COLOR}--- تشغيل: فحص المنافذ ---")
    
    print(f"{PROMPT_COLOR}أدخل عنوان IP أو اسم المضيف (مثال: scanme.nmap.org): {HEADER_COLOR_RESET}", end='')
    target = input()
    
    print(f"{PROMPT_COLOR}أدخل المنافذ المراد فحصها (مثال: 20-80 أو 21,22,80): {HEADER_COLOR_RESET}", end='')
    port_range_str = input()

    ports_to_scan = []
    if '-' in port_range_str:
        try:
            start_port, end_port = map(int, port_range_str.split('-'))
            ports_to_scan = range(start_port, end_port + 1)
        except ValueError:
            print(f"{ERROR_COLOR}تنسيق المنافذ غير صالح. مثال: 20-80{HEADER_COLOR_RESET}")
            time.sleep(2)
            return
    else:
        try:
            ports_to_scan = [int(p.strip()) for p in port_range_str.split(',')]
        except ValueError:
            print(f"{ERROR_COLOR}تنسيق المنافذ غير صالح. مثال: 21,22,80{HEADER_COLOR_RESET}")
            time.sleep(2)
            return
    
    print(f"{INFO_COLOR}بدء الفحص على {target}...{HEADER_COLOR_RESET}")
    try:
        remote_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{ERROR_COLOR}اسم المضيف لا يمكن تحليله. يرجى التحقق من العنوان.{HEADER_COLOR_RESET}")
        time.sleep(2)
        return

    print(f"{INFO_COLOR}فحص المنافذ المفتوحة على {remote_ip}:{HEADER_COLOR_RESET}")
    open_ports = []
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        result = sock.connect_ex((remote_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"{SUCCESS_COLOR}المنفذ {port} مفتوح{HEADER_COLOR_RESET}") 
        sock.close()

    if open_ports:
        print(f"{SUCCESS_COLOR}المنافذ المفتوحة: {', '.join(map(str, open_ports))}{HEADER_COLOR_RESET}")
    else:
        print(f"{INFO_COLOR}لم يتم العثور على منافذ مفتوحة في النطاق المحدد.{HEADER_COLOR_RESET}")
    print(f"{INFO_COLOR}--- انتهى فحص المنافذ ---{HEADER_COLOR_RESET}")
    print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
    input()


# 2. تحليل الثغرات (Vulnerability Analyzer - مثال بسيط)
def vulnerability_analyzer(name_color_index):
    clear_screen()
    print_header_only(name_color_index)
    print(f"{INFO_COLOR}--- تشغيل: تحليل الثغرات (مثال بسيط) ---{HEADER_COLOR_RESET}")
    
    print(f"{PROMPT_COLOR}أدخل عنوان IP أو اسم المضيف لتحليله: {HEADER_COLOR_RESET}", end='')
    target = input()
    print(f"{INFO_COLOR}جاري محاكاة تحليل الثغرات على {target}...{HEADER_COLOR_RESET}")
    time.sleep(2)
    print(f"{INFO_COLOR}جاري البحث عن ثغرات شائعة (SQL Injection, XSS, CVEs)...{HEADER_COLOR_RESET}")
    time.sleep(3)
    
    results = [
        "لم يتم العثور على ثغرات حرجة.",
        "تم الكشف عن إصدار قديم من Apache HTTP Server (قديم، قد يحتوي على ثغرات).",
        "لا توجد ثغرات SQL Injection واضحة.",
        "تم تحديد بعض Headers الأمنية المفقودة (مثل X-Content-Type-Options)."
    ]
    for i, res in enumerate(results):
        print(f"{INFO_COLOR}نتيجة {i+1}: {res}{HEADER_COLOR_RESET}")
        time.sleep(0.5)

    print(f"{INFO_COLOR}--- انتهى تحليل الثغرات ---{HEADER_COLOR_RESET}")
    print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
    input()

# 3. مولد كلمات المرور (Password Generator)
def password_generator(name_color_index):
    clear_screen()
    print_header_only(name_color_index)
    print(f"{INFO_COLOR}--- تشغيل: مولد كلمات المرور ---{HEADER_COLOR_RESET}")
    
    print(f"{PROMPT_COLOR}أدخل طول كلمة المرور المطلوبة (الحد الأدنى 8): {HEADER_COLOR_RESET}", end='')
    try:
        length = int(input())
        if length < 8:
            print(f"{ERROR_COLOR}طول كلمة المرور يجب أن لا يقل عن 8 أحرف.{HEADER_COLOR_RESET}")
            time.sleep(2)
            return
    except ValueError:
        print(f"{ERROR_COLOR}إدخال غير صالح. يرجى إدخال رقم.{HEADER_COLOR_RESET}")
        time.sleep(2)
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    print(f"{SUCCESS_COLOR}كلمة المرور التي تم إنشاؤها: {password}{HEADER_COLOR_RESET}")
    print(f"{INFO_COLOR}--- انتهى مولد كلمات المرور ---{HEADER_COLOR_RESET}")
    print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
    input()

# 4. أداة التشفير/فك التشفير (Caesar Cipher كمثال)
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - start + shift * mode) % 26
            result += chr(start + offset)
        else:
            result += char
    return result

def encryption_decryption_tool(name_color_index):
    clear_screen()
    print_header_only(name_color_index)
    print(f"{INFO_COLOR}--- تشغيل: أداة التشفير/فك التشفير (Caesar Cipher) ---{HEADER_COLOR_RESET}")
    
    print(f"{PROMPT_COLOR}اختر (1) تشفير أو (2) فك تشفير: {HEADER_COLOR_RESET}", end='')
    mode_choice = input()

    if mode_choice not in ['1', '2']:
        print(f"{ERROR_COLOR}خيار غير صالح. يرجى اختيار 1 أو 2.{HEADER_COLOR_RESET}")
        time.sleep(2)
        return

    print(f"{PROMPT_COLOR}أدخل النص: {HEADER_COLOR_RESET}", end='')
    text = input()
    print(f"{PROMPT_COLOR}أدخل مفتاح الإزاحة (رقم صحيح): {HEADER_COLOR_RESET}", end='')
    try:
        shift = int(input())
    except ValueError:
        print(f"{ERROR_COLOR}مفتاح الإزاحة غير صالح. يرجى إدخال رقم.{HEADER_COLOR_RESET}")
        time.sleep(2)
        return

    if mode_choice == '1': # تشفير
        encrypted_text = caesar_cipher(text, shift, 1)
        print(f"{SUCCESS_COLOR}النص المشفر: {encrypted_text}{HEADER_COLOR_RESET}")
    else: # فك تشفير
        decrypted_text = caesar_cipher(text, shift, -1)
        print(f"{SUCCESS_COLOR}النص فك التشفير: {decrypted_text}{HEADER_COLOR_RESET}")

    print(f"{INFO_COLOR}--- انتهت أداة التشفير/فك التشفير ---{HEADER_COLOR_RESET}")
    print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
    input()

# 5. أداة الهندسة العكسية (Reverse Engineering Tool - مثال بسيط)
def reverse_engineering_tool(name_color_index):
    clear_screen()
    print_header_only(name_color_index)
    print(f"{INFO_COLOR}--- تشغيل: أداة الهندسة العكسية (مثال بسيط) ---{HEADER_COLOR_RESET}")
    
    print(f"{PROMPT_COLOR}أدخل مسار الملف المراد تحليله (مثال: example.exe أو a.out): {HEADER_COLOR_RESET}", end='')
    file_path = input()

    print(f"{INFO_COLOR}جاري محاكاة تحليل الملف {file_path}...{HEADER_COLOR_RESET}")
    time.sleep(2)

    if not os.path.exists(file_path):
        print(f"{ERROR_COLOR}الملف غير موجود. جاري تحليل محاكاة لملف افتراضي.{HEADER_COLOR_RESET}")
        time.sleep(1)
        print(f"{INFO_COLOR}جاري تحليل وظائف داخلية، سلاسل نصية، ونقاط دخول...{HEADER_COLOR_RESET}")
        time.sleep(3)
        print(f"{INFO_COLOR}تم العثور على بعض السلاسل النصية المشبوهة: 'admin_password_hash', 'decrypt_key'.{HEADER_COLOR_RESET}")
        print(f"{INFO_COLOR}دالة رئيسية: main(int argc, char **argv){HEADER_COLOR_RESET}")
        print(f"{INFO_COLOR}ملف محتمل لـ 'crackme' بسيط.{HEADER_COLOR_RESET}")
    else:
        print(f"{INFO_COLOR}تحليل الملف الحقيقي: {file_path}{HEADER_COLOR_RESET}")
        print(f"{INFO_COLOR}جاري استخراج الميتاداتا، الدوال، والسلاسل النصية...{HEADER_COLOR_RESET}")
        time.sleep(4)
        print(f"{SUCCESS_COLOR}تم تحليل الملف بنجاح (وظيفة محاكاة).{HEADER_COLOR_RESET}")
        print(f"{INFO_COLOR}يمكنك استخدام أدوات مثل Ghidra أو IDA Pro لتعميق التحليل.{HEADER_COLOR_RESET}")

    print(f"{INFO_COLOR}--- انتهت أداة الهندسة العكسية ---{HEADER_COLOR_RESET}")
    print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
    input()


# --- الوظيفة الرئيسية ---
def main():
    color_index = 0
    start_time = time.time()

    while True:
        # تحديث لون الاسم كل 5 ثواني
        if time.time() - start_time >= 5:
            color_index = (color_index + 1) % (len(COLORS) - 1) 
            start_time = time.time()
        
        # قم بملء الـ buffer بالقائمة الرئيسية ثم عرضها
        populate_menu_buffer() 
        display_main_menu(color_index) 

        try:
            # هنا نستخدم input() مباشرة بعد عرض القائمة
            choice = input(f"{PROMPT_COLOR}أدخل رقم الأداة التي تريد تشغيلها: {HEADER_COLOR_RESET}")
        except EOFError: 
            break

        # لا حاجة لـ add_to_buffer("") هنا لأن الأدوات تمسح الشاشة بنفسها

        if choice == '1':
            port_scanner(color_index) # تمرير color_index للحفاظ على لون الرأس
        elif choice == '2':
            vulnerability_analyzer(color_index)
        elif choice == '3':
            password_generator(color_index)
        elif choice == '4':
            encryption_decryption_tool(color_index)
        elif choice == '5':
            reverse_engineering_tool(color_index)
        elif choice == '6':
            clear_screen()
            print(f"{SUCCESS_COLOR}شكرًا لاستخدام {TOOL_NAME}. إلى اللقاء!{HEADER_COLOR_RESET}")
            break
        else:
            # في حال الخيار غير الصالح، نستخدم طباعة مباشرة بدلاً من الـ buffer
            clear_screen()
            print_header_only(color_index)
            print(f"{ERROR_COLOR}خيار غير صالح. الرجاء المحاولة مرة أخرى.{HEADER_COLOR_RESET}")
            print(f"{PROMPT_COLOR}اضغط Enter للعودة إلى القائمة الرئيسية...{HEADER_COLOR_RESET}", end='')
            input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{INFO_COLOR}تم إنهاء {TOOL_NAME}.{HEADER_COLOR_RESET}")
        sys.exit(0)
