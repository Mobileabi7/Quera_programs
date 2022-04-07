'''
برنامه‌ای بنویسید که عدد صحیح n را از ورودی دریافت کند و تعیین کند که آیا این عدد خودمقلوب است یا خیر. عدد خودمقلوب به عددی می گویند که اگر آن را برعکس کنیم، باخودش برابر شود.
'''
n = int(input())  
num1 = n
reversed_num = 0

while num1 != 0:
    
    digit = num1 % 10
    reversed_num = reversed_num * 10 + digit
    num1 = num1 // 10

if n == reversed_num:
    print("YES")
else:
    print("NO")



 


