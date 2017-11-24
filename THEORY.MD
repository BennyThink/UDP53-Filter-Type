## Basic Concepts ##
As I mentioned in `README.MD`, some hotspot will allow traffic via port 53 regardless of its packet format and protocol.
So, in order to test your hotspot's filter type, we could send a TCP/UDP request to a public server (remain non-login status), if we receive any kind of response, then it means we're lucky - setup and proxy service in port 53.
By the way, commonly Web Auth will allow 53(DNS) and 67/68(DHCP Server side and client side). So it's also a good idea to test against 67/68.

## TCP vs UDP ##
Okay, let's just assume that we all know what TCP and UDP is. DNS takes use of both TCP and UDP port of 53, by default we tend to use UDP 53; while DHCP takes use of UDP 67 for DHCP Server and UDP 68 for DHCP Client.
Basically the script tried to test against **TCP 53**. Further details will be discussed.

## Technical Details ##
### Code Explanation ###
The purpose is obvious, send request - receive response -> setup and proxy server.
In order to do this, we tried python socket.
For the code below:
```
sock_clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

```
we created a socket which is a typical TCP socket.
```
sock_clt.connect(('123.206.87.223', 53))
```
we connected to the designated host and port. In my example it's my own server.
Then we tried to catch the exception. Here comes the most marvelous part:
I caught `connection refused` exception. Yes, the server rejected client's request, this process means server sent some info to the client, and socket library threw exception, i.e. the communication was two-way.

### Why choose TCP instead of UDP ###
Here's the thing. Before a TCP transmission, we need to `connect` first, i.e. establish connection. However UDP does not need to do this. In UDP, we just need to send data to the server. Code:
```
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('data',('123.206.87.223',53))
```
And if any response, we could use `s.recvfrom(2028)`.
But here comes the problem: 
1.How could we know the server responses? This could be solve by invoking `recvfrom()` method. 
2.Then it must be a program running on that server, which has significantly complicated our job.

So, I decide to test against TCP 53 since DNS is TCP/UDP protocol.

### Server Requirements ###
My server will retire soon, by then this script may not work well. I'm going to explain which kind of server it needs(TCP 53)
The answer is quiet simple: Any server with public IP address that rejects TCP 53 connection would be enough.
To be more specific, 
1. Your server can't run any program that listens on TCP 53, e.g. Shadowsocks server.
2. You need to configure your firewall to allow TCP port 53. Since there's no program binding on TCP 53, kernel will refuse the connection. Or you could set `ufw reject proto tcp from any to any port 53`, the result will stay the same. `reject` sends response while `deny` doesn't. 

In a word, your server must refuse TCP 53 request whether it's implicitly (refuse by kernel) or explicit(refuse by firewall).

## Other details ##
To be continued.
