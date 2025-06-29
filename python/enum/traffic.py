# from enum library import Enum class

from enum import Enum
import time

class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

def show_signal(signal):
    if signal == TrafficLight.RED:
        print("🔴 STOP!")
    elif signal == TrafficLight.YELLOW:
        print("🟡 GET READY!")
    elif signal == TrafficLight.GREEN:
        print("🟢 GO!")
    else:
        print("Invalid signal")

# Simulate a traffic signal cycle
for signal in TrafficLight:
    show_signal(signal)
    time.sleep(1)  # wait for 1 second