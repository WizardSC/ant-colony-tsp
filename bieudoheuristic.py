import matplotlib.pyplot as plt
import numpy as np
# Mảng giá trị ACO và danh sách tên thuật toán
ACO = [0.09,4.09,8.27,4.40,4.52,9.55,5.55]  # Ví dụ: Giá trị các thuật toán ACO
MEP = [1.72,
4.86,
8.9,
5.24,
8.82,
6.98,
12.01
]
NN = [8.49,
13.88,
19.72,
17.8,
8.43,
18.69,
16.9
]
MST = [37.94,
37.4,
34.51,
31.13,
40.05,
46.11,
30.09
]
instances = ['berlin52', 'eil76', 'eil101', 'lin105', 'ch150','kroA150','kroB100']  # Tên các thuật toán tương ứng

plt.figure(figsize=(8, 6))


# Vẽ biểu đồ các đường
plt.plot(instances, ACO, marker='o', label='ACO', color='skyblue')
plt.plot(instances, MEP, marker='o', label='MEP', color='orange')
plt.plot(instances, NN, marker='o', label='NN', color='red')
plt.plot(instances, MST, marker='o', label='MST', color='green')


# Thêm đường kẻ ngang
for value in [10,20,30,40]:
    plt.axhline(y=value, color='gray', linestyle='--', linewidth=0.5)
# Tạo một đối tượng Figure và chỉnh kích thước
# Thêm nhãn và tiêu đề


# Thêm chú thích
plt.legend()
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
