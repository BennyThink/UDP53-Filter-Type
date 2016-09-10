What's this?
====
Error code when testing.

Error code when you may wanna try OpenVPN
====
Linux
-----
`[Errno 111] Connection refused`

Windows
-----
`socket.error: [Errno 10061]`

Error code when you may try DNS Tunnel
====
Linux
-----
`socket.error: [Errno 110] Connection timed out`
Windows 
----- 
`socket.error: [Errno 10060]`

Error code when You are offline
=====
Windows
-----
`socket.error: [Errno 10065]`
Linux
-----
This seemed to be the same with `[Errno 111] Connection refused`