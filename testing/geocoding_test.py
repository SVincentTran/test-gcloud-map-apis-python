from unittest.mock import Mock
import logging

import main

# Logging to terminal
logging.basicConfig(level=logging.DEBUG)
myLogger = logging.getLogger()

def test_geocoding():
    name = "Big C Thang Long"

    data = {"name": name}
    
    req = Mock(get_json = Mock(return_value=data), args=data)

    geocoding = main.geocoding(req)

    myLogger.info(geocoding)