import os
from os.path import normpath

import requests
from pathlib import Path
from InitialiseDB import _Main


class ChromeAccessURL:
    def __init__(self, second_parameters, WebsiteName):
        print("ChromeAccessURL")
        location = str(os.getcwd()) + "\ACME_Storage.db"
        self.path = normpath(location)
        self.WebsiteName = WebsiteName
        self.secondParameters = second_parameters
        self.URL = ""
        self.url()
        self.data = {}
        self.extract_all_page()

    def extract_all_page(self):
        print("Extracting from Web page")
        response = requests.get(self.URL)
        CheckURL = response.json()
        CheckURL = list(CheckURL.values())
        if str(CheckURL[0]) != "False":
            self.data = response.json()

            keys = list(self.data.keys())
            if keys[4] == "Season":
                self.data.pop('Season')
                self.data.pop('Episode')
                self.data.pop('seriesID')
                keys1 = ["DVD", "BoxOffice", "Production", "Website"]
                items = ["N/A","N/A","N/A","N/A"]
                self.data = _Main.AddToDictionary(self.data,20,keys1,items)
            _Main.InsertIntoTable(self.path, self.WebsiteName, self.data)
            print("Finished Extracting WITH DATA")
        else:
            self.data = {"N/A": "N/A"}
            print("Finished Extracting NO DATA")

    def url(self):
        print("Creating URL")
        parameters = [["i", "t", "type", "y", "plot", "r", "apikey"], self.secondParameters]
        self.URL = "http://www.omdbapi.com/?"
        for i in range(7):
            for y in range(2):
                self.URL = self.URL + parameters[y][i] + "="
            self.URL = self.URL[:-1]
            self.URL = self.URL + "&"
        self.URL = self.URL[:-1]
        print("Finished Creating URL")

    def get_dict(self):
        print("Getting Dictionary from class")
        return self.data



