from flask import Flask, render_template, request

app = Flask(__name__)
from netaddr import *

@app.route('/')
def ipcalc():
    return render_template('ipcalc.html')

@app.route('/ipcalc_results')
def ipcalc_results():
    ipaddr = request.args.get('ipaddy')

    # Convert the CIDR subnetmask to dotted-decimal
    try:
        convert_mask = ipaddr.split(" ")
        cidr_mask = IPAddress(convert_mask[-1]).netmask_bits()
        ipaddr = convert_mask[0] + '/' + str(cidr_mask)
    except:
        pass

    # Import the network and subnet mask into netaddr and generate info
    ipnet = IPNetwork(ipaddr)
    ipnetnetwork = ipnet.network
    ipnetbroadcast = ipnet.broadcast
    ipnetnetmask = ipnet.netmask
    ipnetcidr = ipnet.cidr
    ipnethostmask = ipnet.hostmask
    ipnetsize = ipnet.size
    ipnetfirst = ipnet[1]
    ipnetlast = ipnet[-2]
    ipnetnetworkbits= ipnet.network.bits()
    ipnetnetmaskbits = ipnet.netmask.bits()
    ipnet_1 = ipnet.next(-1)
    ipnet_2 = ipnet.next(-2)
    ipnet_3 = ipnet.next(-3)
    ipnet1 = ipnet.next(1)
    ipnet2 = ipnet.next(2)
    ipnet3 = ipnet.next(3)
    supernets = ipnet.supernet(8)

    # Render the template and pass it the variables from this script
    return render_template('ipcalc_results.html',
        ipaddr=ipaddr,
        ipnet=ipnet,
        ipnetnetwork=ipnetnetwork,
        ipnetbroadcast=ipnetbroadcast,
        ipnetnetmask=ipnetnetmask,
        ipnetcidr=ipnetcidr,
        ipnethostmask=ipnethostmask,
        ipnetsize=ipnetsize,
        ipnetfirst=ipnetfirst,
        ipnetlast=ipnetlast,
        ipnetnetworkbits=ipnetnetworkbits,
        ipnetnetmaskbits=ipnetnetmaskbits,
        ipnet_1=ipnet_1,
        ipnet_2=ipnet_2,
        ipnet_3=ipnet_3,
        ipnet1=ipnet1,
        ipnet2=ipnet2,
        ipnet3=ipnet3,
        supernets=supernets)

# The development server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
