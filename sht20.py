from sensor.SHT20 import SHT20

# I2C bus=1, Address=0x40
sht = SHT20(1, 0x40)

h = sht.humidity()  # read humidity
print(h)            # namedtuple
print(h.RH)         # relative humidity

t = sht.temperature()  # read temperature
print(t)               # namedtuple
print(t.C)             # Celsius

h, t = sht.all()  # read both at once
