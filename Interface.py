#!/usr/bin/python3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Connection
from Server import Server
from Client import Client

# Line Coding
from Vegenere import Vegenere
from LineCode import B8ZS

# Plotting
import matplotlib.pyplot as plt

class selectorWindow:
    def createSender(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.client.start(ip, int(port))
            self.window.destroy()
            self.host = messageWindow('sender', self.server, self.client)
            self.host.run()
    
    def createHost(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.server.start(ip, int(port))
            self.window.destroy()
            self.host = messageWindow('host', self.server, self.client)
            self.host.run()


    def __init__(self, master=None):
        # Connection
        self.server = Server()
        self.client = Client()

        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.window.configure(
            background="#e7c6ff",
            height=200,
            padx=30,
            pady=30,
            width=200)
        self.ip = tk.Label(self.window)
        self.ip.configure(
            background="#e7c6ff",
            font="{poppins} 10 {}",
            text='IP address:')
        self.ip.pack(side="top")
        self.ip_input = tk.Entry(self.window)
        self.ip_input.pack(side="top")
        self.port = tk.Label(self.window)
        self.port.configure(
            background="#e7c6ff",
            compound="center",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Port:')
        self.port.pack(side="top")
        self.port_input = tk.Entry(self.window)
        self.port_input.pack(side="top")
        self.host = tk.Button(self.window, command=lambda: self.createHost())
        self.host.configure(
            background="#b8c0ff",
            compound="none",
            cursor="based_arrow_down",
            overrelief="raised",
            text='host',
            width=7)
        self.host.pack(side="left")
        self.client_button = tk.Button(self.window, command=lambda: self.createSender())
        self.client_button.configure(background="#b8c0ff", text='client', width=7)
        self.client_button.pack(side="bottom")

        self.window.title("Config")
        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()

class messageWindow:

    def receiveMessage(self):
        # connection
        signal = self.server.receiveMessage()

        # line coding
        signal = self.crypt.stringToSignal(signal)
        self.sig = signal
        binary = self.b8.decode(signal)
        self.crypt.decodeVegenere(binary)
        self.binaryString = ''.join([str(item) for item in binary])
        self.vegenere = self.crypt.convertToString()
        self.message = self.crypt.getDecryptographedMessage()
        
        #interface
        self.updateText()

        plt.step(list(range(len(signal))), signal)
        #plt.show(block=False)
        #plt.interactive(True)
        plt.show()

    def sendMessage(self):
        self.message = self.message_input.get()
        self.crypt.encodeVegenere(self.message)
        self.vegenere = self.crypt.getCryptographedMessage()
        binary = self.crypt.convertBinary()
        self.binaryString = ''.join([str(item) for item in binary])
        self.sig = self.b8.encode(binary)

        #interface
        self.updateText()

        # connection
        self.client.sendMessage(self.crypt.signalToString(self.sig))

    def updateText(self):
        if self.fun == 'host':
             text = f"Signal: { self.sig }\nBinary: { self.binaryString } \nEncrypted Message: { self.vegenere }\nMessage: { self.message } "
        else:
            text = f"Message: { self.message } \nEncrypted Message: { self.vegenere }\nBinary: { self.binaryString } \nSignal: { self.sig }"
        self.message_data.delete("1.0","end")
        self.message_data.insert(tk.END, text)


    def __init__(self, fun, server, client, ip=0, port=0, master=None, ):
        # get connection values
        self.ip = ip
        self.port = port

        self.server = server
        self.client = client

        print('ip: ', ip)
        print('port: ', int(port))
        self.info = ''
        self.fun = fun

        self.crypt = Vegenere()
        self.b8 = B8ZS()
        
        # build ui
        self.messageWindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.messageWindow.configure(
            background="#e7c6ff", height=200, width=200)
        self.title = tk.Label(self.messageWindow)
        self.title.configure(background="#e7c6ff", text='Message Data')
        self.title.pack(side="top")
        self.message_data = tk.Text(self.messageWindow)
        self.message_data.configure(height=20, width=100)
        self.message_data.pack(side="top")
        

        if fun != 'host':
            self.m_title = tk.Label(self.messageWindow)
            self.m_title.configure(background="#e7c6ff", text='Message')
            self.m_title.pack(side="top")
            self.message_input = tk.Entry(self.messageWindow)
            self.message_input.configure(width=50)
            self.message_input.pack(side="top")

        self.button = tk.Button(self.messageWindow)
        if fun == 'host':      
            self.button.configure(background="#b8c0ff", text='Receive', command=lambda: self.receiveMessage())
        else:
            self.button.configure(background="#b8c0ff", text='Send', command=lambda: self.sendMessage())
        
        self.button.pack(side="top")

        self.messageWindow.title(fun)

        # Main widget
        self.mainwindow = self.messageWindow

    def run(self):

        self.mainwindow.mainloop()
        