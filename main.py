import math
import os
import time 
from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    total_execution_time = 0
    total_cost = 0
    best_cost = float('inf')
    best_path = None
    
    
    for _ in range(10):  # Chạy chương trình 10 lần
        start_time = time.time()  # Thời điểm bắt đầu thực thi chương trình
        
        cities = []
        points = []
        input_file_name = 'data/berlin52.tsp'
        base_file_name = os.path.splitext(os.path.basename(input_file_name))[0]
        # output_file_name = os.path.join('data/', base_file_name + '_matrix.txt')
        
        with open(input_file_name) as f:
            for line in f.readlines():
                city = line.split()
                if len(city) != 3:
                    # Bỏ qua các dòng không đúng định dạng
                    continue
                try:
                    cities.append(dict(index=int(city[0]), x=int(float(city[1])), y=int(float(city[2]))))
                    points.append((int(float(city[1])), int(float(city[2]))))
                except ValueError:
                    # Bỏ qua các dòng không thể chuyển đổi thành số nguyên
                    continue
        
        cost_matrix = []
        rank = len(cities)
        
        for i in range(rank):
            row = []
            for j in range(rank):
                row.append(distance(cities[i], cities[j]))
            cost_matrix.append(row)
        
        aco = ACO(50, 400, 1.0, 2.0, 0.5, 100, 2)
        graph = Graph(cost_matrix, rank)
        path, cost = aco.solve(graph)
        total_cost += cost
        
        rounded_cost = round(cost)  # Làm tròn kết quả cost thành số nguyên
        
        if cost < best_cost:
            best_cost = cost
            best_path = path
            
        
        
        # plot(points, path)
        
        # Hoặc lưu ma trận chi phí vào một tệp văn bản
        # with open(output_file_name, 'w') as f:
        #     for row in cost_matrix:
        #         f.write(' '.join(map(str, row)) + '\n')
        
        end_time = time.time()  # Thời điểm kết thúc thực thi chương trình
        execution_time = end_time - start_time  # Thời gian thực thi chương trình
        total_execution_time += execution_time
        print('Lần chạy {}: cost: {}, path: {}'.format(_+1, rounded_cost, path))
        print("Thời gian chạy lần {}: {:.2f} giây".format(_+1, execution_time))
    
    average_execution_time = total_execution_time / 10
    average_cost = total_cost / 10
    print("Thời gian chạy trung bình: {:.2f} giây".format(average_execution_time))
    print("Kết quả trung bình: {:.2f}".format(average_cost))
    
    print("Cost của thời gian chạy tốt nhất: {}".format(round(best_cost)))
    print("Path của thời gian chạy tốt nhất:", best_path)
    

if __name__ == '__main__':
    main()
