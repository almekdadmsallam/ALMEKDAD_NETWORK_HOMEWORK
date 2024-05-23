# استيراد مكتبة الجيسون ومن الضروري الانتباه لتثبيتها قبل العمل بها
# من الجدير بالذكر أن ملف الأسئلة المُختار تم اختياره من أرض الواقع بمادة الشبكات
import json
# التابع سيقوم بالحصول على ملف الأسئلة عند اعطائه اسم الملف لاحقًا


def view_all_question(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions
# التابع سيقوم بحفظ نتيجة الاختبار ضمن ملف وفي كل مرة ينزل سطر


def save_student_result(username, score):
    result = {"username": username, "score": score}
    with open("results.json", 'a') as file:
        json.dump(result, file)
        file.write('\n')
# التابع سيقوم بعرض نتيجة الطالب على الشاشة


def admin_view_results():
    with open("results.json", 'r') as file:
        results = file.readlines()
        for result in results:
            print(result.strip())
# تابع يقوم بأخذ بارامتر الأسئلة التي تم قراءتها


def quiz_programme(questions):
    # تبدأ نتيجة الطالب النهائية من صفر وهذا أمر إجباري ومنطقي
    score = 0
    total_questions = len(questions)
    # بكل مرة يتم المرور على الأسئلة سؤال سؤال
    for question in questions:
        # عرض السؤال على الطالب
        print(question['question'])
        # انتظار إجابة الطالب
        user_answer = input("iam sure that answer is: ").strip().lower()
        # بحال تطابق الإجابة مع قيمة المتغير يتم احتساب علامة للطالب
        if user_answer == question['answer'].strip().lower():
            score += 1
    # بنهاية الأمر يعود من التابع قيمتان رئيسيتان هما العلامة ومجموع الأسئلة
    return score, total_questions


# بداية عرض البرنامج بشاشة ترحيب
print("Welcome to the Networks Public Test \n HELLO FROM ALMEKDAD TO YOU \n")
# انتظار ادخال اسم الطالب
username = input("Enter your name: ")
# قراءة الأسئلة
questions = view_all_question("questions.json")
user_score, total_questions = quiz_programme(questions)
# عرض النتيجة على الشاشة باستخدام التوابع السابقة
print(f"Your score is: {user_score} from {total_questions}, THANK YOU")
# حفظ النتيجة
save_student_result(username, user_score)
