# Import can library
import can
# Import gmail api file 
import gmailApi
# import mysql.connctor
import mysql.connector

# to transform timestamp to datetime format 
from datetime import datetime

# seach messages and return position if it exist
def search(list, data):
	for i in range(len(list)):
		if list[i]["code"] == data:
			return i
	return -1

# mysql connection define

mydb = mysql.connector.connect(
  host="mysqlhost",
  user="admin",
  password="password",
  database="database"
)

error_codes = [
{"code":0xc0ffee,"sended":False,"desc":"Description 1","critical":True},
{"code":0x1ff400a,"sended":False,"desc":"Description 2","critical":True},
{"code":0xffa500a,"sended":False,"desc":"Description 3","critical":False},
{"code":0xb0ffaa,"sended":False,"desc":"Description 4","critical":False},
{"code":0x1faf00a,"sended":False,"desc":"Description 5","critical":False},
]
patent_test = "XXXX00"
cursor =  mydb.cursor()

# can interface definition
can_interface = 'vcan0'
# canbus definition
bus = can.interface.Bus(can_interface, bustype='socketcan')

# infinity loop
while(1):
	# searching can messages every 200ms
    message = bus.recv(0.2)

    if message is None:
        print('Timeout occurred, no message.')
    else:
    	#transform can timestamp to datetime string 
    	formatDate =  datetime.fromtimestamp(message.timestamp).strftime("%Y-%m-%d %H:%M:%S")
    	# transform id_error from integer to hex format
    	id_error = hex(message.arbitration_id)
    	# compare can data to error_codes 
    	data_error = message.data[1]	
    	
    	# search if error code exist
    	idNum = search(error_codes,message.arbitration_id)
    	# if message contains errors (it assumes that the error message comes from the byte[1]
    	if(idNum>=0 and  data_error >= 0x1): 
    		if(error_codes[idNum]["sended"] == False):
        		sql =  "INSERT INTO auto (Patente,Codigo_error,Descripcion_error,Fecha_error) values (%s,%s,%s,%s)"
        		varss =  (patent_test,id_error,error_codes[idNum]["desc"],formatDate)
        		cursor.execute(sql,varss)
        		mydb.commit()
        		error_codes[idNum]["sended"] = True
        		if(error_codes[idNum]["critical"] == True):   
        			send_message(service, "email@email.com", "Correo de prueba", 
            email_template + email_body.format(patent_test,id_error,error_codes[idNum]["desc"]), [])     
