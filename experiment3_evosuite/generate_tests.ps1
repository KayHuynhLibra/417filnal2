# PowerShell script to generate tests with EvoSuite
# Usage: .\generate_tests.ps1

Write-Host "=== EvoSuite Test Generation Script ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Compile project
Write-Host "[1/4] Compiling project..." -ForegroundColor Yellow
mvn clean compile
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Compilation failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Compilation successful" -ForegroundColor Green
Write-Host ""

# Step 2: Generate tests for Calculator
Write-Host "[2/4] Generating tests for Calculator..." -ForegroundColor Yellow
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.Calculator `
  -Dsearch_budget=60 `
  -Dassertion_timeout=120 `
  -Dminimization_timeout=120

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Calculator test generation had issues" -ForegroundColor Yellow
} else {
    Write-Host "✅ Calculator tests generated" -ForegroundColor Green
}
Write-Host ""

# Step 3: Generate tests for StringUtils
Write-Host "[3/4] Generating tests for StringUtils..." -ForegroundColor Yellow
java -jar evosuite-1.2.0.jar `
  -projectCP target/classes `
  -class edu.iastate.coms417.demo.StringUtils `
  -Dsearch_budget=60 `
  -Dassertion_timeout=120 `
  -Dminimization_timeout=120

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  StringUtils test generation had issues" -ForegroundColor Yellow
} else {
    Write-Host "✅ StringUtils tests generated" -ForegroundColor Green
}
Write-Host ""

# Step 4: Copy generated tests to src/test/java
Write-Host "[4/4] Copying generated tests..." -ForegroundColor Yellow
if (Test-Path "evosuite-tests\edu\iastate\coms417\demo") {
    New-Item -ItemType Directory -Path "src\test\java\edu\iastate\coms417\demo" -Force | Out-Null
    Copy-Item -Recurse -Force "evosuite-tests\edu\iastate\coms417\demo\*" "src\test\java\edu\iastate\coms417\demo\"
    Write-Host "✅ Tests copied to src/test/java" -ForegroundColor Green
} else {
    Write-Host "⚠️  No generated tests found in evosuite-tests/" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "=== Next Steps ===" -ForegroundColor Cyan
Write-Host "1. Review generated tests in src/test/java/" -ForegroundColor White
Write-Host "2. Run: mvn test" -ForegroundColor White
Write-Host "3. Generate coverage: mvn jacoco:report" -ForegroundColor White
Write-Host "4. View report: target/site/jacoco/index.html" -ForegroundColor White

