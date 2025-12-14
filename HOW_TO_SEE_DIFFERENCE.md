# Cách Thấy Rõ Sự Khác Biệt Giữa Có và Không Có Ekstazi

## Phương Pháp 1: Xem Trong GitHub Actions (Khuyến Nghị)

### Bước 1: Trigger Workflow
1. Truy cập: https://github.com/KayHuynhLibra/417filnal2
2. Vào tab **Actions**
3. Chọn workflow **"Compare: With vs Without Ekstazi"**
4. Click **"Run workflow"** → Chọn branch `main` → **Run workflow**

### Bước 2: Xem Kết Quả So Sánh
Workflow sẽ chạy 2 jobs song song:
- **Without Ekstazi (Retest All)**: Chạy tất cả tests
- **With Ekstazi (RTS)**: Chỉ chạy tests được chọn

**So sánh:**
- Xem thời gian execution trong logs
- Xem số lượng tests được chạy
- Xem output của Maven Surefire

---

## Phương Pháp 2: Chạy Local và So Sánh

### Bước 1: Chạy Không Có Ekstazi (Baseline)
```bash
cd coms417

# Tạm thời comment Ekstazi plugin trong pom.xml
# Hoặc chạy trực tiếp:
mvn clean test -DskipTests=false
```

**Ghi chú:**
- Thời gian: ~4-5 giây
- Số tests: 10 tests (tất cả)

### Bước 2: Chạy Với Ekstazi (Lần đầu - Cold Start)
```bash
cd coms417
mvn clean test
```

**Ghi chú:**
- Thời gian: ~4-5 giây (lần đầu chạy tất cả để build dependency graph)
- Số tests: 10 tests (tất cả)
- Ekstazi tạo file `.ekstazi/org.ekstazi.data`

### Bước 3: Sửa Code và Chạy Lại (Thấy Sự Khác Biệt)
```bash
# Sửa một file source code (ví dụ: Calculator.java)
# Thêm một comment hoặc sửa một dòng code

# Chạy lại tests
mvn test
```

**Kết quả với Ekstazi:**
- Thời gian: ~1.5-2 giây ⚡
- Số tests: 3-4 tests (chỉ tests liên quan)
- Ekstazi skip các tests không liên quan

**So sánh:**
- **Không Ekstazi**: 4.76s, 10 tests
- **Có Ekstazi**: 1.5-2s, 3-4 tests
- **Tiết kiệm**: 60-70% thời gian! 🎉

---

## Phương Pháp 3: Xem Logs Chi Tiết

### Trong GitHub Actions:
1. Vào tab **Actions**
2. Click vào workflow run
3. Click vào job **"With Ekstazi (RTS)"**
4. Xem step **"Run Tests"**
5. Tìm dòng: `[INFO] Ekstazi: selecting tests...`
6. Xem danh sách tests được chọn

### Trong Terminal Local:
```bash
cd coms417
mvn test -X | grep -i ekstazi
```

Hoặc xem file log:
```bash
cat target/surefire-reports/*.txt
```

---

## Phương Pháp 4: Tạo Script So Sánh

Tạo file `compare.sh`:

```bash
#!/bin/bash
cd coms417

echo "=== Test 1: Without Ekstazi ==="
# Disable Ekstazi
sed -i 's/<plugin>/,<!--plugin>/g' pom.xml
time mvn clean test
TEST1_TIME=$(grep "Tests run:" target/surefire-reports/*.txt | tail -1)

# Re-enable Ekstazi
sed -i 's/,<!--plugin>/<plugin>/g' pom.xml
sed -i 's/<\/plugin-->/<\/plugin>/g' pom.xml

echo ""
echo "=== Test 2: With Ekstazi (First Run) ==="
time mvn clean test
TEST2_TIME=$(grep "Tests run:" target/surefire-reports/*.txt | tail -1)

echo ""
echo "=== Test 3: With Ekstazi (After Code Change) ==="
# Make a small change
echo "// Modified" >> src/main/java/edu/iastate/coms417/demo/Calculator.java
time mvn test
TEST3_TIME=$(grep "Tests run:" target/surefire-reports/*.txt | tail -1)

echo ""
echo "=== COMPARISON ==="
echo "Without Ekstazi: $TEST1_TIME"
echo "With Ekstazi (first): $TEST2_TIME"
echo "With Ekstazi (after change): $TEST3_TIME"
```

---

## Các Chỉ Số Cần Quan Sát

### 1. Thời Gian Execution
- **Không Ekstazi**: Luôn chạy tất cả tests → thời gian cố định
- **Có Ekstazi**: Thời gian giảm đáng kể sau lần chạy đầu

### 2. Số Lượng Tests
- **Không Ekstazi**: `Tests run: 10, Failures: 0, Errors: 0`
- **Có Ekstazi**: `Tests run: 3-4, Failures: 0, Errors: 0` (sau khi có thay đổi)

### 3. Ekstazi Output
Tìm trong logs:
```
[INFO] Ekstazi: selecting tests...
[INFO] Ekstazi: selected 3 test(s) out of 10
```

### 4. Cache Hit/Miss
Trong GitHub Actions, xem:
- **Cache Ekstazi** step → "Cache hit" hoặc "Cache miss"

---

## Demo Thực Tế

### Scenario: Sửa Calculator.java

1. **Lần chạy đầu (Cold Start)**:
   ```
   Tests run: 10, Failures: 0, Errors: 0
   Time: 4.67s
   ```

2. **Sửa Calculator.java** (thêm comment)

3. **Chạy lại với Ekstazi**:
   ```
   [INFO] Ekstazi: selected 3 test(s) out of 10
   Tests run: 3, Failures: 0, Errors: 0
   Time: 1.5s
   ```

4. **So sánh**:
   - Tests giảm: 10 → 3 (70% reduction)
   - Thời gian giảm: 4.67s → 1.5s (68% reduction)

---

## Xem Trong GitHub Actions UI

1. **Actions Tab** → Chọn workflow run
2. **Matrix Jobs**:
   - Click vào "Without Ekstazi" → Xem logs
   - Click vào "With Ekstazi" → Xem logs
3. **So sánh thời gian** ở phần summary
4. **Xem chi tiết** trong step "Run Tests"

---

## Tips

- **Lần chạy đầu**: Ekstazi phải chạy tất cả tests để build dependency graph
- **Lần chạy sau**: Ekstazi chỉ chạy tests liên quan → thấy rõ sự khác biệt
- **Sửa nhiều files**: Ekstazi sẽ chọn nhiều tests hơn
- **Sửa ít files**: Ekstazi sẽ chọn ít tests → tiết kiệm nhiều hơn

