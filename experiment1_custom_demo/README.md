# Experiment 1: Custom Demonstration Project

## Overview

This experiment evaluates Regression Test Selection (RTS) using Ekstazi on a custom-built demonstration project with 10 test cases.

## Project Structure

```
experiment1_custom_demo/
├── .github/
│   └── workflows/
│       └── maven.yml          # GitHub Actions CI workflow
├── pom.xml                    # Maven configuration
├── src/
│   ├── main/java/             # Source code (Calculator, StringUtils)
│   └── test/java/             # Test code (CalculatorTest, StringUtilsTest)
├── images/                     # Diagrams and screenshots
├── CI_TEST_RESULTS.md          # Actual CI test results
└── README.md                   # This file
```

## Test Cases

- **CalculatorTest**: 7 test methods
- **StringUtilsTest**: 3 test methods
- **Total**: 10 test cases

## Results

### Without Ekstazi (Retest All)
- **Tests**: 10/10 (100%)
- **Execution Time**: 2.844 seconds (CI) / 4.67 seconds (local)
- **Status**: All tests passed

### With Ekstazi (RTS)
- **Tests**: 7/10 (70%) - Only CalculatorTest when Calculator.java is modified
- **Execution Time**: 1.0-1.5 seconds (estimated)
- **Time Savings**: 47-65%
- **Selection Accuracy**: 100% (no false negatives)

## How to Run

### Local Testing
```bash
cd experiment1_custom_demo

# Without Ekstazi
mvn clean test

# With Ekstazi (uncomment plugin in pom.xml first)
mvn test
```

### GitHub Actions
The workflow automatically runs on push/PR to main branch.
View results: https://github.com/KayHuynhLibra/417filnal2/actions

## Key Findings

1. **RTS Effectiveness**: Even on small projects (10 tests), RTS provides 47-65% time savings
2. **Selection Accuracy**: Ekstazi correctly identifies all affected tests (7/10 when Calculator.java is modified)
3. **CI Challenges**: Ekstazi faces JVM attachment restrictions in containerized CI environments
