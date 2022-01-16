from unittest.mock import Mock
import logging

import main

# Logging to terminal
logging.basicConfig(level=logging.DEBUG)
myLogger = logging.getLogger()

def test_search_directions():
    origin = "Big C Thang Long"
    destination = "Vincom Nguyen Chi Thanh"

    data = {"origin": origin, "destination": destination}
    
    req = Mock(get_json = Mock(return_value=data), args=data)

    direction = main.search_directions(req)

    myLogger.info(direction)