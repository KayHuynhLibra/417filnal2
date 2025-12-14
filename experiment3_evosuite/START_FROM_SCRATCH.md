# 🚀 Bắt Đầu Lại Từ Đầu - Experiment 3: EvoSuite

## 📋 Mục Đích

File này hướng dẫn bạn **bắt đầu lại từ đầu** để setup và chạy Experiment 3 với EvoSuite.

---

## ✅ Checklist Trước Khi Bắt Đầu

- [ ] Java 17+ đã cài đặt
- [ ] Maven 3.6+ đã cài đặt
- [ ] Đã có folder `experiment3_evosuite/`
- [ ] Đã có file `evosuite-1.2.0.jar`

---

## 📁 Bước 1: Kiểm Tra Cấu Trúc Folder

### Cấu trúc cần có:

```
experiment3_evosuite/
├── pom.xml
├── evosuite-1.2.0.jar
├── src/
│   ├── main/java/edu/iastate/coms417/demo/
│   │   ├── Calculator.java
│   │   └── StringUtils.java
│   └── test/java/edu/iastate/coms417/demo/
│       └── (sẽ có sau khi generate tests)
└── README.md
```

### Kiểm tra:

```powershell
cd experiment3_evosuite
Get-ChildItem -Recurse -File | Select-Object FullName
```

**Nếu thiếu file nào**, xem phần "Khôi Phục Files" bên dưới.

---

## 🔧 Bước 2: Setup Java 17

### Kiểm tra Java version:

```powershell
java -version
```

**Phải thấy**: `java version "17.x.x"` hoặc cao hơn

### Nếu không có Java 17:

1. **Tải Java 17**: https://adoptium.net/
2. **Cài đặt**
3. **Set JAVA_HOME**:

```powershell
# Windows PowerShell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Verify
java -version
```

---

## 📦 Bước 3: Setup Maven

### Kiểm tra Maven:

```powershell
mvn -version
```

**Phải thấy**: `Apache Maven 3.6.x` hoặc cao hơn

### Nếu không có Maven:

1. **Tải Maven**: https://maven.apache.org/download.cgi
2. **Giải nén** vào folder (ví dụ: `D:\tools\apache-maven-3.9.11`)
3. **Thêm vào PATH**:

```powershell
$env:PATH += ";D:\tools\apache-maven-3.9.11\bin"
mvn -version
```

---

## 🏗️ Bước 4: Compile Project

### Compile source code:

```powershell
cd experiment3_evosuite

# Đảm bảo dùng Java 17
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Compile
mvn clean compile
```

### Kết quả mong đợi:

```
[INFO] BUILD SUCCESS
[INFO] Compiling 2 source files with javac [debug target 17]
```

### Nếu có lỗi:

- **"invalid target release: 17"** → Đảm bảo dùng Java 17
- **"mvn: command not found"** → Maven chưa trong PATH
- **"Cannot find pom.xml"** → Đang ở sai folder

---

## 🧪 Bước 5: Generate Tests với EvoSuite

### Option A: Dùng Script (Khuyên dùng)

```powershell
# Chạy script tự động
.\generate_tests.ps1
```

Script sẽ:
1. Compile project
2. Generate tests cho Calculator
3. Generate tests cho StringUtils
4. Copy tests vào `src/test/java/`

### Option B: Manual Commands

#### 5.1: Generate Calculator Tests

```powershell
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.Calculator `
  -Dsearch_budget=60 `
  -Dassertion_timeout=120 `
  -Dminimization_timeout=120
```

**Kết quả**: Folder `evosuite-tests/` được tạo với `Calculator_ESTest.java`

#### 5.2: Generate StringUtils Tests

```powershell
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.StringUtils `
  -Dsearch_budget=60 `
  -Dassertion_timeout=120 `
  -Dminimization_timeout=120
```

**Kết quả**: `StringUtils_ESTest.java` được tạo

#### 5.3: Copy Generated Tests

```powershell
# Tạo folder test nếu chưa có
New-Item -ItemType Directory -Path "src\test\java\edu\iastate\coms417\demo" -Force

# Copy tests
Copy-Item -Recurse -Force "evosuite-tests\edu\iastate\coms417\demo\*" "src\test\java\edu\iastate\coms417\demo\"
```

---

## ▶️ Bước 6: Run Tests

### Compile và run tests:

```powershell
mvn test
```

### Kết quả mong đợi:

```
[INFO] Tests run: X, Failures: 0, Errors: 0
[INFO] BUILD SUCCESS
```

### Nếu có lỗi:

- **"ClassNotFoundException"** → EvoSuite runtime chưa trong classpath (đã có trong pom.xml)
- **"Tests not found"** → Tests chưa được copy vào `src/test/java/`
- **Compilation errors** → Check generated tests có syntax errors

---

## 📊 Bước 7: Generate Coverage Report

### Generate JaCoCo report:

```powershell
mvn jacoco:report
```

### Xem report:

```powershell
# Windows
start target/site/jacoco/index.html

# Linux/Mac
open target/site/jacoco/index.html
```

### Kết quả mong đợi:

- **Line Coverage**: 70-90%
- **Branch Coverage**: 60-80%
- **Method Coverage**: 80-100%

---

## 🔍 Bước 8: So Sánh với Manual Tests

### Xem generated tests:

```powershell
# Xem Calculator tests
Get-Content src\test\java\edu\iastate\coms417\demo\Calculator_ESTest.java

# Xem StringUtils tests
Get-Content src\test\java\edu\iastate\coms417\demo\StringUtils_ESTest.java
```

### So sánh với Experiment 1:

1. **Coverage**: EvoSuite thường có coverage cao hơn
2. **Readability**: Manual tests dễ đọc hơn
3. **Edge cases**: EvoSuite tìm được nhiều edge cases hơn
4. **Maintenance**: Manual tests dễ maintain hơn

---

## 🛠️ Khôi Phục Files (Nếu Cần)

### Nếu thiếu pom.xml:

Xem file `pom.xml` trong folder `experiment3_evosuite/` hoặc tạo lại từ template trong `README.md`

### Nếu thiếu evosuite-1.2.0.jar:

1. **Download**: https://github.com/EvoSuite/evosuite/releases/tag/v1.2.0
2. **Hoặc copy từ**: `417-final-CICD/CICD-testing/evosuite-1.2.0.jar`

### Nếu thiếu source code:

Xem files:
- `src/main/java/edu/iastate/coms417/demo/Calculator.java`
- `src/main/java/edu/iastate/coms417/demo/StringUtils.java`

---

## ⚠️ Troubleshooting

### Vấn đề 1: "EvoSuite không tìm thấy class"

**Nguyên nhân**: Classpath sai hoặc class chưa compile

**Giải pháp**:
```powershell
# Recompile
mvn clean compile

# Verify class exists
Test-Path target/classes/edu/iastate/coms417/demo/Calculator.class
```

### Vấn đề 2: "Generated tests không compile"

**Nguyên nhân**: EvoSuite runtime chưa trong classpath

**Giải pháp**: 
- Check `pom.xml` có dependency `evosuite-standalone-runtime`
- Run: `mvn clean compile test-compile`

### Vấn đề 3: "Coverage report không được tạo"

**Nguyên nhân**: JaCoCo plugin chưa chạy

**Giải pháp**:
```powershell
# Run tests với JaCoCo
mvn clean test jacoco:report

# Check report exists
Test-Path target/site/jacoco/index.html
```

### Vấn đề 4: "Script không chạy được"

**Nguyên nhân**: Execution policy hoặc path issues

**Giải pháp**:
```powershell
# Allow script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Hoặc chạy manual commands (xem Option B ở Bước 5)
```

---

## 📝 Checklist Hoàn Thành

Sau khi hoàn thành, bạn nên có:

- [ ] ✅ Project compile thành công
- [ ] ✅ Generated tests cho Calculator
- [ ] ✅ Generated tests cho StringUtils
- [ ] ✅ Tests chạy thành công (0 failures)
- [ ] ✅ Coverage report được tạo
- [ ] ✅ Đã xem coverage metrics
- [ ] ✅ Đã so sánh với manual tests

---

## 🎯 Kết Quả Mong Đợi

| Metric | Expected Value |
|--------|----------------|
| **Generated Tests** | 20-50 tests per class |
| **Line Coverage** | 70-90% |
| **Branch Coverage** | 60-80% |
| **Test Execution Time** | 5-15 seconds |
| **Build Status** | SUCCESS |

---

## 📚 Tài Liệu Tham Khảo

- **README.md**: Hướng dẫn đầy đủ về EvoSuite
- **STEP_BY_STEP_GUIDE.md**: Hướng dẫn chi tiết từng bước
- **QUICK_START.md**: Bắt đầu nhanh
- **EvoSuite Docs**: http://www.evosuite.org/documentation/

---

## 🆘 Cần Giúp Đỡ?

1. **Check logs**: Xem output của Maven/EvoSuite
2. **Verify setup**: Đảm bảo Java 17 và Maven đã setup đúng
3. **Clean rebuild**: `mvn clean compile test`
4. **Check files**: Đảm bảo tất cả files cần thiết đã có

---

## ✅ Hoàn Thành!

Sau khi hoàn thành tất cả các bước, bạn đã:

1. ✅ Setup EvoSuite thành công
2. ✅ Generate tests tự động
3. ✅ Measure code coverage
4. ✅ So sánh automated vs manual tests

**Chúc mừng! Bạn đã hoàn thành Experiment 3!** 🎉

