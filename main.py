from machine import Pin, I2C, ADC
from time import sleep, sleep_ms


# ---------- LCD 驱动 ----------
class LCD:
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address
        self.backlight = 0x08

        sleep_ms(50)
        self.command(0x33)
        self.command(0x32)
        self.command(0x28)
        self.command(0x0C)
        self.command(0x06)
        self.clear()

    def _write(self, data):
        self.i2c.writeto(self.address, bytes([data | self.backlight]))

    def _pulse(self, data):
        self._write(data | 0x04)
        sleep_ms(1)
        self._write(data & ~0x04)
        sleep_ms(1)

    def _send(self, value, mode=0):
        self._pulse((value & 0xF0) | mode)
        self._pulse(((value << 4) & 0xF0) | mode)

    def command(self, value):
        self._send(value, 0)

    def text(self, message):
        for char in message:
            self._send(ord(char), 1)

    def cursor(self, row, column):
        self.command([0x80, 0xC0][row] + column)

    def clear(self):
        self.command(0x01)
        sleep_ms(2)


# ---------- 接线设置 ----------
# LCD：SDA=21，SCL=22，地址=0x27
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = LCD(i2c, 0x27)

# 土壤传感器：AO 接 GPIO33
soil_sensor = ADC(Pin(33))
soil_sensor.atten(ADC.ATTN_11DB)

# 水泵驱动：IN_A=18，IN_B=19
pump_a = Pin(18, Pin.OUT)
pump_b = Pin(19, Pin.OUT)

# LED：GPIO12
led = Pin(12, Pin.OUT)

# 土壤值达到此数值，开始浇水
SOIL_DRY = 2200


def pump_off():
    pump_a.off()
    pump_b.off()


def pump_on():
    pump_a.on()
    pump_b.off()


def read_soil():
    # 连续读取 5 次取平均，数字会更稳定
    total = 0
    for _ in range(5):
        total += soil_sensor.read()
        sleep_ms(20)
    return total // 5


def show(soil, message):
    lcd.clear()
    lcd.cursor(0, 0)
    lcd.text("Soil: " + str(soil))
    lcd.cursor(1, 0)
    lcd.text(message)


# 开机先确保水泵关闭
pump_off()
led.off()

while True:
    soil = read_soil()
    print("Soil:", soil)

    # 读数异常：不浇水
    if soil < 100:
        pump_off()
        led.off()
        show(soil, "SENSOR CHECK")
        sleep(2)

    # 土太干：浇水 3 秒
    elif soil >= SOIL_DRY:
        led.on()
        show(soil, "WATERING 3 SEC")
        print("Pump ON")

        pump_on()
        sleep(3)

        pump_off()
        led.off()
        print("Pump OFF")

        show(soil, "WAIT 60 SEC")
        sleep(60)

    # 土壤湿度正常：不浇水
    else:
        pump_off()
        led.off()
        show(soil, "MOIST OK")
        sleep(2)
