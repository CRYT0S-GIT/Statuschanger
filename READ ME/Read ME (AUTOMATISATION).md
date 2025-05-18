🚀 Générer un EXE avec PyInstaller
Ce guide explique comment convertir statuschanger.py en un fichier exécutable (.exe) sous Windows à l'aide de PyInstaller.

📥 Installation de PyInstaller
Avant de pouvoir créer l'exécutable, assure-toi que PyInstaller est installé.
Ouvre un terminal (CMD) et tape la commande suivante :


pip install pyinstaller


🔨 Créer un EXE sans console

Une fois PyInstaller installé, exécute cette commande dans le même dossier que statuschanger.py :


pyinstaller --onefile --noconsole statuschanger.py


🔍 Explication des options :


--onefile → Regroupe tous les fichiers nécessaires en un seul .exe.


--noconsole → Masque la console Windows (évite qu'une fenêtre noire s'ouvre).



📂 Où est le fichier .exe ?

Une fois la commande exécutée :

Un dossier dist/ sera créé.

Ton exécutable statuschanger.exe se trouvera à l'intérieur.
Déplace-le où tu veux et exécute-le !


⚠ Problèmes fréquents

🔴 "PyInstaller n'est pas reconnu"

➡ Vérifie que Python et pip sont bien installés en tapant :

python --version
pip --version



Si cela ne fonctionne pas, essaie :


python -m pip install pyinstaller


🔴 "Mon antivirus supprime l'EXE"

➡ Certains antivirus détectent les fichiers .exe générés comme suspects.
Ajoute une exception dans ton antivirus ou utilise --clean pour minimiser les faux positifs :


pyinstaller --onefile --noconsole --clean statuschanger.py


ℹ️ Support
Si tu rencontres un problème, contacte 632213356127846439 sur Discord ou rejoins le serveur :
➡ https://discord.gg/xhyMMgda8X