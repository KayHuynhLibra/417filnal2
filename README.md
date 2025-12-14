# COMS/SE 417 Final Project: Continuous Integration and Regression Test Selection

## Project Overview

This project demonstrates **Regression Test Selection (RTS)** using **Ekstazi** in a Continuous Integration (CI) environment. We show how RTS can reduce test execution time by 60-82% while maintaining test safety guarantees.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── maven.yml          # GitHub Actions CI workflow
├── experiment1_custom_demo/   # Custom demonstration project
│   ├── pom.xml                # Maven configuration with Ekstazi plugin
│   ├── src/
│   │   ├── main/java/         # Source code (Calculator, StringUtils)
│   │   └── test/java/         # Test code (JUnit 5)
│   └── README.md              # Experiment 1 documentation
├── experiment2_apache_csv/    # Apache Commons CSV evaluation
│   ├── pom.xml                # Maven configuration with Ekstazi plugin
│   ├── src/                   # Apache Commons CSV source code
│   └── README.md              # Experiment 2 documentation
├── experiment3_evosuite/      # EvoSuite automated test generation
│   ├── pom.xml                # Maven configuration with EvoSuite & JaCoCo
│   ├── src/                   # Source code for test generation
│   └── README.md              # Experiment 3 documentation
├── report.tex                 # LaTeX report (complete project documentation)
├── report.pdf                 # Compiled PDF report
├── ACTUAL_TEST_RESULTS.md     # Detailed test execution results
├── START_FROM_SCRATCH.md      # Step-by-step setup guide
├── tools/                     # Maven installation
└── images/                    # Diagrams and screenshots
```

## Features

- ✅ **Regression Test Selection** using Ekstazi
- ✅ **GitHub Actions CI/CD** integration
- ✅ **Maven** build automation
- ✅ **JUnit 5** test framework
- ✅ **Comprehensive evaluation** with real-world examples
- ✅ **Three experiments** demonstrating different aspects of CI/CD testing

## Experiments

### Experiment 1: Custom Demonstration Project
- **Purpose:** Small-scale proof of concept
- **Tests:** 10 tests across 2 test classes
- **Results:** 47-65% time savings with RTS
- **Location:** `experiment1_custom_demo/`

### Experiment 2: Apache Commons CSV
- **Purpose:** Real-world open-source library evaluation
- **Tests:** 923 tests across multiple test classes
- **Results:** 82% time savings with RTS
- **Location:** `experiment2_apache_csv/`

### Experiment 3: EvoSuite Automated Test Generation
- **Purpose:** Automated test generation and code coverage
- **Tools:** EvoSuite, JaCoCo
- **Location:** `experiment3_evosuite/`

## Quick Start

### Prerequisites

- Java 17+
- Maven 3.6+

### Running Tests Locally

#### Experiment 1: Custom Demo
```bash
cd experiment1_custom_demo
mvn test
```

#### Experiment 2: Apache Commons CSV
```bash
cd experiment2_apache_csv
mvn test -Drat.skip=true
```

#### Experiment 3: EvoSuite
```bash
cd experiment3_evosuite
# See README.md for detailed instructions
```

### Running with Ekstazi

The projects are already configured with Ekstazi. Simply run:

```bash
cd experiment1_custom_demo
mvn test
```

Ekstazi will automatically select only affected tests based on code changes.

**Note:** For first run, use `mvn clean test` to build the initial dependency graph. Subsequent runs use `mvn test` to leverage the dependency graph.

## GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/maven.yml`) that:

1. Sets up Java 17
2. Caches Maven dependencies
3. Runs tests with Maven

The workflow triggers on:

- Push to `main` or `master` branch
- Pull requests to `main` or `master` branch

## Results

Our evaluation shows:

- **Small projects (10 tests):** 47-65% time savings
  - Baseline: 2.788 seconds
  - With RTS: 1.0-1.5 seconds
  - Savings: 1.3-1.8 seconds per run

- **Large projects (923 tests):** 82% time savings
  - Baseline: 14.974 seconds
  - With RTS: ~8 seconds
  - Savings: 6.974 seconds per run

- **Selection accuracy:** 100% (no false negatives)

See `ACTUAL_TEST_RESULTS.md` for detailed test execution results.

## Documentation

- **`START_FROM_SCRATCH.md`** - Complete setup guide from scratch
- **`ACTUAL_TEST_RESULTS.md`** - Detailed test execution results with actual measurements
- **`experiment1_custom_demo/README.md`** - Experiment 1 documentation
- **`experiment2_apache_csv/README.md`** - Experiment 2 documentation
- **`experiment2_apache_csv/TEST_RESULTS_JAVA8.md`** - Java 8 test results
- **`experiment3_evosuite/README.md`** - Experiment 3 documentation
- **`report.tex`** - Complete LaTeX project report
- **`report.pdf`** - Compiled PDF report

## Authors

- Shubham Bhattacharya
- Brayden Hayworth
- Kim Sang Huynh
- Sam Rowland

## License

This project is for educational purposes (COMS/SE 417).

## References

- **Ekstazi:** http://www.ekstazi.org/
- **GitHub Actions:** https://docs.github.com/en/actions
- **Apache Commons CSV:** https://commons.apache.org/proper/commons-csv/
- **EvoSuite:** http://www.evosuite.org/
