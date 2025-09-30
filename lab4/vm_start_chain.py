#Dave Rodriguez
#https://github.com/jaripeo/ee250/tree/main/lab4

"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket


"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("daverodr/pong")
    client.message_callback_add("daverodr/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
   received_num = int(message.payload.decode())
   print(f"Pong - Received number: {received_num}")

   # Add 1 and publish back as ping
   new_num = received_num + 1
   time.sleep(1)  # Small delay for readability
   client.publish("daverodr/ping", str(new_num))
   print(f"Ping - Publishing number: {new_num}")



if __name__ == '__main__':

    """your code here"""
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python.
        
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="172.20.10.4", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(2)  # Give time to connect and subscribe
    
    # Start the ping-pong chain with an initial number
    initial_num = 1
    client.publish("daverodr/ping", str(initial_num))
    print(f"Starting ping-pong chain with number: {initial_num}")
    
    # Keep the program running to receive pong messages
    client.loop_forever()
        
       
        
        