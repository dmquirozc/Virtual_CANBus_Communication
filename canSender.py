# import can library
import can 

# time library import
import time

# define can interface
can_interface = "vcan0" 

# define bus can interface
bus = can.interface.Bus(can_interface,bustype = "socketcan")

message_counter = 0

#error_code = [0xc0ffee, 0x1ff400a, 0xffa500a, 0xb0ffaa,0x1faf00a]
error_code = [0xc0ffea, 0x1ff400e, 0xffa500a, 0xb0ffaa,0x1faf00a]
# infinity loop
while(1):
	
	d = message_counter +1
	# message to send 
	msg = can.Message(arbitration_id=error_code[message_counter], data=[0, d, 0, 0, 0, 0, 0, 0], is_extended_id=True)
	# try to send the message
	try:
		bus.send(msg)
		# if the message was sent, increment counter
		message_counter = message_counter + 1
		
		# if all messages were send, reset counter
		if(message_counter == 5):
			message_counter = 0
		
		#wait 200ms between messages
		time.sleep(0.2)
	except can.CanError:
		print(f"Error sending MSG: {msg}")
	
