# Step-by-Step Guide: Experiment 3 - EvoSuite

## 📋 Tổng Quan

Hướng dẫn từng bước để chạy Experiment 3 với EvoSuite.

---

## ✅ Đã Hoàn Thành

### Bước 1-6: Setup Project ✅

- [x] ✅ Tạo folder structure
- [x] ✅ Copy source code (Calculator, StringUtils)
- [x] ✅ Tạo pom.xml với EvoSuite & JaCoCo
- [x] ✅ Copy evosuite-1.2.0.jar
- [x] ✅ Tạo README.md
- [x] ✅ Tạo helper scripts

---

## 🚀 Bước Tiếp Theo: Generate Tests

### Bước 7: Compile Project

```powershell
cd experiment3_evosuite

# Đảm bảo dùng Java 17
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Compile
mvn clean compile
```

**Kết quả mong đợi**: 
```
[INFO] BUILD SUCCESS
[INFO] Compiling 2 source files
```

---

### Bước 8: Generate Tests với EvoSuite

#### Option A: Dùng Script (Dễ nhất)

```powershell
# Windows PowerShell
.\generate_tests.ps1
```

#### Option B: Manual Commands

**Generate tests cho Calculator:**
```powershell
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.Calculator `
  -Dsearch_budget=60
```

**Generate tests cho StringUtils:**
```powershell
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.StringUtils `
  -Dsearch_budget=60
```

**Kết quả mong đợi**:
- Folder `evosuite-tests/` được tạo
- Test files: `Calculator_ESTest.java`, `StringUtils_ESTest.java`

---

### Bước 9: Copy Generated Tests

```powershell
# Tạo folder nếu chưa có
New-Item -ItemType Directory -Path "src\test\java\edu\iastate\coms417\demo" -Force

# Copy tests
Copy-Item -Recurse -Force "evosuite-tests\edu\iastate\coms417\demo\*" "src\test\java\edu\iastate\coms417\demo\"
```

---

### Bước 10: Run Tests

```powershell
mvn test
```

**Kết quả mong đợi**:
```
Tests run: X, Failures: 0, Errors: 0
BUILD SUCCESS
```

---

### Bước 11: Generate Coverage Report

```powershell
mvn jacoco:report
```

**Kết quả**:
- Report tại: `target/site/jacoco/index.html`
- Mở file này trong browser để xem coverage

---

### Bước 12: So Sánh với Manual Tests

1. Xem generated tests trong `src/test/java/`
2. So sánh với manual tests từ Experiment 1
3. Note differences:
   - Coverage
   - Test cases
   - Readability

---

## 📊 Expected Results

| Metric | Expected Value |
|--------|----------------|
| Generated Tests | 20-50 tests per class |
| Line Coverage | 70-90% |
| Test Execution Time | 5-15 seconds |
| Report Location | `target/site/jacoco/index.html` |

---

## ⚠️ Troubleshooting

### Issue: "invalid target release: 17"

**Solution**: Đảm bảo dùng Java 17:
```powershell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
java -version  # Should show Java 17
```

### Issue: EvoSuite không tìm thấy class

**Solution**: 
- Check classpath: `-projectCP target/classes`
- Verify class đã compile: `mvn compile`
- Use full package name: `edu.iastate.coms417.demo.Calculator`

### Issue: Generated tests không compile

**Solution**:
- Check EvoSuite runtime dependency trong `pom.xml`
- Clean và rebuild: `mvn clean compile test-compile`

---

## 🎯 Next Steps After Completion

1. ✅ Review generated tests
2. ✅ Analyze coverage report
3. ✅ Compare với manual tests
4. ✅ Document findings
5. ✅ Integrate với CI/CD (optional)

---

## 📝 Notes

- EvoSuite có thể mất 1-2 phút để generate tests
- Search budget càng cao, coverage càng tốt (nhưng mất thời gian hơn)
- Generated tests có thể cần chỉnh sửa để dễ đọc hơn

