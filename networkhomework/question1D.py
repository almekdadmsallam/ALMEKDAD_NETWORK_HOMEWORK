# في البداية أحتاج إلى قاموس فارغ مع التزام بأسم القاموس حسب السؤال
d = {}
# باستخدام "رينج" سأبدا من 0 وأنتهي ب 10 لأنها تصل للعنصر قبل الأخير الموجود ضمن قوسيها
for almekdad in range(11):
    # بما أن الانديكس يبدأ من صفر فإن كل انديكس هو مفتاح تكون قيمته هو الانديكس مضافًا له واحد
    d[almekdad] = almekdad + 1
# طباعة القاموس للتحقق
print(d)
