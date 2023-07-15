import numpy as np
#Example1

#  =partition=تقسيم
arr=np.array([70,50,30,100,60,50,40])
print("before partition: ")
print(arr)
arr=np.partition(arr,2)
print("After partition: ")
print(arr)
# ---------------------------------------------------------

#Example2

# فرز جزء من المصفوفة (أصغر (ن عناصر)) والعناصر الكبيرة لا تُفرز
# num = np.random.randint (10) # إنشاء أرقام عشوائية
# num = np.random.randint (0،10، (3،3)) # إنشاء أرقام عشوائية
arr=np.array([70,50,30,100,60,50,40])
print(arr)
print("------------------")
print(arr[np.argpartition(arr,range(5))])

# ---------------------------------------------------------

#Example3

nums=np.random.randint(5,100,(3,3)) #generate random numbers توليد أرقام عشوائية 
print(nums)
print("------------------")
print(nums[nums[:,1].argsort()])

# ---------------------------------------------------------

#Example4

nums=np.array([[10,40],[30,20],[101,401],[301,201]])
print(nums)
print("------------------")
print(np.sort(nums))
print("------------------")
print(np.sort(nums,axis=0))
print("------------------")
print(np.sort(nums,axis=None))


# ---------------------------------------------------------

#Example5


# اضافة عمود
# new_array = np.append(array2d, [[9], [10]], axis=1)

# لإلضافة على المصفوفة في مكان محدد )ليس في آخرها( نستخدم الدالة insert.np بالطريقة التالية:
# new_array = np.insert(array2d, (0, 0), 5, axis=1)

# اكتب برنامج باستخدام NumPy لتقسيم مصفوفة معينة في موضع محدد ونقل جميع قيم العناصر
# األصغر إلى يسار القسم والقيم المتبقية إلى اليمين بترتيب عشوائي )بنا ًء على اختيار عشوائي(.

nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4))

#---------------------------------------------------------
nums = np.random.rand(10)  # عشوائية أرقام توليد
print("Original array:")
print(nums)
print("\nSorted first 5 elements:")
print(nums[np.argpartition(nums, range(5))])


#---------------------------------------------------------

print("Original array:\n")
nums = np.random.randint(0, 10, (3, 3))# توليد ارقام عشوائية  
print(nums)
print("\nSort the said array by the nth column: ")#افرز المصفوفة حسب العمود التاسع:
print(nums[nums[:, 1].argsort()])


#---------------------------------------------------------

a = np.array([[10, 40, 50], [29, 30, 9],[23,2,1]])
print("Original array:")
print(a)
print("Sort the array along the first axis:")#فرز حسب الصف الاول
print(np.sort(a, axis=0))
print("Sort the array along the last axis:")#)فرز حسب الصف الاخير#
print(np.sort(a))
print("Sort the flattened array:")# ترتيب المصفوفة
print(np.sort(a, axis=None))


#----------------------------------------------------------

# 5 اكتب برنامج NumPy إلنشاء مصفوفة منظمة من اسم الطالب وطوله وفصله وأنواع بياناته. اآلن
# قم بفرز المصفوفة على ارتفاع

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),
                    ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))

#---------------------------------------------------------


# 6 اكتب برنامج NumPy إلنشاء مصفوفة منظمة من اسم الطالب وطوله وفصله وأنواع بياناته. اآلن قم بالفرز حسب
# الفئة ، ثم االرتفاع إذا كانت الفئة متساوية.

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),
                    ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)
print("Sort by class, then height if class are equal:")
print(np.sort(students, order=['class', 'height']))

#------------------------------------------------------