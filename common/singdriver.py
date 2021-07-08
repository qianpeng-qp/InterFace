from selenium import webdriver


class Singdriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = webdriver.Chrome()
        return cls.__instance

