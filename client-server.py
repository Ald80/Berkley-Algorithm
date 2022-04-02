from dateutil import parser
import threading
import datetime
import socket
import time

def start_sending_time(slave_client):
    while True:
        slave_client.send(str(datetime.datetime.now()).encode())

        print("Recent time sent successfully", end="\n\n")

        time.sleep(5)

def start_receiving_time(slave_client):
    while True:
        
        synchronized_time = parser.parse(slave_client.recv(1024).decode())

        print("Synchronized time at the client is: " 
                + str(synchronized_time), end="\n\n")
        
def initiate_slave_client(port = 8080):

    slave_client = socket.socket()

    slave_client.connect(('127.0.0.1', port))

    print("Starting to receive time from server\n")
    send_time_thread = threading.Thread(
                                    target = start_sending_time,
                                    args = (slave_client, ))
    send_time_thread.start()

    print("Starting to receiving synchronized time from server\n")
    receive_time_thread = threading.Thread(
                                        target = start_receiving_time,
                                        args = (slave_client, ))
    receive_time_thread.start()

if __name__=="__main__":
    initiate_slave_client(port = 8080)