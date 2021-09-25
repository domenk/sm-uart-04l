# Amphenol Telaire SM-UART-04L for Python on Raspberry Pi

Telaire SM-UART-04L is a particulate dust sensor.

Resources:
* [Web site](https://www.amphenol-sensors.com/en/telaire/dust-sensors/3393-sm-uart-04l)
* [Data sheet](https://f.hubspotusercontent40.net/hubfs/9035299/Literature/AAS-916-139C-Telaire-SM-UART-04L_EN_043020-web.pdf)
* [Official code for Arduino](https://github.com/AmphenolAdvancedSensors/Telaire/tree/Dust-Sensor---Laser-Technology)
* Evaluation board [AAS-LDS-UNO](https://www.amphenol-sensors.com/en/telaire/509-accessories/3469-aas-lds-uno)

## Connector

You can use Samtec [ISDF-05-D](https://www.samtec.com/products/isdf-05-d) connector together with [CC03R-2830-01-GF](https://www.samtec.com/products/cc03r-2830-01-gf) crimp contact.

Also available is cable assembly [SFSDT](https://www.samtec.com/products/sfsdt) in various lengths (for example: [SFSDT-05-28-G-03.00-S](https://www.samtec.com/products/sfsdt-05-28-g-03.00-s) for 3 inch wires, ~ 7,6 cm).

## Connections

| Sensor       | Raspberry Pi      |
| ------------ | ----------------- |
| 1 5V         | 5 V               |
| 2 5V         | 5 V               |
| 3 GND        | Ground            |
| 4 GND        | Ground            |
| 5 RESET      | 3.3 V             |
| 6 NC         | --                |
| 7 RXD        | UART TX (GPIO 14) |
| 8 NC         | --                |
| 9 TXD        | UART RX (GPIO 15) |
| 10 SET/SLEEP | 3.3 V             |

Connect 100 nF, 22 μF and 220 μF capacitor between 5 V and ground per data sheet (page 3).
