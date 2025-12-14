# PowerShell Script để capture terminal output

Write-Host "`n=== HƯỚNG DẪN CHỤP TERMINAL OUTPUT ===" -ForegroundColor Cyan

Write-Host "`nBước 1: Chạy tests không Ekstazi" -ForegroundColor Yellow
Write-Host "cd coms417" -ForegroundColor White
Write-Host "mvn clean test" -ForegroundColor White
Write-Host "`n→ Chụp output (Win + Shift + S)" -ForegroundColor Green
Write-Host "→ Lưu: coms417/images/terminal_without_ekstazi.png" -ForegroundColor Green

Write-Host "`nBước 2: Enable Ekstazi (uncomment trong pom.xml)" -ForegroundColor Yellow
Write-Host "→ Chạy: mvn clean test (lần đầu)" -ForegroundColor White
Write-Host "→ Chụp output" -ForegroundColor Green
Write-Host "→ Lưu: coms417/images/terminal_ekstazi_first.png" -ForegroundColor Green

Write-Host "`nBước 3: Sửa code và chạy lại" -ForegroundColor Yellow
Write-Host 'echo "// Modified" >> src/main/java/edu/iastate/coms417/demo/Calculator.java' -ForegroundColor White
Write-Host "mvn test" -ForegroundColor White
Write-Host "`n→ Chụp output (có Ekstazi: selected 3 tests)" -ForegroundColor Green
Write-Host "→ Lưu: coms417/images/terminal_ekstazi_selected.png" -ForegroundColor Green

Write-Host "`n✅ Hoàn thành! Có 3 ảnh terminal output" -ForegroundColor Green

