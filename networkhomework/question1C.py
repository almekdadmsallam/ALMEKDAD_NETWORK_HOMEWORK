# تعريف القائمة المكتوبة في السؤال
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
# المرور على عناصر القائمة عنصر تلو العنصر
for word in L:
    # شرط التحقق فيما إذا كان العنصر طولة أكبر من 1 ويبدأ بالحرف المطلوب
    if len(word) > 0 and word.startswith('B'):
        print(f"'{word}' : start with letter 'B'")
    else:
        print(f"sorry, '{word}' does not start with letter 'B' ")
