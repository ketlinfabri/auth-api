import os
import ast
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):
    @staticmethod
    def get(name: str) -> str:
        return os.getenv(name)

    @staticmethod
    def get_list(name: str) -> list:
        value = os.getenv(name)
        if value:
            return ast.literal_eval(value)
        return []


      # AWS_ACCESS_KEY_ID: "AKIA3566Y2WN7IFYKNER"
      # AWS_SECRET_ACCESS_KEY: "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"