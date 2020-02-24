#!/usr/bin/python
# -*- coding:utf-8 -*-
#developed by SystMX
#All rights reserved to systmx
#When modifying and distributing, leave the due credits

import socket
import os
import time
import sys

azul = '\033[34;1m'
verde = '\033[32;1m'
vermelho = '\033[31m'
original = '\033[0;0m'
os.system('reset')

def menu():
    banner = azul + '''
        +###############################+
        |  Port Scan v1.5               |
        |  date: 18/04/2017             |
        |  github: github.com/Elifelete |
        +###############################+
               
        [1]one port 
        [2]range of port's
        [3]list of port's
        [4]Exit
    '''
    print banner
    try:
        op = raw_input(verde + "Choose an option: ")
        if op == "1":
            option1()
        elif op == "2":
            option2()
        elif op == "3":
            option3()
        elif op == "4":
            print(vermelho + "Bye...")
            time.sleep(1)
            print(azul + "[✓] thanks [✓]")
            time.sleep(0.5)
        else:
            print vermelho + "\n   [✘] command invalid, returning to menu [✘]"
            time.sleep(3)
            os.system("reset")
            menu()
    except KeyboardInterrupt:
        print (vermelho + "\nYou press ctrl+c, exiting...")
        time.sleep(2)
        sys.exit()

def option1():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)
        ip = raw_input(verde + "\nEnter ip or Address: ")
        port = int(raw_input("Enter port: "))
        code = client.connect_ex((ip, port))
        if code == 0:
            print ""
            print verde + str(port) + ' -> Port open!'
        else:
            print ""
            print vermelho + str(port) + ' -> Port closed'

        print verde + '\n   ---> Scan Finalized <---'
        time.sleep(4)
        menu()

def option2():
    ip = raw_input("\nEnter the ip or address: ")
    port1 = int(raw_input("Home port: "))
    port2 = int(raw_input("End port: "))
    ports = range(port1, port2+1)
    print verde + "\n     ====================="
    print "          ✓ Scanning ✓    "
    print "     ====================="

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.15)
        code = client.connect_ex((ip, port))

        if code == 0:
            print ""
            print verde + (str(port) + " -> Port open")

    print verde + '\n   ---> Scan Finalized <---'
    time.sleep(4)
    menu()

def option3():
    ip = raw_input("\nEnter the ip or address: ")
    port = int(raw_input("Numbers of port: "))
    print ""

    ports = []
    count = 0

    while count < port:
        ports.append(int(raw_input("Port: ")))
        count += 1

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.15)
        code = client.connect_ex((ip, port))

        if code == 0:
            print ""
            print verde + (str(port) + " -> Port open")
        else:
            print ""
            print vermelho + (str(port) + " -> Port closed")
    print verde + '\n   ---> Scan Finalized <---'
    time.sleep(4)
    menu()

menu()
