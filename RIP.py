#Design and implement a 'routing demon' that operates in three stages
#Beginning -> read a config file containing:
#     Unique identification for demon instance
#     Input port numbers
#     Specifications for outputs
#Intermediate -> Create UDP sockets (according to # of input ports) and bind socket to port
#     No sockets for outputs
#Final -> Enter infinite loop, to react to incoming events. Events are either:
#     routing packet received from peer
#     timer event 
#Config file specifications:
#Program is run on a single command line parameter. The parameter = filename of config file. Config file
#should be an ascii file. Config file allows user to set:
#     Router ID: unique to each router (between 1 - 64000)
#     Input port numbers: set of numbers that listen for incoming packets
#           Port numbers within (1024,64000)
#     Output: specify 'contact info' for neighboured routers
#           Suggested format: 5000-5-4 -> 5001 (port number) 5 (metric value of link) 4 (router id of peer router)
#                             Each output separated by commas
#If one is missing form config file, error be raised and handled accordingly.

#Implement split-horizon with poisoned reverse
#Implement triggered updates only when routes become invalid, not for other updates
#DO NOT implement request messages
#Version number is always 2
#Do not multicast response messages, just send to intended peer through input port
#RIP Packet format changes:
#     IGnore network byte order
#     USe 16 bit all-zero fields in RIP header for router-id. Otherwise you would have no identification of the router sending updates
#     Packets should be constructed as byte-arrays
#If a demon has several input ports, it must listen simultaneously using select()

import select, socket, sys, time

LOCAL = '127.0.0.1'

def read_config(file):
    """reads contents of router configuration file"""

def create_rip_entry(afi, destination, metric):
    """creates a rip entry from the given parameters
    afi - address family identifiers
    destination - ip address for destined router
    metric - cost to reach destination
    """

def create_rip_packet():
    """creates a rip packet"""

def create_sockets(ports):
    """creates and binds sockets
    ports - ports given by config file
    """

def update(type, destination, sender, entries):
    """creates a triggered or periodic update
    type - either triggered or periodic
    destination - intended destination of packet
    sender - sender of update
    entries - """

def create_router(id, inputs, outputs):
    """creates a router based on information from config file
    id - router id
    inputs - valid input ports for router
    outputs - contact information, including:
                        input of peer router
                        metric value for link to peer router
                        router id of peer router
    """
