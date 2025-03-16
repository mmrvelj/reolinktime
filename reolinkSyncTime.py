import configparser
from onvif import ONVIFCamera
import datetime

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Extract values from the config file
CAMERA_IP = config.get("CAMERA", "IP")
CAMERA_PORT = config.getint("CAMERA", "PORT")
USERNAME = config.get("CAMERA", "USERNAME")
PASSWORD = config.get("CAMERA", "PASSWORD")
WSDL_PATH = config.get("CAMERA", "WSDL_PATH")

# Connect to the camera
camera = ONVIFCamera(CAMERA_IP, CAMERA_PORT, USERNAME, PASSWORD, WSDL_PATH)

# Get the device management service
device_service = camera.create_devicemgmt_service()

# Get the current system time in UTC
current_time = datetime.datetime.utcnow()

# Create the request to set the system date and time
dt_request = device_service.create_type('SetSystemDateAndTime')
dt_request.DateTimeType = 'Manual'
dt_request.DaylightSavings = False  # Adjust if daylight savings is observed
dt_request.TimeZone = None  # Set to None or specify the timezone if required

# Set the UTC date and time
dt_request.UTCDateTime = {
    'Time': {'Hour': current_time.hour, 'Minute': current_time.minute, 'Second': current_time.second},
    'Date': {'Year': current_time.year, 'Month': current_time.month, 'Day': current_time.day}
}

# Send the request to update the system date and time
try:
    device_service.SetSystemDateAndTime(dt_request)
    print(f"✅ Time successfully updated to {current_time.isoformat()} (UTC) on {CAMERA_IP}")
except Exception as e:
    print(f"❌ Failed to update time: {e}")

