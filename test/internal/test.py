import os

from dotenv import load_dotenv
from injector import Injector, inject

class A:
    name: str = "llmops"

@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print_name(self):
        print(f"class A.name = {self.a.name}")

injector = Injector()
b = injector.get(B)
b.print_name()

loaded = load_dotenv()
print(f"Dotenv loaded: {loaded}")
print(os.getenv("SQLALCHEMY_DATABASE_URI"))
print(os.getenv("DASHSCOPE_BASE_URL"))