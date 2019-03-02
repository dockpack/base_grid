#!/bin/bash -e
if [ ! -f selenium-server-standalone-3.141.59.jar ]
then
    wget "https://bit.ly/2TlkRyu"
fi
HUB_URL=http://localhost:4444
java -jar selenium-server-standalone-3.141.59.jar -role node -hub $HUB_URL -nodeConfig "$(uname).json"
read -r
