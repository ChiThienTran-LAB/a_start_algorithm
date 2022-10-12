from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list #danh sách các đỉnh và đỉnh gần kề
    def get_neighbors(self, v): #lấy hàng xóm nút đang xét
        return self.adjacency_list[v]
    def h(self, n): #khai báo vị trí các điểm, h: hàm heuristic, hàm heuristic với các giá trị bằng nhau cho tất cả các nút
        H = {
            'P1': 1,
            'P2': 1,
            'P3': 1,
            'P4': 1,
            'P5': 1,
            'P6': 1,
            'P7': 1
        }
        return H[n]
    def a_star_algorithm(self, start_node, stop_node): #hàm a* chứa điểm BĐ và điểm KT
        # open_list là danh sách các nút đã được truy cập, nhưng ai là hàng xóm của
        # tất cả nút chưa được kiểm tra, hãy bắt đầu với nút bắt đầu
        # closed_list là danh sách các nút đã được truy cập
        # và hàng xóm của ai đã được kiểm tra
        open_list = set([start_node])
        closed_list = set([])
        # g chứa khoảng cách hiện tại từ start_node đến tất cả các nút khác
        # giá trị mặc định (nếu nó không được tìm thấy trong bản đồ) là + vô cùng
        g = {}
        g[start_node] = 0
        # parents chứa một bản đồ kề của tất cả các nút
        parents = {}
        parents[start_node] = start_node
        
        while len(open_list) > 0:
            n = None
            #tìm một nút có giá trị thấp nhất của f () - hàm đánh giá
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('Không có đường đi nào!')
                return None
            # nếu nút hiện tại là stop_node
            # sau đó bắt đầu tạo lại đường dẫn từ nó đến start_node
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Đường đi được tìm thấy: {}'.format(reconst_path))
                return reconst_path
            # đối với tất cả các hàng xóm của nút hiện tại thì thực hiện
            for (m, weight) in self.get_neighbors(n):
                # nếu nút hiện tại không có trong cả open_list và closed_list
                # thêm nó vào open_list và ghi chú n vì nó là parents
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # nếu không, hãy kiểm tra xem lần đầu tiên đến thăm n có nhanh hơn không, sau đó m
                # và nếu có, hãy cập nhật dữ liệu parents và dữ liệu g
                # và nếu nút nằm trong closed_list, hãy chuyển nó sang open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # xóa n khỏi open_list và thêm nó vào closed_list
            # Bởi vì tất cả hàng xóm đã được kiểm tra
            open_list.remove(n)
            closed_list.add(n)
        print('Đường đi không tồn tại!')
        return None
def input_start():
    print('Mời bạn nhập điểm đi: ')
    start = input() #P1
    return start.upper()
def input_stop():
    print('Mời bạn nhập điểm đến: ')
    stop = input()
    return stop.upper()
adjacency_list = {
    'P1': [('P2', 0.5), ('P3', 1.1)],
    'P2': [('P3', 1.0), ('P1', 0.5)],
    'P3': [('P4', 1.5), ('P6', 2.9), ('P7', 2.0), ('P1', 1.1), ('P2', 1.0)],
    'P4': [('P5', 1.5), ('P4', 1.5)],
    'P5': [('P6', 1.0), ('P4', 1.5)],
    'P6': [('P7', 1.0), ('P5', 1.0), ('P3', 2.9)],
    'P7': [('P3', 2.0), ('P6', 1.0)]
}
graph1 = Graph(adjacency_list)
# print(f"Đường đi ngắn nhất từ {input_start()} đến {input_stop()}")
print('Chào mừng bạn đến với!\nChương trình tìm đường đi đến các Trạm Y tế phường Bình Thạnh')
print('Danh sách Trạm Y tế hỗ trợ từ Phường 1 đến Phường 24')
print('Bạn chỉ cần nhập đúng viết tắt của tên phường đi và đến (Ví dụ: P1 ứng với Phường 1)')
print('Minh họa: Điểm đi P1 -> Điểm đến P4')
graph1.a_star_algorithm(input_start(), input_stop())
