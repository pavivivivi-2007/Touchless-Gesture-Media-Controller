import machine
import time
# Pin Configurations (Using the working Left Sensor)
trig_left = machine.Pin(2, machine.Pin.OUT)
echo_left = machine.Pin(3, machine.Pin.IN)
def get_distance(trig, echo):
 """
 Triggers the ultrasonic sensor and calculates the distance in centimeters
 based on the time of flight of the acoustic pulse.
 """
 # Ensure trigger is low
 trig.value(0)
 time.sleep_us(2)
 
 # Send a 10 microsecond pulse to trigger the sensor
 trig.value(1)
 time.sleep_us(10)
 trig.value(0)
 
 # Measure the duration of the incoming echo pulse (30ms timeout)
 duration = machine.time_pulse_us(echo, 1, 30000)
 if duration < 0:
 return 999.0 # Return out-of-range value if pulse fails
 
 # Calculate distance: (Speed of sound * time) / 2 for one-way travel
 return (duration * 0.0343) / 2
# Main Infinite Execution Loop
while True:
 try:
 dist = get_distance(trig_left, echo_left)
 
 # Zone 1: Very Close (Under 10 cm) -> Play/Pause Action
 if dist < 10:
 print("GESTURE_PAUSE")
 time.sleep(0.8) # Debounce delay to prevent rapid double-triggering
# Zone 2: Medium Distance (10 cm to 20 cm) -> Next Track Action
elif 10 <= dist < 20:
print("SWIPE_RIGHT")
time.sleep(0.6)
# Zone 3: Far Distance (20 cm to 35 cm) -> Previous Track Action
elif 20 <= dist < 35:
print("SWIPE_LEFT")
time.sleep(0.6)
except Exception as e:
# Prevent runtime hardware glitches from crashing the entire system
pass
time.sleep(0.05) # 50ms sampling rate interval
