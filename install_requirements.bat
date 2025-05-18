@echo off
echo Installation des dépendances...

:: Vérifier si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé. Installe-le avant de continuer !
    pause
    exit /b
)

:: Installer les modules nécessaires
pip install requests

echo ✅ Installation terminée !
pause
