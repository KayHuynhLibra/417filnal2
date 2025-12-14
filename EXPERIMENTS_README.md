# COMS/SE 417 Final Project - Experiments Package

## 📦 Project Organization

This project is organized into **2 main experiments** to evaluate Regression Test Selection (RTS) using Ekstazi:

---

## 📁 Experiment 1: Custom Demonstration Project
**Location**: `experiment1_custom_demo/`

### Overview
- **Purpose**: Small-scale proof of concept
- **Test Cases**: 10 tests (7 CalculatorTest + 3 StringUtilsTest)
- **Language**: Java 17
- **Build Tool**: Maven 3.9.11
- **Results**: 47-65% time savings with RTS

### Contents
- `pom.xml`: Maven configuration
- `src/`: Source and test code
- `.github/workflows/maven.yml`: CI workflow
- `CI_TEST_RESULTS.md`: Actual CI test results
- `images/`: Diagrams and screenshots
- `README.md`: Detailed documentation

### Quick Start
```bash
cd experiment1_custom_demo
mvn test
```

---

## 📁 Experiment 2: Apache Commons CSV
**Location**: `experiment2_apache_csv/`

### Overview
- **Purpose**: Real-world open-source library evaluation
- **Test Cases**: 300+ tests
- **Language**: Java 8+
- **Build Tool**: Maven
- **Results**: 82% time savings with RTS

### Contents
- `pom.xml`: Maven configuration (if Apache CSV is included)
- `src/`: Source and test code (if Apache CSV is included)
- `README.md`: Project information and setup instructions

### Quick Start
```bash
cd experiment2_apache_csv
# First, clone Apache Commons CSV if not present
git clone https://github.com/apache/commons-csv.git .
mvn test
```

---

## 📊 Results Summary

| Experiment | Project Size | Without RTS | With Ekstazi | Time Savings |
|------------|--------------|-------------|--------------|--------------|
| **1. Custom Demo** | 10 tests | 2.84s | 1.0-1.5s | 47-65% |
| **2. Apache CSV** | 300+ tests | 45s | 8s | 82% |

---

## 📄 Main Report

The complete project report is available in `report.tex` at the root directory.

## 🔗 GitHub Repository

- **Repository**: https://github.com/KayHuynhLibra/417filnal2
- **Actions**: https://github.com/KayHuynhLibra/417filnal2/actions

## 👥 Authors

- Shubham Bhattacharya
- Brayden Hayworth
- Kim Sang Huynh
- Sam Rowland

---

## 📝 Notes

- **Experiment 1** contains the complete custom demo project with CI integration
- **Experiment 2** contains Apache Commons CSV project (or setup instructions if not included)
- Both experiments demonstrate RTS effectiveness at different scales
- See individual README files in each experiment folder for detailed information
