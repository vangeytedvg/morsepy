echo "Compiling GUI files (PyQt5 format)"
echo "Resource file"
pyrcc5 ui/images.qrc -o images_rc.py
echo "[+] Converting .ui files to .py files"
echo " |-> ui/main.ui to ui/main_form.py"
pyuic5 ui/main.ui -o ui/main_form.py
echo "[*] Done"
