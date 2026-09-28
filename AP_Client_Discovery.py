"""
Wireless 802.11 client discovery with Scapy - Junior Python Developer Portfolio
Author: Thulasizwe Magagula
Purpose: Penetration Testing - Wireless Access Point Client Identification
Demonstrates working with scapy module, utilizating wireless monitoring mode on Linux
"""
from scapy.all import *
interface ='mon0'
probe_req = []
ap_name = raw_input("Enter the AP name ")
def probesniff(fm):
  if fm.haslayer(Dot11ProbeReq):
    client_name = fm.info
    if client_name == ap_name :
      if fm.addr2 not in probe_req:
        print "New Probe Request: ", client_name 
        print "MAC ", fm.addr2
        probe_req.append(fm.addr2)
sniff(iface= interface,prn=probesniff)
