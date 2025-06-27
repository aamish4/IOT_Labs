import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11  # Ya DHT22 agar wo use ho raha ho
pin = 4  # Apne sensor ka actual GPIO pin yahan likho

# Sirf 5 dafa try karega
for i in range(5):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature}°C  Humidity: {humidity}%")
        break
    else:
        print("Failed to read from DHT sensor!")
    time.sleep(2)
