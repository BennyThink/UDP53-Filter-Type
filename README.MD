## What's this? ##
This Python script is aimed to test your hotspot's interception/filter of UDP 53. Besides, DHCP(67/68) is also a good option.

## What's the purpose? ##

The good news is, if your hotspot DOES NOT filter any kind of UDP 53 Packet,
you may want to setup an OpenVPN server with UDP 53 in order to bypass Web Auth so you could surf the internet without paying fees.
**Sometimes under some rare conditions the test just went wrong, so you may wanna test it a few times to make it more accurate.** 

## What's that IP Address? ##
That IP is my server to perform the response. It's a sad 
news I haven't found a public server that could meet my needs(check [THEORY.MD](THEORY.MD) for more info).
By the way, this server is about to close(in a few months). I'm looking for alternatives.


## Quick Start ##
### If you have Python ###
```
git clone https://github.com/BennyThink/UDP53-Filter-Type
cd UDP53-Filter-Type
python UDP53.py
```
### If not... ###
(For Windows user only) Download and open the `dist` directory. By then you'll see an `udp.exe`.
Double-click it!

### If you have Python...Option 2 ###
Fire up a terminal, type `python` and enter:
```
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('123.206.87.223', 53))
```
If you see complains about `connection refuse`, then try OpenVPN.

## My test passed, how can I bypass Web Auth? ##
Just simply setup an OpenVPN server with UDP Port 53. If you are newbie to this, 
simply [click me](https://www.bennythink.com/udp53.html) for more info.



## I want to build exe file by myself. ##
Ok, install Python and corresponding version of [pyinstaller](https://sourceforge.net/projects/pywin32/files/pywin32/).
Then run `build_exe.cmd`, you would get an single exe file.

## Environment ##
Windows/Linux with Python 2.7 test passed.
Also support Python 3.6
## See Also ##
[error code](ERROR_CODE.MD)

[theory](THEORY.MD)
## License ##
Published under MIT License.
