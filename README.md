# ipcalc
A web-based IP Address/Subnet classifier

There are two builds here; one for CGI and one for Flask.

To use the CGI version, copy index.html and calc.cgi to a working web directory and then open in your browser. 
You must change the python path in calc.cgi!!

Flask version is coming soon!

The home page asks for an IP Address and subnet. The subnet can be in dotted-decimal or CIDR notation. The result will provide a plethora
of information; network ID, broadcast, host range, next & previous networks and more.

![](ipcalc/ipcalc.png)

![](https://github.com/collin-clark/ipcal/results.png)
