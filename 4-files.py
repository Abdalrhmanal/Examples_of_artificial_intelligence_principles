import os
import numpy as np
# لحفظ صفيف في ملف ومن ثم التحقق من وجود الملف وتحميل الصفيف منه.
a = np.arange(20)
np.save('temp_arra.npy', a)
print("Check if 'temp_arra.npy' exists or not?")
if os.path.exists('temp_arra.npy'):
    x2 = np.load('temp_arra.npy')
    print(np.array_equal(a, x2))
    print(x2)


#-----------------------------------------------------------------------

import numpy as np

# تعريف المصفوفات الأصلية
x = np.arange(10)
y = np.arange(11, 20)

print("Original arrays:")
print(x)
print(y)

# حفظ المصفوفات في ملف npz
np.savez('temp_arra.npz', x=x, y=y)

print("Load arrays from the 'temp_arra.npz' file:")
# تحميل المصفوفات من الملف npz
with np.load('temp_arra.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(x2)
    print(y2)



#-----------------------------------------------------------------------#


import numpy as np

# تعريف المصفوفة الأصلية
x = np.arange(0, 12).reshape(4, 3)

print("Original array:")
print(x)

header = 'col1 col2 col3'

# حفظ المصفوفة في ملف نصي
np.savetxt('temp.txt', x, fmt="%d", header=header)

print("After loading, content of the text file:")
# تحميل المصفوفة من الملف النصي
result = np.loadtxt('temp.txt')
print(result)



