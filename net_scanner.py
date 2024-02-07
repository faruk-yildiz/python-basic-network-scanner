import scapy.all
from optparse import OptionParser


# Arp Request 
# Broadcast
# Response

def get_user_input():
    optParser=OptionParser()
    optParser.add_option("-r","--range",dest="ip_range",help="ip range to scan")
    return optParser.parse_args()

def request():
    (user_input,arguments)=get_user_input()
    arp_request=scapy.all.ARP(pdst=user_input.ip_range) 
    broadcast=scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast/arp_request
    (answered,unanswered)=scapy.all.srp(combined_packet,timeout=1)
    print(answered.summary())

request()
#scapy help
#scapy.ls(scapy.ARP())
