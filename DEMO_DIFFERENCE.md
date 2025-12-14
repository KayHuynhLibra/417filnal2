# 🎯 CÁCH THẤY RÕ SỰ KHÁC BIỆT - HƯỚNG DẪN NHANH

## ⚡ Cách Nhanh Nhất: Xem Trong GitHub Actions

### Bước 1: Vào GitHub Repository
👉 https://github.com/KayHuynhLibra/417filnal2

### Bước 2: Vào Tab "Actions"
- Click tab **Actions** ở trên cùng
- Bạn sẽ thấy 2 workflows:
  - **"Java CI with Maven and Ekstazi"** - Workflow chính
  - **"Compare: With vs Without Ekstazi"** - Workflow so sánh

### Bước 3: Xem Workflow Run
1. Click vào workflow run mới nhất
2. Xem **2 jobs chạy song song**:
   - 🔴 **Without Ekstazi**: Chạy tất cả 10 tests
   - 🟢 **With Ekstazi**: Chỉ chạy tests được chọn

### Bước 4: So Sánh Kết Quả
**Trong mỗi job, xem step "Run Tests":**

**Without Ekstazi:**
```
Tests run: 10, Failures: 0, Errors: 0
Time: ~4-5 seconds
```

**With Ekstazi (sau khi có code change):**
```
[INFO] Ekstazi: selected 3 test(s) out of 10
Tests run: 3, Failures: 0, Errors: 0
Time: ~1.5-2 seconds
```

**➡️ Sự khác biệt:**
- ⏱️ **Thời gian**: 4.5s → 1.5s (tiết kiệm 67%)
- 🧪 **Tests**: 10 → 3 (giảm 70%)

---

## 🖥️ Cách Chạy Local (Thấy Rõ Hơn)

### Setup:
```bash
cd coms417
```

### Test 1: Không Có Ekstazi (Baseline)
```bash
# Tạm thời disable Ekstazi
# Sửa pom.xml: comment Ekstazi plugin

mvn clean test
```

**Kết quả:**
- ✅ Tests run: **10**
- ⏱️ Time: **~4.76 seconds**

### Test 2: Có Ekstazi - Lần Đầu (Cold Start)
```bash
# Enable Ekstazi trong pom.xml
mvn clean test
```

**Kết quả:**
- ✅ Tests run: **10** (lần đầu phải chạy tất cả)
- ⏱️ Time: **~4.67 seconds**
- 📝 Ekstazi tạo dependency graph trong `.ekstazi/`

### Test 3: Có Ekstazi - Sau Khi Sửa Code
```bash
# Sửa Calculator.java (thêm comment hoặc sửa code)
echo "// Modified by Ekstazi demo" >> src/main/java/edu/iastate/coms417/demo/Calculator.java

# Chạy lại tests
mvn test
```

**Kết quả:**
- ✅ Tests run: **3-4** (chỉ tests liên quan đến Calculator)
- ⏱️ Time: **~1.5-2 seconds**
- 🎯 Ekstazi skip StringUtilsTest (không liên quan)

**➡️ Sự khác biệt rõ ràng:**
- **Không Ekstazi**: Luôn chạy 10 tests, ~4.76s
- **Có Ekstazi**: Chỉ chạy 3-4 tests, ~1.5s
- **Tiết kiệm**: 60-70% thời gian! 🚀

---

## 📊 Các Chỉ Số Quan Trọng

### 1. Số Lượng Tests
Tìm trong output:
```
[INFO] Tests run: X, Failures: 0, Errors: 0
```

### 2. Ekstazi Selection Message
Tìm dòng:
```
[INFO] Ekstazi: selecting tests...
[INFO] Ekstazi: selected X test(s) out of Y
```

### 3. Thời Gian Execution
Xem ở cuối output:
```
[INFO] BUILD SUCCESS
[INFO] Total time: X.XXX s
```

### 4. Cache Status (GitHub Actions)
Trong step "Cache Ekstazi":
- **Cache hit**: ✅ Ekstazi đã có dependency graph
- **Cache miss**: ⚠️ Lần đầu chạy, phải build dependency graph

---

## 🎬 Demo Scenario Cụ Thể

### Scenario: Sửa Calculator.java

**Bước 1: Chạy lần đầu (Cold Start)**
```bash
cd coms417
mvn clean test
```
Output:
```
[INFO] Tests run: 10, Failures: 0, Errors: 0
[INFO] BUILD SUCCESS in 4.67s
```

**Bước 2: Sửa Calculator.java**
```bash
# Thêm comment vào Calculator.java
echo "    // Modified for Ekstazi demo" >> src/main/java/edu/iastate/coms417/demo/Calculator.java
```

**Bước 3: Chạy lại với Ekstazi**
```bash
mvn test
```
Output:
```
[INFO] Ekstazi: selecting tests...
[INFO] Ekstazi: selected 3 test(s) out of 10
[INFO] Tests run: 3, Failures: 0, Errors: 0
[INFO] BUILD SUCCESS in 1.52s
```

**➡️ So sánh:**
| Metric | Không Ekstazi | Có Ekstazi | Tiết kiệm |
|--------|---------------|------------|-----------|
| Tests | 10 | 3 | 70% |
| Time | 4.67s | 1.52s | 67% |

---

## 🔍 Xem Chi Tiết Trong Logs

### Trong GitHub Actions:
1. Vào workflow run
2. Click vào job
3. Click vào step "Run Tests"
4. Scroll xuống tìm:
   - `[INFO] Ekstazi: selecting tests...`
   - `[INFO] Ekstazi: selected X test(s)`
   - Danh sách tests được chọn

### Trong Terminal:
```bash
cd coms417
mvn test | grep -i ekstazi
```

Hoặc xem file report:
```bash
cat target/surefire-reports/*.txt
```

---

## 💡 Tips Để Thấy Rõ Hơn

1. **Sửa ít files**: Ekstazi sẽ chọn ít tests → thấy rõ sự khác biệt
2. **Sửa nhiều files**: Ekstazi sẽ chọn nhiều tests → vẫn tiết kiệm nhưng ít hơn
3. **Lần chạy đầu**: Ekstazi phải chạy tất cả để build dependency graph
4. **Lần chạy sau**: Ekstazi chỉ chạy tests liên quan → thấy rõ sự khác biệt

---

## 📈 Kết Quả Mong Đợi

### Với Project Nhỏ (10 tests):
- **Không Ekstazi**: 10 tests, ~4.5s
- **Có Ekstazi**: 3-4 tests, ~1.5s
- **Tiết kiệm**: 60-70%

### Với Project Lớn (300+ tests):
- **Không Ekstazi**: 300+ tests, ~45s
- **Có Ekstazi**: 12 tests, ~8s
- **Tiết kiệm**: 82%

---

## 🎯 Tóm Tắt

**Để thấy rõ sự khác biệt:**

1. ✅ **Xem trong GitHub Actions** (dễ nhất)
   - Vào tab Actions
   - So sánh 2 jobs (With/Without Ekstazi)

2. ✅ **Chạy local** (rõ ràng nhất)
   - Chạy không Ekstazi → ghi nhận kết quả
   - Chạy có Ekstazi lần đầu → ghi nhận kết quả
   - Sửa code → chạy lại → thấy sự khác biệt!

3. ✅ **Xem logs chi tiết**
   - Tìm message "Ekstazi: selected X test(s)"
   - So sánh số tests và thời gian

**Sự khác biệt rõ ràng nhất khi:**
- ✅ Đã có dependency graph (sau lần chạy đầu)
- ✅ Chỉ sửa 1-2 files
- ✅ So sánh số tests và thời gian execution

