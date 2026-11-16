name: Build EXE
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install pyTelegramBotAPI pyautogui pillow pyinstaller
      - name: Build with PyInstaller
        run: pyinstaller --onefile --noconsole bot.py
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: bot-exe
          path: dist/bot.exe
