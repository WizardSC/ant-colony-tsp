import matplotlib.pyplot as plt
import numpy as np
# Mảng giá trị ACO và danh sách tên thuật toán
ACO = [5.67, 9.55, 5.55, 7.05, 4.24, 7.19]  # Ví dụ: Giá trị các thuật toán ACO
GA = [6.01, 10.21, 6.9, 13.93, 9.44, 6.64]
HGA = [2.06, 5.89, 0.16, 4.93, 1.97, 1.16]
CSO = [2.04, np.nan, 3.94, np.nan, 4.43, np.nan]
HMMAS = [0.42, np.nan,np.nan,np.nan,np.nan, np.nan]
BHA = [np.nan, np.nan, np.nan,np.nan,np.nan, np.nan]
instances = ['kroA100', 'kroA150', 'kroB100', 'kroB150', 'kroC100', 'kroE100']  # Tên các thuật toán tương ứng

plt.figure(figsize=(8, 6))


# Vẽ biểu đồ các đường
plt.plot(instances, ACO, marker='o', label='ACO', color='skyblue')
plt.plot(instances, GA, marker='o', label='GA', color='orange')
plt.plot(instances, HGA, marker='o', label='HGA', color='red')
plt.plot(instances, CSO, marker='o', label='CSO', color='green')
plt.plot(instances, HMMAS, marker='o', label='HMMAS', color='yellow')
plt.plot(instances, BHA, marker='o', label='BHA', color='purple')

# Thêm đường kẻ ngang
for value in [2, 4,6,8, 10,12,14]:
    plt.axhline(y=value, color='gray', linestyle='--', linewidth=0.5)
# Tạo một đối tượng Figure và chỉnh kích thước
# Thêm nhãn và tiêu đề

# Thêm chú thích
plt.legend()
plt.tight_layout()
# Hiển thị biểu đồ
plt.show()
