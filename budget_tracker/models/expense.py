#models/ -- contain data structures, classes etc

class Expense:
    def __init__(self, config: dict):
        self.__value = config.get("value", None)
        self.__category = config.get("category", None)
        self.__date = config.get("date", None)
        self.__note = config.get("note", None)
        self.__config = config

    #later: __init__() overload w/ explicit parameters instead of config dictionary? or replace dict config entirely

    def get_config(self):
        return self.__config
    