pyinstaller --onefile --distpath C:\Users\liam\Documents\code\python main.py
if %errorlevel% equ 0 (
    rmdir /s /q build
    del /f /q main.spec
    echo Build successful and cleanup complete.
) else (
    echo Build failed. Build folder and spec file retained for debugging.
)
pause