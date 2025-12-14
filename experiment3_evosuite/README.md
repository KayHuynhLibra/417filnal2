# Experiment 3: Automated Test Generation with EvoSuite

## 📋 Overview

This experiment demonstrates **Automated Test Generation** using **EvoSuite**, complementing the Regression Test Selection (RTS) approach shown in Experiments 1 and 2.

### Key Concepts

- **EvoSuite**: Automatically generates JUnit test suites for Java classes
- **Code Coverage**: Uses JaCoCo to measure test coverage
- **Test Quality**: Compares automatically generated tests vs manual tests

---

## 🎯 Objectives

1. Generate test cases automatically using EvoSuite
2. Measure code coverage with JaCoCo
3. Compare EvoSuite-generated tests with manual tests
4. Demonstrate complete CI/CD testing pipeline

---

## 📁 Project Structure

```
experiment3_evosuite/
├── pom.xml                          # Maven config with EvoSuite & JaCoCo
├── evosuite-1.2.0.jar               # EvoSuite tool (command line)
├── src/
│   ├── main/java/
│   │   └── edu/iastate/coms417/demo/
│   │       ├── Calculator.java     # Source class 1
│   │       └── StringUtils.java     # Source class 2
│   └── test/java/                   # Manual tests (optional)
└── evosuite-tests/                  # Generated tests (after running EvoSuite)
```

---

## 🚀 Quick Start

### Prerequisites

- Java 17+
- Maven 3.6+
- EvoSuite 1.2.0 (included in this folder)

### Step 1: Compile the Project

```bash
cd experiment3_evosuite
mvn clean compile
```

### Step 2: Generate Tests with EvoSuite

#### Option A: Using Command Line (Recommended)

```bash
# Generate tests for Calculator class
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.Calculator \
  -Dsearch_budget=60

# Generate tests for StringUtils class
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.StringUtils \
  -Dsearch_budget=60
```

#### Option B: Generate for All Classes

```bash
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -target target/classes \
  -Dsearch_budget=60
```

### Step 3: Copy Generated Tests

After generation, EvoSuite creates tests in `evosuite-tests/` directory. Copy them to `src/test/java/`:

```bash
# Windows PowerShell
Copy-Item -Recurse evosuite-tests\edu\iastate\coms417\demo\* src\test\java\edu\iastate\coms417\demo\

# Linux/Mac
cp -r evosuite-tests/edu/iastate/coms417/demo/* src/test/java/edu/iastate/coms417/demo/
```

### Step 4: Run Tests with Coverage

```bash
mvn test jacoco:report
```

### Step 5: View Coverage Report

Open `target/site/jacoco/index.html` in a browser.

---

## 📊 EvoSuite Options

### Common Options

| Option | Description | Example |
|--------|-------------|---------|
| `-projectCP` | Classpath to project classes | `target/classes` |
| `-class` | Specific class to test | `edu.iastate.coms417.demo.Calculator` |
| `-target` | Directory/JAR to test all classes | `target/classes` |
| `-Dsearch_budget` | Time budget in seconds | `60` (default: 120) |
| `-Dassertion_timeout` | Timeout for assertions | `120` |
| `-Dminimization_timeout` | Timeout for minimization | `120` |

### Advanced Options

```bash
# Generate with specific coverage criterion
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.Calculator \
  -Dcriterion=BRANCH \
  -Dsearch_budget=120

# Generate with MOSA algorithm
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.Calculator \
  -Dalgorithm=DynaMOSA \
  -Dsearch_budget=120
```

---

## 📈 Code Coverage Analysis

### View Coverage Report

After running `mvn test jacoco:report`, open:
```
target/site/jacoco/index.html
```

### Coverage Metrics

- **Line Coverage**: Percentage of lines executed
- **Branch Coverage**: Percentage of branches covered
- **Method Coverage**: Percentage of methods called

### Coverage Goals

The project is configured to require:
- **Minimum 50% line coverage** (configurable in `pom.xml`)

---

## 🔍 Comparing Generated vs Manual Tests

### EvoSuite-Generated Tests

**Characteristics**:
- ✅ High code coverage
- ✅ Edge case detection
- ✅ Regression assertions
- ⚠️ Less readable
- ⚠️ May include redundant tests

**Example Generated Test**:
```java
@Test
public void test01() throws Throwable {
    Calculator calculator0 = new Calculator();
    int int1 = calculator0.add(1, 1);
    assertEquals(2, int1);
}
```

### Manual Tests

**Characteristics**:
- ✅ More readable
- ✅ Better documentation
- ✅ Focused on business logic
- ⚠️ May miss edge cases
- ⚠️ Lower coverage potential

---

## 🎓 Learning Outcomes

After completing this experiment, you should understand:

1. **Automated Test Generation**: How EvoSuite generates tests
2. **Code Coverage**: How to measure and improve coverage
3. **Test Quality**: Trade-offs between automated and manual tests
4. **CI/CD Integration**: How to integrate test generation into CI pipeline

---

## 🔗 Integration with Other Experiments

### With Experiment 1 (Ekstazi RTS)

1. Generate tests with EvoSuite
2. Run tests with Ekstazi to select only affected tests
3. Compare: Full test suite vs RTS-selected tests

### With Experiment 2 (Apache CSV)

1. Generate additional tests for Apache Commons CSV
2. Measure coverage improvement
3. Use Ekstazi to optimize test execution

---

## 📚 References

- **EvoSuite**: http://www.evosuite.org/
- **EvoSuite Documentation**: http://www.evosuite.org/documentation/
- **JaCoCo**: https://www.jacoco.org/
- **Maven Plugin**: http://www.evosuite.org/documentation/maven-plugin/

---

## ⚠️ Troubleshooting

### Issue: EvoSuite not generating tests

**Solution**: 
- Check classpath: `-projectCP target/classes`
- Verify class name: Use full package name
- Increase search budget: `-Dsearch_budget=120`

### Issue: Generated tests don't compile

**Solution**:
- Ensure EvoSuite runtime is in classpath (already in `pom.xml`)
- Check Java version compatibility
- Clean and rebuild: `mvn clean compile`

### Issue: Coverage report not generated

**Solution**:
- Run `mvn test jacoco:report`
- Check `target/site/jacoco/index.html`
- Verify JaCoCo plugin is configured in `pom.xml`

---

## 📝 Next Steps

1. **Generate tests** for both Calculator and StringUtils
2. **Run coverage analysis** to see coverage metrics
3. **Compare** with manual tests from Experiment 1
4. **Integrate** with CI/CD pipeline (GitHub Actions)

---

## 🎯 Expected Results

- **Generated Tests**: ~20-50 tests per class
- **Coverage**: 70-90% line coverage
- **Test Execution**: 5-15 seconds
- **Report**: HTML coverage report in `target/site/jacoco/`

