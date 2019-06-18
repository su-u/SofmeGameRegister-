from enum import Enum

class LogType(Enum):
    NEW = 1
    UPDATE = 2
    ACCESS_EDIT = 3
    ACCESS_REGISTER= 4
    ACCESS_INDEX = 5
    ACCESS_ADMIN_INDEX = 6
    ACCESS_CONFIRMATION = 7
    ACCESS_LP = 8
    FAILED_UUID = 9
    ACCESS_MANUAL_PAGE = 10
    ACCESS_SIGH_BORD_PAGE = 11
    ACCESS_MOVIE_PAGE = 12

    def string(type):
        if type == LogType.NEW:
            return "CREATED_POST"
        elif type == LogType.UPDATE:
            return "UPDATE_POST"
        elif type == LogType.ACCESS_EDIT:
            return "ACCESS_EDIT"
        elif type == LogType.ACCESS_REGISTER:
            return "ACCESS_REGISTER"
        elif type == LogType.ACCESS_INDEX:
            return "ACCESS_INDEX"
        elif type == LogType.ACCESS_ADMIN_INDEX:
            return "ACCESS_ADMIN_INDEX"
        elif type == LogType.ACCESS_CONFIRMATION:
            return "ACCESS_CONFIRMATION"
        elif type == LogType.ACCESS_LP:
            return "ACCESS_LP"
        elif type == LogType.FAILED_UUID:
            return "FAILED_UUID"
        elif type == LogType.ACCESS_MANUAL_PAGE:
            return "ACCESS_MANUAL_PAGE"
        elif type == LogType.ACCESS_SIGH_BORD_PAGE:
            return "ACCESS_SIGH_BORD_PAGE"
        elif type == LogType.ACCESS_MOVIE_PAGE:
            return "ACCESS_MOVIE_PAGE"