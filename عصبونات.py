import numpy as np
features = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])
labels = np.array([0, 0, 0, 1])  # AND Gate
w = [0.9, 0.9]  # initial random values for weights القيم العشوائية الأولية للأوزان
threshold = 0.5
learning_rate = 0.1  # 0.1 to 1
epoch = 20  # learning time
for j in range(epoch):
    print("epoch", j)
    global_delta = 0
    for i in range(features.shape[0]):
        actual = labels[i]
        instance = features[i]
        sum_unit = np.dot(instance, w)
        if sum_unit > threshold:
            fire = 1
        else:
            fire = 0
        delta = actual - fire  # Error
        global_delta += abs(delta)
        print("predicted:", fire, "Actual:", actual, "(Error:", delta, ")")
        # Update weights with respect to the error
        # تحديث الأوزان فيما يتعلق بالخطأ
        w += delta * learning_rate * instance
    print("------------------------------")
    if global_delta == 0:
        break
print("------------------------------")
# Final weights
# الاوزان النهائية 
print("Final weights (w):", w)
