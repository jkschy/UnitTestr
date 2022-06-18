from .JsonHelp import getSetting

def log(msg):
    """
    Logs the message with the prefix Log

    Only prnts on Verbose Logging
    :param msg: The Message to print
\    """
    if getSetting('logging_level') == "verbose":
        print(f"Log: {msg}")


def debug(msg):
    """
    Logs the message with the prefix Debug

    Only prnts on Debug Logging
    :param msg: The Message to print
\    """
    if getSetting('logging_level') == "verbose" or getSetting('logging_level') == "debug":
        print(f"Debug: {msg}")


def Error(msg, location=None):
    """
    Logs the message with the prefix Error

    Always prints, also on minimal logging
    :param location: Optional, where the error occurred, example, Error in After hook
    :param msg: The Message to print
\    """
    error_loc = "Error"
    if location is not None:
        error_loc += f" in {location}"

    print(f"{error_loc}: {msg}")
