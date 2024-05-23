import termcolor
# تعريف تابع يقوم بحساب عاملي أي عدد


def factorial_question1B(n):
    factorial_sum = 1
    for i in range(1, n + 1):
        factorial_sum = factorial_sum * i
    return factorial_sum


# ادخال عدد من قبل المستخدم أكبر من صفر
num = int(input("Enter a number greater than or equal to zero "))
# هنا تتم معالجة حالة ادخال عدد أفل من صفر
if num < 0:
    print("I told you earlier to enter a number greater than zero because there is no factorial for negative numbers")
# حالة الادخال الصحيح والحساب
else:
    print(termcolor.colored("The Factorial of", color="red"), end=" ")
    print(f"{num} is : {factorial_question1B(num)}")
