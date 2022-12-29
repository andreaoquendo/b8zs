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

class SelectorWindow:

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
        self.host = tk.Button(self.window, command=lambda: self.create_host())
        self.host.configure(
            background="#b8c0ff",
            compound="none",
            cursor="based_arrow_down",
            overrelief="raised",
            text='host',
            width=7)
        self.host.pack(side="left")
        self.client_button = tk.Button(self.window, command=lambda: self.create_sender())
        self.client_button.configure(background="#b8c0ff", text='client', width=7)
        self.client_button.pack(side="bottom")

        self.window.title("Config")
        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()
    
    ## Creates a Sender Interface
    def create_sender(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.client.start(ip, int(port))
            self.window.destroy()
            self.host = MessageWindow('sender', self.server, self.client)
            self.host.run()
    
    ## Creates a Hosdt Interface
    def create_host(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.server.start(ip, int(port))
            self.window.destroy()
            self.host = MessageWindow('host', self.server, self.client)
            self.host.run()

class MessageWindow:

    def receive_message(self):
        # connection
        signal = self.server.receive_message()

        # line coding
        signal = self.b8.string_to_signal(signal)
        self.sig = signal
        binary = self.b8.decode(signal)

        # crypto
        #self.crypt.decodeVegenere(binary)
        self.binary_string = ''.join([str(item) for item in binary])
        self.vegenere = self.crypt.binary_to_string(self.binary_string)
        self.message = self.crypt.get_original_message(self.vegenere)
        
        #interface
        self.updateText()

        # graphic
        plt.step(list(range(len(signal))), signal)
        plt.show()

    def send_message(self):
        self.message = self.message_input.get()
        self.vegenere = self.crypt.get_encrypted_message(self.message)
        binary_message = self.crypt.convert_to_binary(self.vegenere)
        self.binary_string = ''.join([str(item) for item in binary_message])
        self.sig = self.b8.encode(binary_message)

        #interface
        self.updateText()

        # connection
        self.client.send_message(self.b8.signal_to_string(self.sig))

    def updateText(self):
        if self.fun == 'host':
             text = f"Signal: { self.sig }\nBinary: { self.binary_string } \nEncrypted Message: { self.vegenere }\nMessage: { self.message } "
        else:
            text = f"Message: { self.message } \nEncrypted Message: { self.vegenere }\nBinary: { self.binary_string } \nSignal: { self.sig }"
        self.message_data.delete("1.0","end")
        self.message_data.insert(tk.END, text)


    def __init__(self, fun, server, client, ip=0, port=0, master=None, ):
        # get connection values
        self.ip = ip
        self.port = port

        self.server = server
        self.client = client

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
            self.button.configure(background="#b8c0ff", text='Receive', command=lambda: self.receive_message())
        else:
            self.button.configure(background="#b8c0ff", text='Send', command=lambda: self.send_message())
        
        self.button.pack(side="top")

        self.messageWindow.title(fun)

        # Main widget
        self.mainwindow = self.messageWindow

    def run(self):

        self.mainwindow.mainloop()
        