#!/bin/bash

# fetch required files if not already existing
if ! pwd | grep -q 'workspace/discordbots'; then
    if ! [ -e ~/workspace/discordbots ]; then
        cd
        mkdir workspace
        cd workspace
        git clone --depth=1 "https://github.com/paperbenni/discordbots.git"
        cd discordbots
    else
        cd ~/workspace/discordbots
        git pull
    fi
fi

sudo pip3 install -r requirements.txt

# install systemd service
sudo cp discordbot.service /etc/systemd/system/discordbot.service
sudo chmod 644 /etc/systemd/system/discordbot.service
# enable and start service
sudo systemctl enable discordbot.service
sudo systemctl start discordbot.service
