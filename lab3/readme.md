# P-HUBcode
P-HUBcode là một dự án mô phỏng và so sánh hai thuật toán duyệt đồ thị phổ biến:  
**BFS (Breadth-First Search)** và **DFS (Depth-First Search)**.

## Công nghệ sử dụng
- **Ngôn ngữ**: Python 3.x  
- **Thư viện**: `networkx`, `matplotlib`, `time`, `collections`  
- **Môi trường**: Jupyter Notebook (`.ipynb`), Python script (`.py`)

## Mô tả hoạt động
### `demo.py`
- Triển khai và chạy BFS, DFS trên các đồ thị có/không có trọng số.
- Đo thời gian thực thi và so sánh hiệu suất.
- Tìm đường đi từ đỉnh nguồn đến đỉnh đích.
- Tính tổng trọng số (nếu có).
- Vẽ đồ thị trực quan với đường đi tô màu nổi bật.

### `lab2.ipynb`
- Notebook minh họa chi tiết từng bước:
  - Định nghĩa đồ thị
  - Cài đặt thuật toán
  - Đo thời gian chạy
  - Trực quan hóa kết quả
- Kèm giải thích và biểu đồ rõ ràng.

## Kết quả cục bộ
- Thuật toán chạy chính xác với dữ liệu mẫu.
- Hiển thị đúng đường đi của BFS và DFS.
- Đồ thị và đường đi được trực quan hóa bằng `matplotlib`.

## Kết quả trực tuyến
- File `.ipynb` tương thích với:
  - Google Colab
  - JupyterLab / Notebook
- Có thể mở rộng thành giao diện Web bằng **Streamlit**.

