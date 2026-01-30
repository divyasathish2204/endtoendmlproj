import logging
import os
from datetime import datetime
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)
logfilename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logfilepath = os.path.join("logs", logfilename)
logging.basicConfig(
    filename=logfilepath,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)

