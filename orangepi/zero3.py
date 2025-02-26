# -*- coding: utf-8 -*-
# Copyright (c) 2023 terindo

"""
******** Warning Developement ********
** dont use this file in production **

Alternative pin mappings for Orange PI Zero3
(see https://drive.google.com/file/d/1GelRJz-6Dg4i_EQ1SwrfHeqfLOPw9kdO/view for schematic)
Usage:
.. code:: python
   import orangepi.zero3
   from OPi import GPIO
   GPIO.setmode(orangepi.zero3.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero 3 physical board pin to GPIO pin
BOARD = {
    3:    229,   # PH5/I2C3_SDA
    5:    228,   # PH4/I2C3_SCK
    7:    73,    # PC9
    8:    226,   # PH2/UART5_TX
    10:   227,   # PH3/UART5_RX
    11:   70,    # PC6
    12:   75,    # PC11
    13:   69,    # PC5
    15:   72,    # PC8
    16:   79,    # PC15
    18:   78,    # PC14
    19:   231,   # PH7,SPI1_MOSI
    21:   232,   # PH8,SPI1_MISO
    22:   71,    # PC7
    23:   230,   # PH6,SPI1_CLK
    24:   233,   # PH9,SPI1_CS
    26:   74,    # PC10
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD