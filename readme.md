What's this?
=====
This Python script is aimed to test your hostpot's interception/filter of UDP 53.

What's the purpose?
=====
The good news is, if your hostpot DOES NOT filter any kind of UDP 53 Packet<br>
you may wanna setup an OpenVPN server with UDP 53 in order to bypass Web Auth.

What's that IP Address?
=====
Wow, you got me! That IP is my server to perform the acknowledgement. It's a sad <br>
news I haven't found a public server that could meet my needs. So, don't DDoS it.

My test passed, how can I bypass Web Auth?
=====
Just simply setup an OpenVPN server with UDP Port 53. If you are newbee to this,<br>
simply [clike me](https://www.bennythink.com/udp53.html)for more info.

I don't have Python installed on my Windows!
=====
Well,you have to download and open the `dist` directory. By then you'll see an `udp.exe`.
Double-click it!

I want to comipile exe file by myself.
=====
Ok, install Python and corresponding version of py2exe.
Then cd to git directory, run:
`python "compile exe.py" py2exe`

Environment
=====
Windows/Linux with Python 2.7 test passed.

License
=====
Published under MIT License.
