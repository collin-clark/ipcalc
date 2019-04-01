#! C:\Users\243607\AppData\Local\Programs\Python\Python37-32\python.exe
############################################
# A simple Subnet Calculator using netaddr.
# Copy index.html and calc.cgi to a folder
# under your www root. Open with the 
# browser of your choice.
#
# Version 1.0
# Author: Collin Clark
############################################

import cgi, cgitb, pprint
from netaddr import *
cgitb.enable()

def htmlTop():
	print("""Content-type:text/html\n\n
				<!DOCTYPE html>
				<html lang="en">
					<head>
						<meta charset="utf-8"/>
						<title> Subnet Calculator </title>
					</head>
					<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<div class="col-md-12">
					<form class="form-horizontal">
					<fieldset>
					""")
					
def htmlTail():
	print("""</font></body>
		</fieldset>
		</form>
		</html>
		""")					
		
	
if __name__ == "__main__":
	try:
		htmlTop()
		# Get the subnet and mask from the form				
		form = cgi.FieldStorage()
		ipaddr = form.getvalue('ipaddy')
		
		    
		# Convert a dotted decimal subnet mask into CIDR notation
		try:	
			convert_mask = ipaddr.split(" ")
			cidr_mask = IPAddress(convert_mask[-1]).netmask_bits()
			ipaddr = convert_mask[0] + '/' + str(cidr_mask)
		except:
			pass

       		
       # Import the subnet and mask into netaddr
		ipnet = IPNetwork(ipaddr)
		# Build out the results webpage and assign it to a variable that we 
		# can easily print out later
		
		custom_html = """
		<br>
		<div class="container">
		<div class="header clearfix">
		<nav>
		<ul class="nav nav-pills float-right">
		<li class="nav-item">
		<a class="nav-link active" href="./">Another subnet <span class="sr-only">(current)</span></a>
		</li>
		</ul>
		</nav>
		<h2 class="text-muted">%s</h2>
		<hr>
		</div>

		<div class="row marketing">
		<div class="col-lg-6">
		<h4>Network</h4>
		<p><h6><span class="badge badge-success">Network ID</span> %s</h6>
		<h6><span class="badge badge-success">Broadcast</span> %s</h6></p>
		
		<h4>Subnet Mask</h4>
		<p><h6> <span class="badge badge-primary">Subnet Mask</span> %s</h6>
		<h6> <span class="badge badge-primary">CIDR</span> %s</h6>
		<h6> <span class="badge badge-primary">Wilcard Mask</span> %s</h6>
		</p>
		
		<h4>Hosts</h4>
		<p><h6> <span class="badge badge-info">Network Size</span> %s</h6>
		<h6> <span class="badge badge-info">Host Range</span> %s - %s</h6></p>
		</div>
		
		<div class="col-lg-6">
		<h4>Network Binary</h4>
		<p><h6> <span class="badge badge-secondary">Network ID</span> %s</h6></p>
		
		<h4>Subnet Mask Binary</h4>
		<p><h6> <span class="badge badge-warning">Subnet Mask</span> %s</h6></p>
		
		<h4>Neighboring Networks</h4>
		<p><h6> <span class="badge badge-dark">Previous 3 Subnets</span> %s, %s, %s</h6>
		<h6> <span class="badge badge-dark">Next 3 Subnets</span> %s, %s, %s</h6></p>
		
		</div>
		</div>
		
		</div> <!-- /container -->
		
		</body>
		</html>
		""" % (ipnet,ipnet.network,ipnet.broadcast,ipnet.netmask,ipnet.cidr,ipnet.hostmask,ipnet.size,ipnet[1],ipnet[-2],ipnet.network.bits(),ipnet.netmask.bits(),ipnet.next(-1),ipnet.next(-2),ipnet.next(-3),ipnet.next(1),ipnet.next(2),ipnet.next(3))

		print(custom_html)
		
		htmlTail()
	except:
		cgi.print_exception()
			
