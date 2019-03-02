@ECHO OFF
cd D:\Program Files\Selenium
SET HUB_URL=http://192.168.10.22:4444
java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig "Windows.json" -hub %HUB_URL%
@pause
