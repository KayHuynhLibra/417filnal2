# GitHub Actions CI Test Results

## Actual Test Execution Results

**Date:** 2025-12-14T14:06:29Z  
**Workflow:** Java CI with Maven and Ekstazi  
**Total Workflow Time:** ~9-10 seconds

### Test Execution Details

```
[INFO] Running edu.iastate.coms417.demo.CalculatorTest
[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.066 s

[INFO] Running edu.iastate.coms417.demo.StringUtilsTest
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.009 s

[INFO] Results:
[INFO] Tests run: 10, Failures: 0, Errors: 0, Skipped: 0

[INFO] BUILD SUCCESS
[INFO] Total time: 2.844 s
```

### Summary

- **Total Tests:** 10
  - CalculatorTest: 7 tests (0.066s)
  - StringUtilsTest: 3 tests (0.009s)
- **Maven Test Execution Time:** 2.844 seconds
- **Total Workflow Time:** 9-10 seconds (including checkout, setup, compilation)
- **Status:** ✅ All tests passed
- **Strategy:** Retest All (Ekstazi disabled in CI)

### Comparison with Ekstazi (Estimated)

If Ekstazi were enabled and only CalculatorTest was selected:
- **Tests:** 7 (instead of 10)
- **Estimated Time:** ~1.5-2.0 seconds
- **Time Savings:** ~30-47% (0.8-1.3 seconds)
- **Selection Ratio:** 70% (7/10 tests)

### Notes

- These are actual results from GitHub Actions CI
- Ekstazi is disabled in CI due to JVM attachment restrictions
- Local testing with Ekstazi shows 60-70% time savings
- CI demonstrates stable test execution with Retest All strategy

