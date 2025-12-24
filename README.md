# Turn on PC using Relay

Wake-On-LAN had been working well in my PC previously, but it suddenly didn't work properly after Windows update updated something. I was struggling to find out the root cause with changing NIC and WoL configuration, but finally I gave up. 
Now I decided to use physical power on method using a relay module and PI. I can say this way is more reliable than WoL.

<img width="663" height="472" alt="image" src="https://github.com/user-attachments/assets/467d92f9-1cbc-447b-9333-2510c239df92" />

## Requirements

- General relay module using SRD-05VDC-SL-C (I bought it in Ali)
- Raspberry PI

## Connections

      Raspberry Pi 3.3V -- VCC
      Raspberry Pi GND  -- GND
      Raspberry Pi GPIO17 -- IN1

      Raspberry Pi 5V -- JD-VCC
      * Remove Jumper SW between JD-VCC and VCC and do not connect GND 

      Relay COM ── PWR_SW(1)
      Relay NO  ── PWR_SW(2)

Image:

<img width="620" height="240" alt="image" src="https://github.com/user-attachments/assets/66abdec4-4761-4774-b316-7e6b0e3c5075" />


## Installation

      vi /usr/local/bin/relay_safe_high.py
      chmod +x /usr/local/bin/relay_safe_high.py

      cd /etc/systemd/system
      vi relay-safe-high.service

      # enable daemon
      systemctl daemon-reload
      systemctl enable relay-safe-high
      systemctl start relay-safe-high
      systemctl status relay-safe-high

      # check if GPIO17 is HIGH
      raspi-gpio get 17
      > GPIO 17: level=1 fsel=1 func=OUTPUT
      
## Usage

      # Just run
      ./power-on.py

