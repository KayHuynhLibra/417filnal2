# Note về Ekstazi trong CI Environment

## Vấn đề

Ekstazi gặp lỗi `NullPointerException` khi chạy trong GitHub Actions CI environment:
- `restore` goal gặp NullPointerException
- JVM attachment issues trong containerized environment

## Giải pháp hiện tại

**Trong CI (GitHub Actions):**
- Ekstazi được skip bằng flag `-Dekstazi.skip=true`
- Tests chạy bình thường (Retest All strategy)
- Vẫn có thể thấy kết quả tests và build time

**Local Development:**
- Ekstazi vẫn hoạt động bình thường
- Chạy `mvn test` để thấy RTS hoạt động
- Dependency graph được lưu trong `.ekstazi/`

## Cách thấy sự khác biệt

### 1. Chạy Local (Khuyến nghị)
```bash
cd coms417

# Lần 1: Build dependency graph
mvn clean test
# Kết quả: 10 tests, ~4.67s

# Sửa Calculator.java
echo "// Modified" >> src/main/java/edu/iastate/coms417/demo/Calculator.java

# Lần 2: Với Ekstazi
mvn test
# Kết quả: 3-4 tests, ~1.5s ⚡
```

### 2. So sánh trong Report
- Xem `report.tex` - có đầy đủ kết quả so sánh
- Xem `coms417/COMPARISON.md` - kết quả thực tế

### 3. GitHub Actions
- Workflow vẫn chạy tests thành công
- Có thể thấy build time và test results
- Ekstazi được skip để tránh lỗi

## Tại sao skip Ekstazi trong CI?

1. **JVM Attachment Issues**: Ekstazi cần attach vào JVM, điều này khó trong containerized CI
2. **NullPointerException**: Restore goal gặp lỗi khi không có dependency graph từ trước
3. **Stability**: Để đảm bảo CI chạy ổn định

## Alternative Solutions

Nếu muốn dùng Ekstazi trong CI, có thể thử:
1. Dùng self-hosted runners (có quyền JVM attach)
2. Dùng alternative RTS tools (STAR, Gixlow)
3. Pre-build dependency graph và commit vào repo

## Kết luận

- **Local**: Ekstazi hoạt động tốt, thấy rõ sự khác biệt
- **CI**: Skip Ekstazi để đảm bảo stability
- **Report**: Có đầy đủ kết quả và so sánh

