#!/usr/bin/env python
# -*- coding: utf-8 -*-
from httplib2 import Http
from oauth2client import file, tools, client
from pathlib import Path
import os
from googleapiclient.discovery import build


class AuthenticationSheets:
    def __init__(self):
        self.ROOT_PATH = Path(Path(os.path.abspath(__file__)).parent)
        self.PATH_TO_SECRET = Path(self.ROOT_PATH / "secret/client_secret.json")
        self.SCOPE = "https://www.googleapis.com/auth/spreadsheets"
        
    def __return_credentials(self):
        storage = file.Storage(self.ROOT_PATH / "secret/token.json")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.PATH_TO_SECRET, scope=self.SCOPE)
            args = tools.argparser.parse_args([])
            credentials = tools.run_flow(flow, storage, args)
        return credentials

    def build_service(self):
        credentials = self.__return_credentials()
        http = credentials.authorize(Http())
        service = build("sheets", "v4", http=http)
        return service
    @property
    def get_service(self):
        service = self.build_service()
        spreadsheets = service.spreadsheets()
        return spreadsheets
