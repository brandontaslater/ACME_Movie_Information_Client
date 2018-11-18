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
        data = response.json()
        CheckURL = list(data.values())
        if str(CheckURL[1]) != "0":
            data = data.get("results")
            data = data[0]
            self.data = dict(data)

            _Main.InsertIntoTable(self.path, self.WebsiteName, self.data)
        else:
            self.data = {"N/A": "N/A"}
        print("Finished Extracting")

    def url(self):
        print("Creating URL")
        parameters = [["query", "api_key"], self.secondParameters]
        self.URL = "https://api.themoviedb.org/3/search/movie?"
        for i in range(2):
            for y in range(2):
                self.URL = self.URL + parameters[y][i] + "="
            self.URL = self.URL[:-1]
            self.URL = self.URL + "&"
        self.URL = self.URL[:-1]
        print("Finished Creating URL")

    def get_dict(self):
        print("Getting Dictionary from class")
        return self.data



