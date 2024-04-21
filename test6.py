import matplotlib.pyplot as plt

# داده‌های خود را تعیین کنید
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# ایجاد نمودار خطی
plt.plot(x, y)

# تنظیم فاصله مقادیر برای محور x
plt.xticks([1, 2, 3, 4, 5])

# نمایش نمودار
plt.show()