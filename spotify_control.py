import serial
import time
import pyautogui
# Hardware Serial Parameters
COM_PORT = "COM3" 
BAUD_RATE = 115200
print(f"Connecting to Pico on {COM_PORT}...")
try:
 # Initialize connection to the microcontroller
 ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
 time.sleep(2) # Allow port connection to stabilize
 print("Connected! Listening for 3-Zone gestures... Open Spotify and try it!")
 
 while True:
 # Check if incoming serial data is waiting in the buffer
 if ser.in_waiting > 0:
 # Read line, decode raw bytes to text string, and strip whitespace
 line = ser.readline().decode('utf-8').strip()
 
 # Map string identifiers to system-level keyboard macros
 if "GESTURE_PAUSE" in line:
 print("Gesture detected: PLAY / PAUSE")
 pyautogui.press('space') # Universal media spacebar toggle
 
 elif "SWIPE_RIGHT" in line:
 print("Gesture detected: Moving to NEXT song")
 pyautogui.hotkey('ctrl', 'right') # Spotify shortcut for next
 
 elif "SWIPE_LEFT" in line:
 print("Gesture detected: Moving to PREVIOUS song")
 pyautogui.hotkey('ctrl', 'left') # Spotify shortcut for back
 
 time.sleep(0.01) # Minimal sleep to prevent high CPU utilization
except serial.SerialException:
 print(f"Error: Could not open {COM_PORT}. Ensure Thonny is closed!")
except KeyboardInterrupt:
 print("\nStopping PC receiver script.")
