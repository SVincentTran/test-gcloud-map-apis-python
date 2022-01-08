# Google cloud functions imports
from flask import escape
import functions_framework

@functions_framework.http
def test_hello_world(request):
    """ Hello World function to test HTTP GCloud Function
    """
    return "Hello World"