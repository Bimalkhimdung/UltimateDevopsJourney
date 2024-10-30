import sys
from datetime import datetime
import socket
import argparse

def scan_port(target,ports):
    open_ports = []
    for port in ports:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

