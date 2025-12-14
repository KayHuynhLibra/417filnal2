# 🚀 Quick Start - Experiment 3

## 3 Bước Đơn Giản

### 1️⃣ Setup Java 17

```powershell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"
```

### 2️⃣ Generate Tests

```powershell
cd experiment3_evosuite
.\generate_tests.ps1
```

### 3️⃣ View Results

```powershell
# Run tests
mvn test

# Generate coverage
mvn jacoco:report

# Open report
start target/site/jacoco/index.html
```

---

## 📚 Chi Tiết

Xem `STEP_BY_STEP_GUIDE.md` để biết chi tiết từng bước.

---

## ⚡ Nhanh Hơn

Nếu script không chạy, dùng commands thủ công:

```powershell
# Compile
mvn clean compile

# Generate Calculator tests
java -jar evosuite-1.2.0.jar -projectCP target/classes -class edu.iastate.coms417.demo.Calculator -Dsearch_budget=60

# Generate StringUtils tests  
java -jar evosuite-1.2.0.jar -projectCP target/classes -class edu.iastate.coms417.demo.StringUtils -Dsearch_budget=60

# Copy tests
Copy-Item -Recurse -Force "evosuite-tests\edu\iastate\coms417\demo\*" "src\test\java\edu\iastate\coms417\demo\"

# Run
mvn test jacoco:report
```

