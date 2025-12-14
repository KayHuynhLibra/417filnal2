# COMS/SE 417 Final Project: Continuous Integration and Regression Test Selection

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-enabled-brightgreen)](https://github.com/KayHuynhLibra/coms417/actions)

## Project Overview

This project demonstrates the use of **Regression Test Selection (RTS)** using **Ekstazi** in a Continuous Integration environment. We evaluate the effectiveness of RTS by comparing test execution times with and without Ekstazi on the Apache Commons CSV library.

**Repository**: [https://github.com/KayHuynhLibra/coms417](https://github.com/KayHuynhLibra/coms417)

## Project Structure

```
coms417/
├── .github/
│   └── workflows/
│       └── maven.yml          # GitHub Actions CI/CD pipeline
├── report.tex                  # LaTeX report (main deliverable)
├── README.md                  # This file
├── SETUP_EKSTAZI.md           # Step-by-step Ekstazi setup guide
├── MAVEN_SETUP.md             # Maven installation guide
├── pom-ekstazi-example.xml    # Example Ekstazi plugin configuration
└── .gitignore                 # Git ignore rules
```

## Setup Instructions

### Prerequisites
- Java JDK 17 or higher
- Maven 3.6+ (see [MAVEN_SETUP.md](MAVEN_SETUP.md) for installation)
- Git

### Local Setup

1. **Clone this repository:**
```bash
git clone https://github.com/KayHuynhLibra/coms417.git
cd coms417
```

2. **Clone the Apache Commons CSV repository** (for experimentation):
```bash
git clone https://github.com/apache/commons-csv.git
cd commons-csv
```

3. **Add Ekstazi plugin** to `pom.xml` (see [SETUP_EKSTAZI.md](SETUP_EKSTAZI.md) for detailed instructions)

4. **Run tests:**
```bash
mvn test
```

### GitHub Actions Setup

The `.github/workflows/maven.yml` file is already configured. Simply push to the repository and GitHub Actions will automatically:
- Run tests on every push/PR
- Cache Ekstazi data between runs
- Show execution time improvements

View the workflow runs: [Actions Tab](https://github.com/KayHuynhLibra/coms417/actions)

## Results

Our evaluation showed:
- **Without RTS**: All 300+ tests executed, taking ~45 seconds
- **With Ekstazi**: Only 12 tests executed after a minor change, taking ~8 seconds
- **Time savings**: 82% reduction in test execution time

## Report

The complete project report is available in `report.tex`. To compile:

```bash
pdflatex report.tex
```

## Team Members

- Shubham Bhattacharya
- Brayden Hayworth
- Kim Sang Huynh
- Sam Rowland

## References

See the full report (`report.tex`) for complete references and methodology.

## Additional Resources

- [Ekstazi Documentation](http://www.ekstazi.org/)
- [Apache Commons CSV](https://commons.apache.org/proper/commons-csv/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

