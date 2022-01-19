import os
from tkinter.messagebox import NO
import uuid

import requests

def test_no_args():
    BASE_URL = os.getenv("HTTP_CLOUD_FUNC_BASE_URL")
    assert BASE_URL is not None

    res = requests.post("{}/search_directions".format(BASE_URL))
    print(res)

def test_args():
    BASE_URL = os.getenv("HTTP_CLOUD_FUNC_BASE_URL")
    assert BASE_URL is not None

    origin = "Big C Thang Long"
    destination = "Vincom Nguyen Chi Thanh"

    res = requests.post(
        "{}/search_directions".format(BASE_URL),
        json={"origin": origin, "destination": destination}
    )

    print(res)