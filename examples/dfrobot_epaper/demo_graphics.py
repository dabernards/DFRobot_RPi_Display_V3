# -*- coding:GB18030 -*-
'''!
  @file demo_graphics.py
  @brief basic graphics demo, such as line, rectangle, triangle, circle and pixel��
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @License     The MIT License (MIT)
  @author [fengli](li.feng@dfrobot.com)
  @version  V1.0
  @date  2022-6-13
  @url https://github.com/DFRobot/DFRobot_RPi_Display_V3
'''

import sys
sys.path.append("../..") # set system path to top

from devices import DFRobot_Epaper
import time

# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4
RASPBERRY_PIN_RST = 26

epaper = DFRobot_Epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY,RASPBERRY_PIN_RST) # create epaper object

# clear screen and set line width to 3
epaper.begin()
epaper.clearScreen();
#epaper.setLineWidth(3)
time.sleep(1)
epaper.readID()
for i in range(10, 50):
  epaper.pixel(10, i * 2, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.line(20, 20, 20, 100, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.line(40, 20, 60, 100, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.line(60, 20, 40, 100, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.rect(80, 20, 40, 80, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.fillRect(90, 30, 20, 60, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.circle(150, 30, 20, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.fillCircle(150, 30, 15, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.roundRect(130, 60, 40, 40, 10, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.fillRoundRect(140, 70, 20, 20, 5, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.triangle(210, 20, 190, 100, 230, 100, epaper.BLACK)
epaper.flush(epaper.PART)
epaper.fillTriangle(210, 40, 200, 90, 220, 90, epaper.BLACK)

epaper.flush(epaper.PART)