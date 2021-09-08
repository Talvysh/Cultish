class Event:
    queue = []

    def __init__(self, message, function):
        self.function = function  # Function to call when message is found
        self.message = message  # Message to track in queue

    @staticmethod
    def add():
        pass

    @staticmethod
    def pull():
        pass
