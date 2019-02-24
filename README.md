
# Webcam with ESP32-CAM and MicroPython

![Imgur](https://i.imgur.com/8v4lsjd.jpg)

See http://micropython.org/ for more information on MicroPython.

See https://github.com/tsaarni/micropython-with-esp32-cam/wiki for
instructions on how to build custom version of MicroPython for ESP32 with
OV2640 camera support.

MicroPython logo is by MicroPython project https://github.com/micropython/micropython/tree/master/logo.


## Installation

Install tools on development machine

    virtualenv -p python3 venv
    . venv/bin/activate
    pip install esptool adafruit-ampy pyserial


Install webcam

    export AMPY_PORT=/dev/ttyUSB0
    ampy put boot.py
    ampy put webcam.py


Connect UART to esp32 and start terminal console

    miniterm.py /dev/ttyUSB0 115200 --dtr 0   # normal mode


Install dependencies on esp32 by running following on console

    import upip
    upip.install('picoweb')  # tested with 1.5.2
    upip.install('micropython-ulogging')
    upip.install('ujson')




# Known problems

## uasyncio throws exception

Following exception is thrown by uasyncio

    Running on http://0.0.0.0:80/
    INFO:picoweb:642.000 <HTTPRequest object at 3f819b90> <StreamWriter <socket>> "GET /"
    Traceback (most recent call last):\r\n  File "<stdin>", line 25, in <module>
    File "/lib/picoweb/__init__.py", line 298, in run
    File "/lib/uasyncio/core.py", line 161, in run_forever
    File "/lib/uasyncio/core.py", line 136, in run_forever
    File "/lib/uasyncio/__init__.py", line 60, in remove_writer
    TypeError: function takes 2 positional arguments but 3 were given


workaround is to modify lib/uasyncio/__init__.py on the target

    --- lib/uasyncio/__init__.py.orig       2019-02-17 19:13:41.207015002 +0200
    +++ lib/uasyncio/__init__.py    2019-02-17 19:12:33.895297196 +0200
    @@ -57,7 +57,7 @@
             # and if that succeeds, yield IOWrite may never be called
             # for that socket, and it will never be added to poller. So,
             # ignore such error.
    -        self.poller.unregister(sock, False)
    +        self.poller.unregister(sock)

         def wait(self, delay):
             if DEBUG and __debug__:
