from dotenv import load_dotenv
import os
import argparse


class Vars:
    DB_TYPE = ""
    USER = ""
    PASS = ""
    HOST = ""
    PORT = ""
    DB_NAME = ""

    @classmethod
    def initialize(cls):
        load_dotenv()
        cls.DB_TYPE = os.getenv("DB_TYPE")
        cls.USER = os.getenv("USER")
        cls.PASS = os.getenv("PASS")
        cls.HOST = os.getenv("HOST")
        cls.PORT = os.getenv("PORT")
        cls.DB_NAME = os.getenv("DB_NAME")

        if not cls.DB_TYPE or not cls.USER or not cls.PASS or not cls.HOST\
                or not cls.PORT or not cls.DB_NAME:
            cls.DB_TYPE = "postgresql"
            cls.USER = "postgres"
            cls.PASS = "123gh45"
            cls.HOST = "localhost"
            cls.PORT = "5432"
            cls.DB_NAME = "some_db"
