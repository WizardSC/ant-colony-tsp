import matplotlib.pyplot as plt
import numpy as np
# Mảng giá trị ACO và danh sách tên thuật toán
ACO = [4.59, 4.09, 8.27]  # Ví dụ: Giá trị các thuật toán ACO
GA = [np.nan, np.nan, 8.9]
HGA = [np.nan, np.nan, 0.48]
CSO = [1.04, 2.04, 1.11]
HMMAS = [1.6, 2.14, 8.89]
BHA = [7.15, 5.25, 14.53]
instances = ['st70', 'eil76', 'eil101']  # Tên các thuật toán tương ứng

plt.figure(figsize=(8,6))


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
