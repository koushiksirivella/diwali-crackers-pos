@echo off
echo ========================================================
echo   DIWALI CRACKERS SMART PRICING & VERIFICATION SERVER
echo ========================================================
echo.
echo Opening browser on this PC: http://localhost:3000
echo For mobile phones on the same Wi-Fi/Hotspot, find this PC's IP address and open:
echo   http://^<YOUR_PC_IP^>:3000
echo.
timeout /t 2 >nul
start http://localhost:3000
python -m http.server 3000
