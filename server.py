import socket  # Import socket module
import os
from flask import Flask
import requests

username = ["Mohamed", "Ahmed"]
password = ["01234", "56789"]
user = ''
pw = ''
authenflag = '0'

BUFFER_SIZE = 4096

s = socket.socket()  # Create a socket object
host = '0.0.0.0'  # Get local machine name
port = int(os.environ.get("PORT", 5000))  # Reserve a port for your service.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))  # Bind to the port
s.listen(120)  # Now wait for client connection.

print('Server listening....')

while True:

    conn, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    user = conn.recv(1024).decode()
    pw = conn.recv(1024).decode()
    for x in username:
        if user == x:
            if pw == password[username.index(x)]:
                authenflag = '1'
    conn.send(authenflag.encode())
    if authenflag == '1':                                     #authentication successful
        folder = os.getcwd() + '\\' + user                  #get current directory
        if not os.path.exists(folder):        #if folder doesn't exist
            os.mkdir(user)                                  #create the file
            print("Directory ", user, " Created ")
        else:
            print("Directory ", user, " already exists")
        filename = conn.recv(1024).decode()                 #recieve file name
        print(folder+'\\'+filename)
        f = open(folder+'\\'+filename, 'rb')
        l = f.read(BUFFER_SIZE)
        while (l):
            conn.sendall(l)
            l = f.read(BUFFER_SIZE)
        f.close()
        print('Done sending')
    conn.close()
app = Flask(__name__)
@app.route("/")
def hello_world():
    print(requests.get('0.0.0.0'))
    return requests.get('0.0.0.0')
if __name__ == '__main__':
    flaskapp.run(debug=True)
