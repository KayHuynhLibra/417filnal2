# Hướng dẫn từng bước: Triển khai Project COMS417

## Mục tiêu
Học và demo Regression Test Selection (RTS) với Ekstazi trong CI/CD pipeline.

---

## BƯỚC 1: Kiểm tra môi trường

### 1.1 Kiểm tra Java
```bash
java -version
```
**Kết quả mong đợi:** JDK 17 hoặc cao hơn
- Nếu chưa có: Tải từ https://adoptium.net/

### 1.2 Kiểm tra Maven
```bash
mvn --version
```
**Kết quả mong đợi:** Maven 3.6+ 
- Nếu chưa có: Xem file `MAVEN_SETUP.md` hoặc tải từ https://maven.apache.org/

### 1.3 Kiểm tra Git
```bash
git --version
```
**Kết quả mong đợi:** Git đã cài đặt

---

## BƯỚC 2: Clone và Setup Project

### 2.1 Clone repository
```bash
git clone https://github.com/KayHuynhLibra/coms417.git
cd coms417
```

### 2.2 Kiểm tra cấu trúc project
```bash
# Windows PowerShell
tree /F

# Linux/Mac
tree
```

**Cấu trúc mong đợi:**
```
coms417/
├── pom.xml
├── src/
│   ├── main/java/edu/iastate/coms417/demo/
│   │   ├── Calculator.java
│   │   └── StringUtils.java
│   └── test/java/edu/iastate/coms417/demo/
│       ├── CalculatorTest.java
│       └── StringUtilsTest.java
├── .github/workflows/maven.yml
└── README.md
```

---

## BƯỚC 3: Chạy test lần đầu (Baseline)

### 3.1 Clean và compile
```bash
mvn clean compile
```

**Kết quả mong đợi:**
```
[INFO] BUILD SUCCESS
```

### 3.2 Chạy test lần đầu (Cold Start)
```bash
mvn test
```

**Quan sát:**
- Tổng số test: 10 tests
- Thời gian chạy: ~4-6 giây
- Kết quả: Tất cả pass

**Ghi lại số liệu:**
```
Lần chạy 1 (Baseline):
- Tests chạy: 10/10 (100%)
- Thời gian: ___ giây
- Status: ✅ All pass
```

---

## BƯỚC 4: Thí nghiệm - Sửa code và chạy lại

### 4.1 Sửa code trong Calculator.java

Mở file: `src/main/java/edu/iastate/coms417/demo/Calculator.java`

**Tìm dòng:**
```java
public int add(int a, int b) {
    return a + b;
}
```

**Sửa thành (thêm comment):**
```java
public int add(int a, int b) {
    return a + b; // Modified for RTS demo
}
```

### 4.2 Chạy test lại (KHÔNG có Ekstazi)

```bash
mvn test
```

**Quan sát:**
- Tests chạy: Vẫn 10/10 tests (100%)
- Thời gian: ~4-6 giây (giống lần 1)
- **Vấn đề:** Chạy cả StringUtilsTest mặc dù không liên quan!

**Ghi lại:**
```
Lần chạy 2 (Sau khi sửa Calculator.java - KHÔNG có Ekstazi):
- Tests chạy: 10/10 (100%) ← Chạy lại TẤT CẢ
- Thời gian: ___ giây
- Status: ✅ All pass
- Vấn đề: Lãng phí chạy StringUtilsTest
```

---

## BƯỚC 5: Setup Ekstazi (Optional - Nâng cao)

### 5.1 Uncomment Ekstazi plugin trong pom.xml

Mở file `pom.xml`, tìm phần:
```xml
<!-- Ekstazi Plugin - Regression Test Selection -->
<!-- Uncomment to enable Ekstazi RTS... -->
<!--
<plugin>
    ...
</plugin>
-->
```

**Uncomment** (xóa `<!--` và `-->`):
```xml
<!-- Ekstazi Plugin - Regression Test Selection -->
<plugin>
    <groupId>org.ekstazi</groupId>
    <artifactId>ekstazi-maven-plugin</artifactId>
    <version>5.3.0</version>
    <executions>
        <execution>
            <id>ekstazi</id>
            <goals>
                <goal>select</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### 5.2 Chạy test với Ekstazi (Cold Start)

```bash
mvn clean test
```

**Lần này Ekstazi sẽ:**
- Chạy TẤT CẢ tests để học dependency
- Lưu thông tin vào `.ekstazi/` directory
- Thời gian: ~4-6 giây (giống baseline)

### 5.3 Sửa code lại và chạy với Ekstazi

**Sửa Calculator.java** (thêm 1 dòng log):
```java
public int add(int a, int b) {
    System.out.println("Adding: " + a + " + " + b); // Demo RTS
    return a + b;
}
```

**Chạy test:**
```bash
mvn test
```

**Quan sát với Ekstazi:**
- Tests chạy: Chỉ 3-4 tests (CalculatorTest)
- Thời gian: ~1.5-2 giây
- **Lợi ích:** Bỏ qua StringUtilsTest!

**Ghi lại:**
```
Lần chạy 3 (Sau khi sửa Calculator.java - CÓ Ekstazi):
- Tests chạy: 3-4/10 (30-40%) ← Chỉ CalculatorTest
- Thời gian: ___ giây
- Status: ✅ All pass
- Tiết kiệm: 60-70% thời gian!
```

---

## BƯỚC 6: So sánh kết quả

### 6.1 Tạo bảng so sánh

| Scenario | Tests chạy | Thời gian | Tiết kiệm |
|----------|------------|-----------|-----------|
| Baseline (lần 1) | 10/10 (100%) | ~5s | - |
| Sửa code - Không Ekstazi | 10/10 (100%) | ~5s | 0% |
| Sửa code - Có Ekstazi | 3-4/10 (30-40%) | ~2s | **60-70%** |

### 6.2 Tính toán tiết kiệm

```
Tiết kiệm thời gian = (Thời gian không Ekstazi - Thời gian có Ekstazi) / Thời gian không Ekstazi × 100%

Ví dụ:
= (5s - 2s) / 5s × 100%
= 60%
```

---

## BƯỚC 7: Setup GitHub Actions CI/CD

### 7.1 Kiểm tra workflow file

File `.github/workflows/maven.yml` đã có sẵn. Kiểm tra:
```bash
cat .github/workflows/maven.yml
```

### 7.2 Push lên GitHub

```bash
git add .
git commit -m "Add changes for RTS demo"
git push origin main
```

### 7.3 Xem kết quả trên GitHub

1. Vào: https://github.com/KayHuynhLibra/coms417
2. Click tab **"Actions"**
3. Xem workflow run mới nhất
4. Click vào để xem chi tiết

**Quan sát:**
- GitHub Actions tự động chạy `mvn test`
- Xem thời gian execution
- Xem logs để hiểu quá trình

---

## BƯỚC 8: Thí nghiệm với dự án lớn hơn (Optional)

### 8.1 Clone Apache Commons CSV

```bash
cd ..
git clone https://github.com/apache/commons-csv.git
cd commons-csv
```

### 8.2 Thêm Ekstazi vào pom.xml

Thêm plugin vào `<build><plugins>`:
```xml
<plugin>
    <groupId>org.ekstazi</groupId>
    <artifactId>ekstazi-maven-plugin</artifactId>
    <version>5.3.0</version>
    <executions>
        <execution>
            <id>ekstazi</id>
            <goals>
                <goal>select</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### 8.3 Chạy test baseline

```bash
mvn clean test
```

**Ghi lại:**
- Tổng số test: 300+ tests
- Thời gian: ~45-60 giây

### 8.4 Sửa code và chạy lại

Sửa file: `src/main/java/org/apache/commons/csv/CSVFormat.java`
- Thêm 1 dòng comment

Chạy lại:
```bash
mvn test
```

**Quan sát:**
- Tests chạy: Chỉ 5-15 tests (thay vì 300+)
- Thời gian: ~5-10 giây (thay vì 45-60s)
- **Tiết kiệm: 80-90%!**

---

## BƯỚC 9: Viết báo cáo

### 9.1 Thu thập số liệu

Từ các bước trên, bạn đã có:
- Số liệu baseline
- Số liệu không có Ekstazi
- Số liệu có Ekstazi
- Screenshots từ GitHub Actions

### 9.2 Cập nhật report.tex

Mở file `report.tex` và cập nhật phần **Evaluation** với số liệu thực tế:

```latex
\subsection{Results}

In the initial run (cold start), we executed all tests:
- Total tests: 10 tests
- Execution time: 4.75 seconds

After modifying Calculator.java:
- Without RTS: 10 tests, 4.76 seconds
- With Ekstazi: 3-4 tests, ~2 seconds
- Time savings: 60-70%
```

### 9.3 Compile PDF

```bash
pdflatex report.tex
pdflatex report.tex  # Chạy 2 lần để fix references
```

---

## Checklist hoàn thành

- [ ] Bước 1: Kiểm tra môi trường (Java, Maven, Git)
- [ ] Bước 2: Clone và setup project
- [ ] Bước 3: Chạy test baseline
- [ ] Bước 4: Thí nghiệm sửa code (không Ekstazi)
- [ ] Bước 5: Setup Ekstazi (optional)
- [ ] Bước 6: So sánh kết quả
- [ ] Bước 7: Setup GitHub Actions
- [ ] Bước 8: Thí nghiệm với dự án lớn (optional)
- [ ] Bước 9: Viết báo cáo

---

## Troubleshooting

### Lỗi: "mvn not found"
- Giải pháp: Xem `MAVEN_SETUP.md` hoặc thêm Maven vào PATH

### Lỗi: "Java version not supported"
- Giải pháp: Cài JDK 17 hoặc cao hơn

### Lỗi: Ekstazi không hoạt động
- Giải pháp: Xem `EKSTAZI_NOTES.md` hoặc bỏ qua (project vẫn chạy được)

### Lỗi: GitHub Actions fail
- Giải pháp: Kiểm tra `.github/workflows/maven.yml` và logs trên GitHub

---

## Tài liệu tham khảo

- `README.md` - Tổng quan project
- `COMPARISON.md` - So sánh có/không Ekstazi
- `SETUP_EKSTAZI.md` - Hướng dẫn setup Ekstazi
- `MAVEN_SETUP.md` - Hướng dẫn setup Maven
- `EKSTAZI_NOTES.md` - Notes về Ekstazi

---

## Kết luận

Sau khi hoàn thành các bước trên, bạn sẽ:
1. ✅ Hiểu cách RTS hoạt động
2. ✅ Thấy rõ sự khác biệt có/không có Ekstazi
3. ✅ Có số liệu thực tế để viết báo cáo
4. ✅ Có GitHub Actions workflow chạy tự động
5. ✅ Sẵn sàng demo cho giáo sư/TA

**Chúc bạn thành công! 🎉**

