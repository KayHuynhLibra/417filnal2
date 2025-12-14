# COMS/SE 417 Final Project: Continuous Integration and Regression Test Selection

## Project Overview

This project demonstrates **Regression Test Selection (RTS)** using **Ekstazi** in a Continuous Integration (CI) environment. We show how RTS can reduce test execution time by 60-82% while maintaining test safety guarantees.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── maven.yml          # GitHub Actions CI workflow
├── coms417/                    # Maven project with Ekstazi
│   ├── pom.xml                # Maven configuration with Ekstazi plugin
│   ├── src/
│   │   ├── main/java/         # Source code
│   │   └── test/java/         # Test code
│   └── images/                # Diagrams and screenshots
├── report.tex                 # LaTeX report
└── README.md                  # This file
```

## Features

- ✅ **Regression Test Selection** using Ekstazi
- ✅ **GitHub Actions CI/CD** integration
- ✅ **Maven** build automation
- ✅ **JUnit 5** test framework
- ✅ **Comprehensive evaluation** with real-world examples

## Quick Start

### Prerequisites

- Java 17+
- Maven 3.6+

### Running Tests Locally

```bash
cd coms417
mvn test
```

### Running with Ekstazi

The project is already configured with Ekstazi. Simply run:

```bash
cd coms417
mvn test
```

Ekstazi will automatically select only affected tests based on code changes.

## GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/maven.yml`) that:

1. Sets up Java 17
2. Caches Maven dependencies
3. Caches Ekstazi's dependency graph
4. Runs tests with Maven

The workflow triggers on:
- Push to `main` or `master` branch
- Pull requests to `main` or `master` branch

## Results

Our evaluation shows:
- **Small projects (10 tests):** 60-70% time savings
- **Large projects (300+ tests):** 82% time savings
- **Selection accuracy:** 100% (no false negatives)

## Documentation

- See `coms417/README.md` for detailed setup instructions
- See `coms417/SETUP_EKSTAZI.md` for Ekstazi configuration
- See `report.tex` for the complete project report

## Authors

- Shubham Bhattacharya
- Brayden Hayworth
- Kim Sang Huynh
- Sam Rowland

## License

This project is for educational purposes (COMS/SE 417).
