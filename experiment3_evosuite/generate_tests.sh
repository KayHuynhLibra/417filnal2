#!/bin/bash
# Bash script to generate tests with EvoSuite
# Usage: ./generate_tests.sh

echo "=== EvoSuite Test Generation Script ==="
echo ""

# Step 1: Compile project
echo "[1/4] Compiling project..."
mvn clean compile
if [ $? -ne 0 ]; then
    echo "❌ Compilation failed!"
    exit 1
fi
echo "✅ Compilation successful"
echo ""

# Step 2: Generate tests for Calculator
echo "[2/4] Generating tests for Calculator..."
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.Calculator \
  -Dsearch_budget=60 \
  -Dassertion_timeout=120 \
  -Dminimization_timeout=120

if [ $? -ne 0 ]; then
    echo "⚠️  Calculator test generation had issues"
else
    echo "✅ Calculator tests generated"
fi
echo ""

# Step 3: Generate tests for StringUtils
echo "[3/4] Generating tests for StringUtils..."
java -jar evosuite-1.2.0.jar \
  -projectCP target/classes \
  -class edu.iastate.coms417.demo.StringUtils \
  -Dsearch_budget=60 \
  -Dassertion_timeout=120 \
  -Dminimization_timeout=120

if [ $? -ne 0 ]; then
    echo "⚠️  StringUtils test generation had issues"
else
    echo "✅ StringUtils tests generated"
fi
echo ""

# Step 4: Copy generated tests to src/test/java
echo "[4/4] Copying generated tests..."
if [ -d "evosuite-tests/edu/iastate/coms417/demo" ]; then
    mkdir -p src/test/java/edu/iastate/coms417/demo
    cp -r evosuite-tests/edu/iastate/coms417/demo/* src/test/java/edu/iastate/coms417/demo/
    echo "✅ Tests copied to src/test/java"
else
    echo "⚠️  No generated tests found in evosuite-tests/"
fi
echo ""

echo "=== Next Steps ==="
echo "1. Review generated tests in src/test/java/"
echo "2. Run: mvn test"
echo "3. Generate coverage: mvn jacoco:report"
echo "4. View report: target/site/jacoco/index.html"

