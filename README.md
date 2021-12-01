# Virtual CANBus Communication
Communicate 2 programs within a virtual CAN Bus and save data into a database using mysql-connector. 
If a message is detected as critial, also sends an email using Gmail API
This project is able to run in a Linux Machine. 
To set up the environment you need to install python-can and can-utils.

## Instalation
### Mysql
To install mysql-connector use pip:
```bash
pip install mysq-connector
```
or 
```bash
pip install mysq-connector-python
```
### Python CAN
To install python-can use pip:
```bash
pip install python-can
```
### Can Utils
To install can-utils you need to use apt:
```bash
sudo apt-get install can-utils
```
## Setup the environment.
### Virtual CAN
To set up a virtual CAN you need to run the commands:
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
This will create a virtual CAN bus, where you can send and read messages using CAN protocol.
### Mysql Database
In the file [canReder.py](https://github.com/dmquirozc/Virtual_CANBus_Communication/blob/main/canReader.py) you need to set the mysql credentials with your own database credentials.

```python

mydb = mysql.connector.connect(
  host="mysqlhost",
  user="admin",
  password="password",
  database="database"
)

```

### GMail API
To send Emails you need to setup your [Google Platform Console](https://cloud.google.com/) give access to Gmail API and download the credentias on a file called "credencials.json"
## Usage
### Sending messages on CAN Bus
With the file canSender.py you can send a variety of messages, you can define your own messages and dataframes. By default this script send 5 messages. 
To run this script just use python:
```bash
python canSender.py
```
or if you wanna run this on background
```bash
python canSender.py &
```

### Visualize CAN Bus
If you have installed can-utils, you can watch the messages on virtual can as follows:
```bash
candump vcan0
```
![candump vcan0](https://user-images.githubusercontent.com/32380955/144330227-0abd73d9-59d6-4bac-a1fb-b1cd623bf8bc.png)
### Analyze,store and alert CAN Bus data.
Finally, running the script canReader.py, you will be able to store data from CAN Bus on the database.
This script by default store different messages once, so you need to modify thescript if you want to store data multiple times.
Also the "critical" messages have the byte 1 defined as the trigger, if this trigger is >= 0, an email will be send.
```bash
python canReader.py
```
If you defined a message as critical and this message was detected with the trigger, you will receive an email linke this

![Default Email](https://user-images.githubusercontent.com/32380955/144330761-9f3d8ba3-0b88-45fc-b992-da7f5fc45419.png)
