#!/bin/bash

#Create Alias pyphotos
LINE='alias pyphotos="cd /data/data/com.termux/files/home/pyPhotos && pipenv run python run.py"'
FILE='/data/data/com.termux/files/usr/etc/bash.bashrc'
grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"


#Continue msg
echo ""
echo ""
echo ""
echo "Have you placed a valid client_id.json or auth.txt on the external storage root? This script will attempt to move these files to pyPhotos git cloned folder. "
TEXT='[Y/y] to proceed. [N/n] to exit'
echo ""
read -p "$TEXT" -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

#Ask for storage permission
echo ""
read -p "Grant storage permission (needed). Press Enter to ask"
termux-setup-storage
echo ""
read -p "Once permission is granted, press Enter to continue"

#Install packages and dependencies
pkg install openssl
pkg install python -y
pip install pipenv
pip install --upgrade pip
pipenv install

#Create shortcut
mkdir ~/.shortcuts
cp ~/pyPhotos/resources/launch_pyphotos.sh ~/.shortcuts

#Move client_id.json and auth.txt to pyPhotos
cp ~/pyPhotos/resources/client_id.json ./client_id.json
mv ~/storage/shared/client_id.json ~/pyPhotos
mv ~/storage/shared/auth.txt ~/pyPhotos

echo ""
read -p "Termux is required to restart... Press Enter to continue"
exit
