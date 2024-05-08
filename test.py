import matplotlib.pyplot as plt
import numpy as np
# Mảng giá trị ACO và danh sách tên thuật toán
ACO = [0.09, 4.40, 4.52]  # Ví dụ: Giá trị các thuật toán ACO
GA = [0.013,1.75, 12.04]
HGA = [0, 1.61, 5.38]  # Ví dụ: Giá trị các thuật toán ACO2
CSO = [2, np.nan, 3.89]
HMMAS = [0.03, 0.11, 0.4]
BHA = [8.87, np.nan, np.nan]
instances = ['berlin52', 'lin105', 'ch150']  # Tên các thuật toán tương ứng

# Vẽ biểu đồ các đường
plt.plot(instances, ACO, marker='o', label='ACO', color='skyblue')
plt.plot(instances, GA, marker='s', label='GA', color='orange')
plt.plot(instances, HGA, marker='s', label='HGA', color='red')
plt.plot(instances, CSO, marker='s', label='CSO', color='green')
plt.plot(instances, HMMAS, marker='s', label='HMMAS', color='yellow')
plt.plot(instances, BHA, marker='s', label='BHA', color='purple')

# Thêm đường kẻ ngang
for value in [2, 4,6,8, 10,12]:
    plt.axhline(y=value, color='gray', linestyle='--', linewidth=0.5)

# Thêm nhãn và tiêu đề

# Thêm chú thích
plt.legend()
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
