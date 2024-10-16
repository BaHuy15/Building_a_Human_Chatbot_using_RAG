# Building_a_Human_Chatbot_using_RAG

## Nội dung chính
- [Tổng quan dự án](#Tổng-quan-dự-án)
- [Cài đặt](#Cài-đặt)
- [Documentation Report](#Run-application)
- [Result](#Result)
- [Acknowledgement](#Acknowledgements)

## I. Tổng quan dự án
### 1. Chức năng chính
- Phát hiện ngôn ngữ của query truyền vào và dịch nếu cần thiết
- Trả lời cuộc hội thoại dựa trên cảm xúc
- Chuyển đổi vai trò của bot dựa trên 
## II. Cài đặt
### 1. Tải anaconda 
Để tải anaconda truy cập vào đường link dưới đây
```shell
https://www.anaconda.com/products/navigator                     
```

### 2. Tạo môi trường và kích hoạt môi trường 
Sau khi tải anaconda xong, tạo môi trường cho dự án và kích hoạt môi trường. Sử dụng 2 câu lệnh dưới đây để tạo và kích hoạt môi trường mới
cho dự án.   
``` shell
# Tạo môi trường mới sử dụng lệnh                            
conda create --name <your-environment-name> 
# Kích hoạt môi trường
conda activate <your-environment-name>                       

```  
### 3. Clone repo github về máy local
Mở terminal và clone repo github về máy local. Sử dụng câu lệnh dưới đây:
 ``` shell                                 
git clone https://github.com/BaHuy15/Building_a_Human_Chatbot_using_RAG.git  
cd Building_a_Human_Chatbot_using_RAG                         
```
### 4. Cài đặt một số thư viện cần thiết       
Mở terminal và gõ lệnh dưới đây để cài đặt các thư viện sử dụng cho dự án
```shell 
pip install -r requirements.txt
```
## 5. Cài đặt Client-Server cho Qdrant vectorDB
Để trải nghiệm Qdrant trên máy cục bộ, hãy chạy container với lệnh sau:
```shell 
docker run -p 6333:6333 qdrant/qdrant
```
## III. Documentation Report
# 1.Phân tích các phương án
Để thực hiện bài toán trên ta có hai hướng tiếp cận: Fine-tune và RAG
- Fine-tuning: Ta có thể để mô hình output ra đầu ra theo ngữ cảnh/tone và cảm xúc của nhân vật. Tuy nhiên trong quá trình chuẩn bị dữ liệu em nhận thấy các bộ dữ liệu trên mạng chỉ cung cấp những câu đơn lẻ và thiếu ngữ cảnh của những cuộc hội thoại trước đó. Bên cạnh đó, qua quá trình chuẩn bị dữ liệu. Em gặp phải thách thức out of quota khi sử dụng GPT4 để sinh câu hỏi => Vấn đề chi phí 
- RAG: Một số thư viện như LangChain hỗ trợ cơ chế lưu trữ hội thoại vào memory => Chọn phương án RAG. Vì RAG phù hợp với những dự án có dữ liệu không quá lớn.

# 2. Chuẩn bị prompt (Lưu trong thư mục Prompt)
 - System prompt: System prompt cho hệ thống đóng vai trò là nhân vật Choi để giải đáp một số thắc mắc của David
 - Emotion prompt: User prompt cho hệ thống đóng vai trò là David để hỏi một số.
 - Topic prompt: Prompt dùng để trích xuất chủ đề của cuộc hội thoại.
 - conversation prompt: Prompt dùng để lưu trữ lịch sử hội thoại
 - anecdotes prompt: Prompt dùng để trích xuất câu chuyện ngắn trong cuộc hội thoại
# 3. Trích xuất thông tin và lưu vào lịch sử trò chuyện
Trước tiên, Để mô hình có thể trả lời theo ngôn ngữ câu hỏi câu hỏi.  Trong system prompt em sử dụng kỹ thuật prompt enigneer là tips thêm cho mô hình tiền nếu mô hình trả lời đúng theo yêu cầu của em đặt ra     
![alt text](Backend/images/image-1.png)            
Và kết quả:           
![alt text](Backend/images/image.png)
- Tạo lịch sử trò chuyện sử dụng LangChain framework, để lưu trữ lịch sử hội thoại vào memory
![alt text](Backend/images/image-2.png)                
- Sử dụng LangChain để lưu trữ câu chuyện ngắn/topic/lịch sử hội thoại vào memory
![alt text](Backend/images/image1.png)

# 4. Lựa chọn vectorDB(Đang làm)
Em lựa chọn Qdrant bởi một số lý do sau:      
- Qdrant được thiết kế để cung cấp khả năng tìm kiếm vector nhanh và hiệu quả
- Với khả năng mở rộng quy mô, Qdrant có thể xử lý lượng dữ liệu lớn và thực hiện tìm kiếm theo thời gian thực, phù hợp cho các ứng dụng cần truy xuất thông tin nhanh chóng từ các tập dữ liệu khổng lồ.

# 5. Embedding model(Đang làm)
model_name : all-MiniLM-L12-v2 
Mặc dù mô hình này chủ yếu tập trung vào tiếng Anh, nó cũng có khả năng hỗ trợ đa ngôn ngữ. Điều này làm cho nó trở thành lựa chọn hợp lý cho các dự án đa ngôn ngữ hoặc yêu cầu xử lý các ngôn ngữ khác nhau trong một hệ thống duy nhất. Rất phù hợp với dự án này. Vì chúng ta cần tìm kiếm ngữ nghĩa của 2 loại ngôn ngữ là tiếng anh và tiếng hàn
Chi tiết: Backend/embedding_model/sentencetransformer.py




