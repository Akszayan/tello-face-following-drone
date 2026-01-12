from djitellopy import Tello
import time


# Connect to Tello
tello = Tello()
tello.connect()

# Start video stream
tello.streamon()

# Take off
tello.takeoff()
time.sleep(1)  # Allow some time for the drone to stabilize

# Land
tello.land()
time.sleep(1)

# Stop video stream
tello.streamoff()

# Disconnect from Tello 
tello.end()                                                                    
