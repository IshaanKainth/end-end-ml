import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Generate a unique log file name with a timestamp
log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log")

# Configure logging
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,  # Use DEBUG for detailed logs
    format="[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S"
)
    
    