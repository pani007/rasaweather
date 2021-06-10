# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


import numpy as np 
import pandas as pd 

import requests
import json
response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/texas/2021-6-10/2021-6-10?unitGroup=us&key=PEX3YKS4TK2SNLWP9QZB84NK2").json()
#res_dict = json.dumps(response)
print(res_dict)
class GetResults(Action):
    def name(self):
        return 'show_weather'
    def show_results(tracker,dispatcher):
        pass
