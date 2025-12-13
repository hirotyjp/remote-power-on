# Turn on PC using Relay

As Wake-On-LAN doesn't work properly after Windows 11 is updated, I decided to use physical power on method using a relay module and PI.

## Requirements

- General relay module suing SRD-05VDC-SL-C (I bought it in Ali)
- Raspberry PI

## Connection

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
      
