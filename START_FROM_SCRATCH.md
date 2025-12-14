# 🚀 Bắt Đầu Lại Từ Đầu - COMS/SE 417 Final Project

## 📋 Tổng Quan

File này hướng dẫn bạn **bắt đầu lại từ đầu** toàn bộ project COMS/SE 417 về Continuous Integration Testing với Regression Test Selection (RTS).

---

## 🎯 Project Structure

```
final/
├── experiment1_custom_demo/      # Experiment 1: Custom Demo với Ekstazi
├── experiment2_apache_csv/       # Experiment 2: Apache Commons CSV
├── experiment3_evosuite/         # Experiment 3: EvoSuite Test Generation
├── report.tex                     # LaTeX report chính
└── README.md                      # Overview
```

---

## ✅ Prerequisites

### 1. Java

**Cần**: Java 8, 17, hoặc 22

**Kiểm tra**:
```powershell
java -version
```

**Cài đặt nếu chưa có**:
- Java 17: https://adoptium.net/
- Hoặc dùng Java 8/22 đã có

### 2. Maven

**Cần**: Maven 3.6+

**Kiểm tra**:
```powershell
mvn -version
```

**Cài đặt nếu chưa có**:
1. Download: https://maven.apache.org/download.cgi
2. Giải nén vào folder (ví dụ: `D:\tools\apache-maven-3.9.11`)
3. Thêm vào PATH:
```powershell
$env:PATH += ";D:\tools\apache-maven-3.9.11\bin"
```

### 3. Git (Optional)

Để clone repository hoặc push changes.

---

## 📦 Bước 1: Setup Môi Trường

### 1.1: Verify Java và Maven

```powershell
# Check Java
java -version
# Should show: java version "X.x.x"

# Check Maven
mvn -version
# Should show: Apache Maven 3.x.x
```

### 1.2: Set JAVA_HOME (Nếu cần)

```powershell
# Windows PowerShell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Verify
java -version
```

---

## 🧪 Bước 2: Chạy Experiment 1 (Custom Demo)

### 2.1: Vào folder

```powershell
cd experiment1_custom_demo
```

### 2.2: Compile và Test

```powershell
# Setup Maven nếu chưa có trong PATH
$env:PATH += ";D:\COMS417\final\tools\apache-maven-3.9.11\bin"

# Run tests
mvn clean test
```

### 2.3: Kết quả mong đợi

```
Tests run: 10, Failures: 0, Errors: 0
BUILD SUCCESS
```

### 2.4: Xem kết quả

- Test results: `target/surefire-reports/`
- README: `README.md`

---

## 📚 Bước 3: Chạy Experiment 2 (Apache CSV)

### 3.1: Vào folder

```powershell
cd ..\experiment2_apache_csv
```

### 3.2: Compile và Test

```powershell
# Run tests (skip RAT check)
mvn test "-Drat.skip=true"
```

**Lưu ý**: Có thể có 3 test failures (do Windows environment), đây là bình thường.

### 3.3: Kết quả mong đợi

```
Tests run: 923, Failures: 3, Errors: 0
BUILD SUCCESS (hoặc FAILURE do 3 failures - OK)
```

### 3.4: Xem kết quả

- Test results: `target/surefire-reports/`
- Analysis: `TEST_RESULTS_JAVA8.md`

---

## 🤖 Bước 4: Chạy Experiment 3 (EvoSuite)

### 4.1: Vào folder

```powershell
cd ..\experiment3_evosuite
```

### 4.2: Đọc hướng dẫn

```powershell
# Xem file hướng dẫn
Get-Content START_FROM_SCRATCH.md
```

### 4.3: Generate Tests

```powershell
# Setup Java 17
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Chạy script
.\generate_tests.ps1
```

### 4.4: Run Tests và Coverage

```powershell
mvn test jacoco:report
start target/site/jacoco/index.html
```

### 4.5: Kết quả mong đợi

- Generated tests: `src/test/java/`
- Coverage report: `target/site/jacoco/index.html`
- Coverage: 70-90%

---

## 📄 Bước 5: Build LaTeX Report

### 5.1: Cài đặt LaTeX (Nếu chưa có)

- **Windows**: MiKTeX hoặc TeX Live
- **Mac**: MacTeX
- **Linux**: `sudo apt-get install texlive-full`

### 5.2: Compile Report

```powershell
cd ..
pdflatex report.tex
# Hoặc dùng editor như Overleaf, TeXstudio
```

### 5.3: Xem Report

File PDF: `report.pdf`

---

## 🔍 Bước 6: Verify Tất Cả Experiments

### Checklist:

- [ ] ✅ Experiment 1: Tests chạy thành công (10 tests)
- [ ] ✅ Experiment 2: Tests chạy (923 tests, 3 failures OK)
- [ ] ✅ Experiment 3: Generated tests và coverage report
- [ ] ✅ Report PDF được tạo

---

## 🛠️ Troubleshooting

### Vấn đề 1: "mvn: command not found"

**Giải pháp**:
```powershell
# Thêm Maven vào PATH
$env:PATH += ";D:\COMS417\final\tools\apache-maven-3.9.11\bin"
mvn -version
```

### Vấn đề 2: "invalid target release: 17"

**Giải pháp**:
```powershell
# Dùng Java 17
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
java -version
```

### Vấn đề 3: "Cannot find pom.xml"

**Giải pháp**: Đảm bảo đang ở đúng folder:
```powershell
# Check current directory
Get-Location
# Should be: D:\COMS417\final\experimentX
```

### Vấn đề 4: Experiment 2 có failures

**Giải pháp**: Đây là **bình thường**! 3 failures do Windows environment:
- `testCSV141Excel`: Line ending issue
- `JiraCsv196Test`: UTF-8 byte tracking

Xem `experiment2_apache_csv/TEST_RESULTS_JAVA8.md` để biết chi tiết.

---

## 📚 Tài Liệu Tham Khảo

### Experiment 1:
- `experiment1_custom_demo/README.md`
- `experiment1_custom_demo/CI_TEST_RESULTS.md`

### Experiment 2:
- `experiment2_apache_csv/README.md`
- `experiment2_apache_csv/TEST_RESULTS_JAVA8.md`

### Experiment 3:
- `experiment3_evosuite/START_FROM_SCRATCH.md`
- `experiment3_evosuite/README.md`
- `experiment3_evosuite/STEP_BY_STEP_GUIDE.md`

### Tổng quan:
- `EXPERIMENTS_README.md`
- `README.md`

---

## 🎯 Quick Start Commands

### Tất cả experiments:

```powershell
# Experiment 1
cd experiment1_custom_demo
mvn clean test
cd ..

# Experiment 2
cd experiment2_apache_csv
mvn test "-Drat.skip=true"
cd ..

# Experiment 3
cd experiment3_evosuite
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
.\generate_tests.ps1
mvn test jacoco:report
cd ..
```

---

## ✅ Hoàn Thành!

Sau khi hoàn thành tất cả các bước, bạn đã:

1. ✅ Setup môi trường (Java, Maven)
2. ✅ Chạy Experiment 1 (Custom Demo với Ekstazi)
3. ✅ Chạy Experiment 2 (Apache CSV)
4. ✅ Chạy Experiment 3 (EvoSuite)
5. ✅ Build LaTeX report

**Chúc mừng! Bạn đã hoàn thành toàn bộ project!** 🎉

---

## 📞 Cần Giúp Đỡ?

1. **Check logs**: Xem output của Maven
2. **Verify setup**: Đảm bảo Java và Maven đã setup đúng
3. **Read docs**: Xem README.md của từng experiment
4. **Clean rebuild**: `mvn clean compile test`

---

## 🔄 Bắt Đầu Lại

Nếu muốn **bắt đầu lại hoàn toàn**:

1. **Clean tất cả**:
```powershell
# Clean all target folders
Get-ChildItem -Recurse -Directory -Filter "target" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Directory -Filter ".ekstazi" | Remove-Item -Recurse -Force
```

2. **Theo lại từ Bước 1** trong file này

3. **Hoặc xem từng experiment**:
   - Experiment 1: `experiment1_custom_demo/README.md`
   - Experiment 2: `experiment2_apache_csv/README.md`
   - Experiment 3: `experiment3_evosuite/START_FROM_SCRATCH.md`

