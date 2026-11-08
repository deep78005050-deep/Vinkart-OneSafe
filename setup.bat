@echo off
title Vinkart OneSafe Auto Setup
powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%userprofile%\Desktop\Vinkart OneSafe.lnk'); $Shortcut.TargetPath = 'http://localhost:8080'; $Shortcut.Save()"
python app.py
pause
