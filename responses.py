from abc import *


class Response(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def audienceResponse(self):
        pass


class Happy(Response):
    def audienceResponse(self):
        print("Cheer")


class unHappy(Response):
    def audienceResponse(self):
        print("Boo")


class Normal(Response):
    def audienceResponse(self):
        print("No Reaction")