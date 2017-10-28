What's this?
=====
This Python script is aimed to test your hostpot's interception/filter of UDP 53. Besides, DHCP is also a good option for this kind of work.

What's the purpose?
=====
The good news is, if your hostpot DOES NOT filter any kind of UDP 53 Packet,
you may wanna setup an OpenVPN server with UDP 53 in order to bypass Web Auth so you could surf the internet without paying fees.
**Sometimes under some rare conditions the test just went wrong, so you may wanna test it a few times to make it more accurate.** 

What's that IP Address?
=====
Wow, you got me! That IP is my server to perform the acknowledgement. It's a sad 
news I haven't found a public server that could meet my needs. So, don't DDoS it.

My test passed, how can I bypass Web Auth?
=====
Just simply setup an OpenVPN server with UDP Port 53. If you are newbee to this, 
simply [clike me](https://www.bennythink.com/udp53.html) for more info.

I don't have Python installed on my Windows!
=====
Well,you have to download and open the `dist` directory. By then you'll see an `udp.exe`.
Double-click it!

I want to build exe file by myself.
=====
Ok, install Python and corresponding version of py2exe.
Then cd to git directory, run:
`python build_exe.py py2exe`

Environment
=====
Windows/Linux with Python 2.7 test passed.
Also support Python 3.6

License
=====
Published under MIT License.
