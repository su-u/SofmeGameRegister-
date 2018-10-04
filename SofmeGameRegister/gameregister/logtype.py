from enum import Enum

class LogType(Enum):
    NEW = 1
    UPDATE = 2

    def string(type):
        if type == LogType.NEW:
            return "NEW"
        elif type == LogType.UPDATE:
            return "UPDATE"
