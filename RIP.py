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
INPUTS_USED = []

def load_config(file):
    """reads contents of router configuration file and return information
    load_config will only check whether router-id and input are within range. other checks
    will be performed by other functions.
    file - config file to be read"""
    try:
        info_dict = {'router_id' : 0,
                     'inputs' : [],
                     'outputs' : []
                     }
        #read config file contents
        r_file = open(file, 'r')
        config = r_file.readlines()
        for each_line in config:
            line = each_line.split()

            #case: router id
            if line[0] == "router-id":
                #check if id in valid range
                try:
                    if int(line[1]) in range (1, 64001):
                        info_dict['router_id'] = int(line[1])
                    else: 
                        #id not in range
                        raise ValueError
                except(ValueError):
                    sys.exit("\n Error: Router ID {} not in range 1 - 64000".format(int(line[1])))

            #case: input ports
            elif line[0] == "input-ports":
                    for port in line[1:]:
                        #remove ','
                        num = port.replace(',', '')
                        #used for error
                        error_port = num
                        #check port in range
                        try:
                            if int(num) not in range(1024, 64001):
                                raise ValueError
                            else:
                                info_dict['inputs'].append(int(num))
                        except(ValueError):
                            sys.exit("\n Error: Port Number {} not in range 1024 - 64000".format(error_port))

            #case: outputs
            elif line[0] == "outputs":
                for output in line[1:]:
                    #remove ','
                    sequence = output.replace(',', '')
                    as_string = sequence.split('-')
                    #convert to int
                    as_int = [int(x) for x in as_string]
                    info_dict['outputs'].append(as_int)

        return info_dict
    
    except(ValueError):
        sys.exit("\n Error: Unknown configuration field")
    except(FileNotFoundError):
        sys.exit("\n Error: {} not found.".format(file))
    except:
        sys.exit("\n Error: Unknown Error Occured.")
        
def check_config(values):
    """checks validity of configuration values
    namely whether or not the inputs have been used or if any field of the outputs is invalid
    values - dictinoary containing values from the config file"""
    inputs = values['inputs']
    outputs = values['outputs']
    try:
        for input in inputs:
            if input in INPUTS_USED:
                raise RuntimeError
        for output in outputs:
            if output[0] not in range(1024, 64001):
                raise ValueError
            elif output[1] == INFINITY or 0:
                raise ValueError
            elif output[2] in inputs:
                return ValueError
    except(RuntimeError):
        sys.exit("\nError: Port number already taken.")
    except(ValueError):
        sys.exit("\nError: A field in Outputs is incorrect.")
    except:
        sys.exit("\nError: Unknown Error Occured.")
    
    return "Configuration File loaded Successfully"

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
