# Hướng dẫn tạo hình ảnh cho báo cáo

## Các hình ảnh cần thiết

1. `rts_diagram.png` - Sơ đồ minh họa RTS workflow
2. `ekstazi_result.png` - Screenshot terminal output khi chạy Ekstazi
3. `github_actions.png` - Screenshot GitHub Actions workflow

## Cách tạo/tìm hình ảnh

### 1. rts_diagram.png

**Cách 1: Vẽ bằng PowerPoint/Visio**
- Vẽ sơ đồ đơn giản minh họa:
  - Code Change → Dependency Analysis → Selected Tests
  - So sánh: Retest All (tất cả tests) vs RTS (chỉ tests liên quan)

**Cách 2: Dùng online tool**
- https://www.draw.io
- https://excalidraw.com
- Vẽ sơ đồ flow chart đơn giản

**Cách 3: Dùng Python (đã tạo script)**
- Chạy script `create_rts_diagram.py` để tự động tạo

### 2. ekstazi_result.png

**Cách chụp screenshot:**
1. Mở terminal/command prompt
2. Vào thư mục project: `cd coms417`
3. Chạy: `mvn test`
4. Chụp màn hình phần output hiển thị:
   - "Ekstazi: Selected X tests"
   - Thời gian execution
   - Số lượng tests chạy

**Hoặc dùng PowerShell để tạo:**
- Chạy script `capture_terminal_output.ps1`

### 3. github_actions.png

**Cách chụp screenshot:**
1. Vào: https://github.com/KayHuynhLibra/coms417/actions
2. Click vào một workflow run
3. Chụp màn hình hiển thị:
   - Build status (green checkmark)
   - Execution time
   - Test results

## Kích thước khuyến nghị

- Width: 800-1200 pixels
- Format: PNG hoặc JPG
- Resolution: 150-300 DPI

## Lưu ý

- Đảm bảo text trong ảnh rõ ràng, dễ đọc
- Nếu chụp terminal, dùng font lớn và contrast tốt
- Có thể crop để loại bỏ phần không cần thiết

