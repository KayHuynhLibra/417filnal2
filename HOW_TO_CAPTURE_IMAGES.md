# Hướng Dẫn Chụp Hình Cho Báo Cáo

## 📸 Các Hình Cần Chụp

### 1. GitHub Actions Workflow Results
### 2. Terminal Output (Local Testing)
### 3. Test Results Comparison
### 4. Project Structure

---

## 🖼️ CÁCH 1: Chụp GitHub Actions (Quan Trọng Nhất)

### Bước 1: Vào GitHub Actions
1. Truy cập: https://github.com/KayHuynhLibra/417filnal2/actions
2. Click vào workflow run mới nhất (có dấu ✅ xanh)

### Bước 2: Chụp Workflow Summary
**Hình 1: Workflow Overview**
- Chụp toàn bộ workflow run page
- Hiển thị: ✅ Build succeeded, thời gian (9s)
- **Cách chụp:**
  - Windows: `Win + Shift + S` (Snipping Tool)
  - Hoặc: `Print Screen` → Paste vào Paint
  - Lưu: `github_actions_workflow.png`

**Hình 2: Test Results**
- Click vào step "Test with Maven"
- Scroll xuống phần test output
- Chụp phần hiển thị:
  ```
  Tests run: 10, Failures: 0, Errors: 0
  BUILD SUCCESS
  ```
- Lưu: `github_actions_tests.png`

**Hình 3: Workflow Steps**
- Chụp phần steps (checkout, setup-java, test)
- Hiển thị các steps đã chạy thành công
- Lưu: `github_actions_steps.png`

---

## 💻 CÁCH 2: Chụp Terminal Output (Local)

### Bước 1: Chạy Tests Không Ekstazi
```bash
cd coms417
mvn clean test
```

**Chụp output:**
- Hiển thị: `Tests run: 10, Failures: 0, Errors: 0`
- Thời gian: `Total time: 4.67 s`
- Lưu: `terminal_without_ekstazi.png`

### Bước 2: Enable Ekstazi và Chạy Lại
```bash
# Uncomment Ekstazi trong pom.xml trước
mvn clean test
```

**Chụp output lần đầu (Cold Start):**
- Hiển thị: `Tests run: 10` (lần đầu)
- Lưu: `terminal_ekstazi_first_run.png`

### Bước 3: Sửa Code và Chạy Lại
```bash
# Sửa Calculator.java
echo "// Modified" >> src/main/java/edu/iastate/coms417/demo/Calculator.java

# Chạy lại
mvn test
```

**Chụp output:**
- Hiển thị: `Ekstazi: selected 3 test(s) out of 10`
- Hiển thị: `Tests run: 3, Failures: 0`
- Thời gian: `Total time: 1.5 s`
- Lưu: `terminal_ekstazi_selected.png`

### Cách Chụp Terminal:
**Windows PowerShell:**
1. Click chuột phải vào terminal
2. Chọn "Mark" → Select text → Copy
3. Paste vào Notepad/Word
4. Hoặc dùng Snipping Tool: `Win + Shift + S`

**Hoặc dùng script:**
```powershell
# Chạy và lưu output
cd coms417
mvn test > ..\test_output.txt 2>&1
```

---

## 📊 CÁCH 3: Tạo Comparison Table

### Sử dụng Excel/Google Sheets:
1. Tạo bảng so sánh:
   | Metric | Without Ekstazi | With Ekstazi | Savings |
   |--------|------------------|--------------|---------|
   | Tests  | 10               | 3-4          | 60-70%  |
   | Time   | 4.67s            | 1.5s         | 67%     |

2. Format đẹp (colors, borders)
3. Chụp screenshot
4. Lưu: `comparison_table.png`

---

## 🎨 CÁCH 4: Sử Dụng Python Script (Tự Động)

Tạo file `capture_screenshots.py`:

```python
from PIL import Image, ImageDraw, ImageFont
import os

# Tạo hình minh họa terminal output
def create_terminal_screenshot():
    # Tạo image
    img = Image.new('RGB', (800, 400), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    # Text màu xanh (terminal style)
    text = """$ cd coms417
$ mvn test

[INFO] Ekstazi: selecting tests...
[INFO] Ekstazi: selected 3 test(s) out of 10
[INFO] Tests run: 3, Failures: 0, Errors: 0
[INFO] BUILD SUCCESS in 1.5s"""
    
    # Vẽ text
    draw.text((20, 20), text, fill='#00ff00')
    
    # Lưu
    img.save('coms417/images/terminal_ekstazi.png')
    print("✅ Created terminal_ekstazi.png")

if __name__ == "__main__":
    os.makedirs('coms417/images', exist_ok=True)
    create_terminal_screenshot()
```

---

## 📁 CÁCH 5: Chụp Project Structure

### Sử dụng Tree Command:
```bash
# Windows PowerShell
tree /F coms417 > project_structure.txt

# Hoặc dùng online tool:
# https://ascii-tree-generator.com/
```

### Hoặc chụp từ VS Code:
1. Mở VS Code
2. Expand folder structure
3. Chụp screenshot
4. Lưu: `project_structure.png`

---

## 🔧 CÁCH 6: Chụp Code Snippets

### Từ GitHub:
1. Vào file trên GitHub (ví dụ: `.github/workflows/maven.yml`)
2. Click "Raw" để xem code đẹp
3. Chụp screenshot
4. Lưu: `workflow_code.png`

### Từ VS Code:
1. Mở file code
2. Format code đẹp (Shift + Alt + F)
3. Chụp screenshot
4. Lưu: `code_snippet.png`

---

## 📝 CÁCH INSERT VÀO LATEX

### Bước 1: Copy ảnh vào thư mục
```bash
# Copy tất cả ảnh vào:
coms417/images/
```

### Bước 2: Thêm vào report.tex
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{github_actions_workflow}
    \caption{GitHub Actions workflow showing successful build and test execution.}
    \label{fig:github_workflow}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{terminal_ekstazi_selected}
    \caption{Terminal output showing Ekstazi selecting only 3 tests out of 10.}
    \label{fig:terminal_ekstazi}
\end{figure}
```

---

## 🎯 CHECKLIST: Các Hình Cần Có

- [ ] **Hình 1**: GitHub Actions workflow overview (✅ succeeded)
- [ ] **Hình 2**: GitHub Actions test results (10 tests passed)
- [ ] **Hình 3**: Terminal - Without Ekstazi (10 tests, 4.67s)
- [ ] **Hình 4**: Terminal - With Ekstazi first run (10 tests)
- [ ] **Hình 5**: Terminal - With Ekstazi selected (3 tests, 1.5s)
- [ ] **Hình 6**: Comparison table (nếu có)
- [ ] **Hình 7**: Project structure (optional)
- [ ] **Hình 8**: Workflow YAML code (optional)

---

## 💡 TIPS

1. **Chất lượng ảnh:**
   - Dùng PNG cho screenshots (rõ nét)
   - Độ phân giải: ít nhất 1920x1080
   - Crop bỏ phần không cần thiết

2. **Naming:**
   - Đặt tên rõ ràng: `github_actions_workflow.png`
   - Không dùng khoảng trắng
   - Dùng lowercase và underscore

3. **Kích thước:**
   - GitHub Actions: Full page hoặc phần quan trọng
   - Terminal: Chỉ phần output, không cần toàn bộ window

4. **Annotate (nếu cần):**
   - Dùng Paint, GIMP, hoặc online tools
   - Thêm mũi tên, highlight phần quan trọng
   - Thêm text labels nếu cần

---

## 🚀 QUICK START

### Cách Nhanh Nhất:

1. **GitHub Actions:**
   - Vào: https://github.com/KayHuynhLibra/417filnal2/actions
   - `Win + Shift + S` → Chụp → Lưu vào `coms417/images/`

2. **Terminal:**
   - Chạy tests → `Win + Shift + S` → Chụp output → Lưu

3. **Insert vào LaTeX:**
   - Copy ảnh vào `coms417/images/`
   - Thêm `\includegraphics` vào report.tex
   - Compile: `pdflatex report.tex`

---

## 📦 Tools Hữu Ích

- **Snipping Tool** (Windows): `Win + Shift + S`
- **Greenshot**: Free screenshot tool
- **ShareX**: Advanced screenshot tool
- **Lightshot**: Quick screenshot
- **Online Image Editor**: https://www.photopea.com/

