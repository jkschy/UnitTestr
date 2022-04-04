import json


def getSetting(name):
    """
    Gets the setting from Config.jsob
    :param name: the name of the Config setting
    :return: The value of the setting
    """
    f = open("./helpers/Config.json")
    config = json.load(f)
    return config[name] if config[name] is not None else "Oh no!"


def verifySettings():
    logging_level = getSetting("logging_level")

    if logging_level != "minimal" and logging_level != "debug" and logging_level != "verbose":
        raise Exception(f"logging_level inside Config was not properly set, must be 'minimal', 'debug' or 'verbose' "
                        f"found ['{logging_level}']")


