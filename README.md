# Decode Transliterate

Initially created for a custom-made ERP system that failed to correctly register the orders made from the website when customers used Google's Translate for the whole page to Russian

Small Python tool that:

• Decodes HTML entities  
• Transliterates text to Latin

## New in v1.1.0

• Drag & Drop text  
• Clipboard paste button  
• Multi language transliteration  

## New in v1.2.0

• Clipboard monitoring for auto paste procedures  
• Shortcuts (ESC to clear text fields, CTRL+Q to exit)  
• Menu added for about and exit  

---

## Install

pip install -r requirements.txt

---

## Run GUI

python main.py

---

## Build EXE

pip install pyinstaller
pyinstaller --onefile --windowed main.py

---

## Test cyrillic word

&#1055&#1088&#1080&#1074&#1077&#1090