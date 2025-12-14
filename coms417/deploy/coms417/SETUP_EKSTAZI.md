# Hướng dẫn Setup Ekstazi cho Apache Commons CSV

## Bước 1: Kiểm tra Maven đã cài đặt

Chạy lệnh sau để kiểm tra:
```bash
mvn --version
```

Nếu chưa có Maven, tải về từ: https://maven.apache.org/download.cgi

## Bước 2: Thêm Ekstazi Plugin vào pom.xml

Mở file `commons-csv/pom.xml` và thêm phần `<build>` nếu chưa có, hoặc thêm plugin vào phần `<build><plugins>` nếu đã có.

### Cách 1: Nếu pom.xml chưa có phần `<build>`

Thêm đoạn này vào trước thẻ `</project>`:

```xml
<build>
  <plugins>
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
  </plugins>
</build>
```

### Cách 2: Nếu pom.xml đã có phần `<build>`

Chỉ cần thêm plugin vào trong `<build><plugins>`:

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

## Bước 3: Chạy test lần đầu (Cold Start)

```bash
cd commons-csv
mvn clean test
```

Lần chạy đầu tiên, Ekstazi sẽ chạy TẤT CẢ test để xây dựng dependency graph. Ghi lại thời gian chạy.

## Bước 4: Sửa code và chạy lại test

1. Mở file `src/main/java/org/apache/commons/csv/CSVFormat.java`
2. Thêm một dòng comment hoặc log statement (ví dụ: `// Test modification`)
3. Lưu file
4. Chạy lại: `mvn test`

Lần này Ekstazi sẽ chỉ chạy các test liên quan đến file bạn vừa sửa!

## Bước 5: So sánh kết quả

Ghi lại:
- **Lần 1 (Cold start)**: Tất cả test, thời gian: ___ giây
- **Lần 2 (Sau khi sửa code)**: Số test được chọn: ___, thời gian: ___ giây
- **Tiết kiệm**: ___% thời gian

## Lưu ý

- Ekstazi lưu thông tin trong thư mục `.ekstazi/` (sẽ tự động tạo)
- Nếu muốn reset, xóa thư mục `.ekstazi/` và chạy lại `mvn clean test`

