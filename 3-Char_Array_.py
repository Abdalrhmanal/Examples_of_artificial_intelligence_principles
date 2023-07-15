import numpy as np

# ----------- 1 ----   ضم العناصر
import numpy as np


# إنشاء المصفوفة الأولى x1 بنوع البيانات np.str_ وتحتوي على السلاسل "Python" و "PHP"
x1 = np.array(["Python", "PHP"], dtype=np.str_)

# إنشاء المصفوفة الثانية x2 بنوع البيانات np.str_ وتحتوي على السلاسل "Java" و "C++"
x2 = np.array(["Java", "C++"], dtype=np.str_)
print(x1)
print(x2)
# دمج المصفوفتين x1 و x2 باستخدام np.char.add()
newArray=np.char.add(x1,x2)
print(newArray)



# ----------- 2 -------- reappet Items
import numpy as np
#  لإنشاء مصفوفة نصية وتكرار كل عنصر في المصفوفة بعدد محدد من المرات.

# إنشاء المصفوفة arr بنوع البيانات np.str_ وتحتوي على السلاسل "Python", "PHP", "Java", "C++"
arr = np.array(["Python", "PHP", "Java", "C++"], dtype=np.str_)

# استخدام np.char.multiply() لتكرار كل عنصر في المصفوفة arr ثلاث مرات
newArray = np.char.multiply(arr, 3)
print(newArray)



# ----------- 3 -------- join Item
#  لإنشاء مصفوفة نصية جديدة حيث يتم دمج عناصر المصفوفة الأصلية باستخدام فاصلة أفقية (|) بين كل عنصر وآخر.

arr = np.array(["Python", "PHP", "Java", "C++"], dtype=np.str_)
newArray=np.char.join("|",arr)
print(newArray)



# ----------- 4 -------- Remove white Space
#لإنشاء مصفوفة نصية جديدة حيث يتم إزالة الفراغات الزائدة في بداية ونهاية كل عنصر في المصفوفة الأصلية.

import numpy as np
arr = np.array([" Python ", " PHP ", " Java ", " C++ "], dtype=np.str_)

# استخدام np.char.strip() لإزالة الفراغات الزائدة في بداية ونهاية كل عنصر في المصفوفة
strip = np.char.strip(arr)

# استخدام np.char.lstrip() لإزالة الفراغات الزائدة في بداية كل عنصر في المصفوفة
lstrip = np.char.lstrip(arr)

# استخدام np.char.rstrip() لإزالة الفراغات الزائدة في نهاية كل عنصر في المصفوفة
rstrip = np.char.rstrip(arr)
print(strip)
print(lstrip)
print(rstrip)


# ----------- 5 --------  split
#لتقسيم سلسلة نصية إلى أجزاء فردية بناءً على فاصل الفراغ (المسافة البيضاء) بين الكلمات.

arr = np.array(["Python PHP Java C++"], dtype=np.str_)
# استخدام np.char.split() لتقسيم السلسلة إلى أجزاء فردية بناءً على فاصل الفراغ
newArray=np.char.split(arr)
print("splite:")
print(newArray)





# لتطبيق عمليات توسيط وملء يسارًا وملء يمينًا على السلاسل في المصفوفة.

#باستخدام مكتبة ال NumPy اكتب برنامج يقوم بجعل طول كل عنصر 15 في المصفوفة المعطاة ومحاذاته 
#تحويله الى اليمين / تحويله الى اليسار باستخدام حشوات من العالمة ) _ ( 

x = np.array(['python exercises', 'PHP', 'java', 'C++'])
print("Original Array:")
print(x)
centered = np.char.center(x, 15, fillchar='_')
left = np.char.ljust(x, 15, fillchar='_')
right = np.char.rjust(x, 15, fillchar='_')
print("\nCentered =", centered)
print("Left =", left)
print("Right =", right)