# Turn on PC using Relay

- Remove Jumper SW between JD-VCC and VCC
- Connection

      Raspberry Pi 3.3V -- VCC
      Raspberry Pi GND  -- GND
      Raspberry Pi GPIO17 -- IN1

      Raspberry Pi 5V -- JD-VCC
      * Do no connect GND *

      Relay COM ── PWR_SW(1)
      Relay NO  ── PWR_SW(2)
 
<img width="620" height="240" alt="image" src="https://github.com/user-attachments/assets/66abdec4-4761-4774-b316-7e6b0e3c5075" />
