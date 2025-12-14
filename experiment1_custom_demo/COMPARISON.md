# So sánh: Có Ekstazi vs Không có Ekstazi

## Tổng quan

Regression Test Selection (RTS) với Ekstazi giúp tối ưu hóa CI/CD pipeline bằng cách chỉ chạy những test cần thiết thay vì chạy toàn bộ test suite.

## Sự khác biệt chính

### 1. **Số lượng test được chạy**

#### ❌ **KHÔNG có Ekstazi (Retest All)**
- Chạy **TẤT CẢ** test cases mỗi lần
- Ví dụ: 300+ tests → Chạy hết 300+ tests
- Không phân biệt code nào thay đổi

#### ✅ **CÓ Ekstazi (RTS)**
- Chỉ chạy test **liên quan** đến code vừa sửa
- Ví dụ: Sửa 1 class → Chỉ chạy 5-10 tests liên quan
- Phân tích dependency tự động

### 2. **Thời gian chạy (Execution Time)**

#### ❌ **KHÔNG có Ekstazi**
```
Scenario: Sửa 1 dòng code trong Calculator.java
- Tổng số test: 10 tests
- Tests chạy: 10 tests (100%)
- Thời gian: ~6 giây
```

#### ✅ **CÓ Ekstazi**
```
Scenario: Sửa 1 dòng code trong Calculator.java
- Tổng số test: 10 tests
- Tests chạy: 3-4 tests (30-40%) - chỉ CalculatorTest
- Thời gian: ~2 giây
- Tiết kiệm: 60-70% thời gian
```

### 3. **Tài nguyên sử dụng (Resources)**

| Metric | Không có Ekstazi | Có Ekstazi | Tiết kiệm |
|--------|------------------|------------|-----------|
| CPU Usage | 100% | 30-40% | 60-70% |
| Memory | 100% | 30-40% | 60-70% |
| CI/CD Minutes | 100% | 30-40% | 60-70% |
| Developer Wait Time | 100% | 30-40% | 60-70% |

### 4. **Feedback Loop cho Developer**

#### ❌ **KHÔNG có Ekstazi**
```
Developer push code
    ↓
CI chạy TẤT CẢ tests (mất 5 phút)
    ↓
Nhận kết quả sau 5 phút
    ↓
Nếu fail → Fix → Chờ lại 5 phút
```

#### ✅ **CÓ Ekstazi**
```
Developer push code
    ↓
CI chạy CHỈ tests liên quan (mất 1 phút)
    ↓
Nhận kết quả sau 1 phút
    ↓
Nếu fail → Fix → Chờ lại 1 phút
→ Developer làm việc nhanh hơn 5 lần!
```

### 5. **Chi phí (Cost)**

Với dự án lớn chạy trên Cloud CI (GitHub Actions, GitLab CI, Jenkins):

#### ❌ **KHÔNG có Ekstazi**
- 100 commits/ngày × 5 phút/commit = 500 phút/ngày
- 500 phút × $0.008/phút = **$4/ngày**
- **$120/tháng** cho 1 project

#### ✅ **CÓ Ekstazi**
- 100 commits/ngày × 1 phút/commit = 100 phút/ngày
- 100 phút × $0.008/phút = **$0.80/ngày**
- **$24/tháng** cho 1 project
- **Tiết kiệm: $96/tháng (80%)**

## Ví dụ thực tế

### Scenario: Sửa bug trong `StringUtils.java`

#### Không có Ekstazi:
```bash
$ mvn test
[INFO] Running CalculatorTest      # ← Không cần!
[INFO] Running StringUtilsTest    # ← Cần
[INFO] Tests run: 10, Time: 6s
```

#### Có Ekstazi:
```bash
$ mvn test
[INFO] Ekstazi: Selected 3 tests (out of 10)
[INFO] Running StringUtilsTest    # ← Chỉ chạy test liên quan
[INFO] Tests run: 3, Time: 2s
```

## Khi nào nên dùng Ekstazi?

### ✅ **Nên dùng khi:**
- Project có **100+ tests**
- Team có **nhiều commits/ngày**
- CI/CD là **bottleneck**
- Muốn **giảm chi phí** cloud CI
- Cần **feedback nhanh** cho developers

### ❌ **Không cần khi:**
- Project nhỏ (< 50 tests)
- Test chạy rất nhanh (< 10 giây)
- Ít commits (1-2 lần/tuần)
- Không dùng cloud CI

## Kết luận

| Tiêu chí | Không có Tool | Có Ekstazi |
|----------|---------------|------------|
| **Tốc độ** | Chậm (chạy hết) | Nhanh (chọn lọc) |
| **Chi phí** | Cao | Thấp (tiết kiệm 60-80%) |
| **Developer Experience** | Chờ lâu | Feedback nhanh |
| **Scalability** | Không tốt | Tốt cho dự án lớn |
| **Setup** | Không cần | Cần config ban đầu |

**Kết luận:** Ekstazi là công cụ **bắt buộc** cho các dự án lớn muốn tối ưu CI/CD pipeline!

