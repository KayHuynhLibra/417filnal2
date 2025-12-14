# Cách Enable Ekstazi cho Local Development

## Hiện tại

Ekstazi plugin đã bị comment out trong `pom.xml` để tránh lỗi trong CI environment.

## Để Enable Ekstazi Local

### Bước 1: Uncomment Plugin trong pom.xml

Mở file `coms417/pom.xml` và tìm section:

```xml
<!-- Ekstazi Plugin - Regression Test Selection -->
<!--
<plugin>
    <groupId>org.ekstazi</groupId>
    <artifactId>ekstazi-maven-plugin</artifactId>
    <version>5.3.0</version>
    <executions>
        <execution>
            <id>ekstazi-select</id>
            <phase>process-test-classes</phase>
            <goals>
                <goal>select</goal>
            </goals>
        </execution>
    </executions>
</plugin>
-->
```

**Uncomment** (bỏ `<!--` và `-->`):

```xml
<!-- Ekstazi Plugin - Regression Test Selection -->
<plugin>
    <groupId>org.ekstazi</groupId>
    <artifactId>ekstazi-maven-plugin</artifactId>
    <version>5.3.0</version>
    <executions>
        <execution>
            <id>ekstazi-select</id>
            <phase>process-test-classes</phase>
            <goals>
                <goal>select</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### Bước 2: Chạy Tests

```bash
cd coms417

# Lần 1: Build dependency graph (chạy tất cả tests)
mvn clean test
# Kết quả: 10 tests, ~4.67s

# Sửa Calculator.java
echo "// Modified" >> src/main/java/edu/iastate/coms417/demo/Calculator.java

# Lần 2: Với Ekstazi (chỉ chạy tests liên quan)
mvn test
# Kết quả: 3-4 tests, ~1.5s ⚡
```

## Kết quả Mong Đợi

- **Lần đầu**: 10 tests, ~4.67s (build dependency graph)
- **Lần sau**: 3-4 tests, ~1.5s (chỉ tests liên quan)
- **Tiết kiệm**: 60-70% thời gian

## Lưu ý

- **Không commit** pom.xml với Ekstazi enabled (sẽ gây lỗi CI)
- Chỉ enable khi test local
- Xem kết quả trong `COMPARISON.md` và `DEMO_RESULTS.md`

