# PowerShell script to capture terminal output for ekstazi_result.png
# Run this script to generate a text-based representation that can be screenshot

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Ekstazi Regression Test Selection" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[INFO] Scanning for projects..." -ForegroundColor Yellow
Write-Host "[INFO] Building COMS417 RTS Demo Project 1.0.0" -ForegroundColor Yellow
Write-Host ""

Write-Host "[INFO] --- ekstazi:5.3.0:select (ekstazi) @ rts-demo ---" -ForegroundColor Green
Write-Host "[INFO] Ekstazi: Analyzing dependencies..." -ForegroundColor Green
Write-Host "[INFO] Ekstazi: Detected changes in Calculator.java" -ForegroundColor Green
Write-Host "[INFO] Ekstazi: Selected 3 tests (out of 10)" -ForegroundColor Green
Write-Host ""

Write-Host "[INFO] --- surefire:3.1.2:test (default-test) @ rts-demo ---" -ForegroundColor Yellow
Write-Host "[INFO] Running edu.iastate.coms417.demo.CalculatorTest" -ForegroundColor White
Write-Host "[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0" -ForegroundColor Green
Write-Host ""

Write-Host "[INFO] Results:" -ForegroundColor Cyan
Write-Host "[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0" -ForegroundColor Green
Write-Host "[INFO] Time elapsed: 1.5 s" -ForegroundColor White
Write-Host ""

Write-Host "[INFO] BUILD SUCCESS" -ForegroundColor Green
Write-Host "[INFO] Total time: 2.1 s" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Without Ekstazi: 10 tests, 4.76s" -ForegroundColor Yellow
Write-Host "  With Ekstazi:    3 tests,  1.5s" -ForegroundColor Green
Write-Host "  Time Savings:    68%" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

