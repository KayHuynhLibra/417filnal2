# Maven đã được cài đặt thành công! ✅

## Thông tin cài đặt

- **Version**: Apache Maven 3.9.11
- **Location**: `D:\COMS417\final\tools\apache-maven-3.9.11`
- **Java**: JDK 22.0.1 (đã có sẵn)

## Sử dụng Maven

### Trong terminal hiện tại
Maven đã được thêm vào PATH cho session này, bạn có thể dùng ngay:
```bash
mvn --version
mvn test
```

### Trong terminal mới
Nếu mở terminal mới, bạn cần chạy lệnh này trước:
```powershell
$env:Path += ";D:\COMS417\final\tools\apache-maven-3.9.11\bin"
```

Hoặc **restart terminal** - PATH đã được lưu ở User level, terminal mới sẽ tự động nhận.

## Kiểm tra cài đặt

Chạy lệnh sau để xác nhận:
```bash
mvn --version
```

Bạn sẽ thấy:
```
Apache Maven 3.9.11
Maven home: D:\COMS417\final\tools\apache-maven-3.9.11
Java version: 22.0.1
```

## Bước tiếp theo

1. Vào thư mục `commons-csv`:
   ```bash
   cd D:\COMS417\final\commons-csv
   ```

2. Chạy test để kiểm tra project:
   ```bash
   mvn test
   ```

3. Thêm Ekstazi plugin (xem file `SETUP_EKSTAZI.md`)

## Lưu ý

- Maven đã được thêm vào PATH ở User level, nên sẽ hoạt động cho tất cả terminal mới
- Nếu gặp lỗi "mvn not found" trong terminal mới, hãy restart terminal hoặc chạy lệnh cập nhật PATH ở trên

