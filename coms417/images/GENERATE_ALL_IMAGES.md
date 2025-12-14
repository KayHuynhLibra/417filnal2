# Hướng dẫn tạo tất cả hình ảnh

## ✅ Đã tạo tự động

1. **rts_diagram.png** - Đã tạo bằng Python script
2. **github_actions.png** - Đã tạo bằng Python script

## 📸 Cần chụp screenshot

### 1. ekstazi_result.png

**Cách 1: Chạy script PowerShell**
```powershell
cd images
.\capture_terminal_output.ps1
# Sau đó chụp màn hình terminal
```

**Cách 2: Chạy thực tế**
```bash
cd coms417
mvn test
# Chụp màn hình phần output hiển thị:
# - "Ekstazi: Selected X tests"
# - Thời gian execution
# - Số lượng tests
```

**Cách 3: Tạo bằng code (nếu có Ekstazi enabled)**
- Uncomment Ekstazi trong pom.xml
- Chạy mvn test
- Chụp screenshot

## 🎨 Chỉnh sửa hình ảnh (nếu cần)

### Dùng Paint hoặc online tools:
- https://www.photopea.com (miễn phí, giống Photoshop)
- https://www.canva.com
- Microsoft Paint (built-in Windows)

### Chỉnh sửa:
- Crop để loại bỏ phần không cần
- Thêm annotations nếu cần
- Đảm bảo text rõ ràng

## 📋 Checklist

- [x] rts_diagram.png - Đã tạo
- [x] github_actions.png - Đã tạo  
- [ ] ekstazi_result.png - Cần chụp screenshot

## 💡 Tips

1. **Terminal screenshot:**
   - Dùng font lớn (Consolas, Courier New)
   - Background tối, text sáng (hoặc ngược lại)
   - Zoom in để text rõ hơn

2. **GitHub Actions screenshot:**
   - Chụp cả phần workflow run
   - Hiển thị execution time
   - Hiển thị test results (green checkmark)

3. **Kích thước:**
   - Width: 800-1200px là tốt nhất
   - Format: PNG (không mất chất lượng)
   - Resolution: 150-300 DPI

## 🚀 Quick Start

```bash
# 1. Tạo diagrams (đã xong)
cd images
python create_rts_diagram.py
python create_github_actions_diagram.py

# 2. Chụp screenshot terminal
cd ..
mvn test
# Chụp màn hình → lưu thành ekstazi_result.png trong thư mục images/

# 3. Kiểm tra tất cả files
ls images/*.png
```

Sau khi có đủ 3 hình ảnh, compile LaTeX sẽ hiển thị chúng trong báo cáo!

