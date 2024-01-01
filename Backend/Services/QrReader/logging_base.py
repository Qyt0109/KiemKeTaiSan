import datetime
import json
import logging
import os


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
    )
    fileHandler = logging.FileHandler(log_file, mode="a+", encoding="utf-8")
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


class LoggerBase:
    def __init__(self, name, root="./logs/"):
        self.name = name
        self.root = root
        datetime.datetime.now()
        name_log = name
        if not os.path.isdir(root):
            os.mkdir(root)
        path_file = os.path.join(root, name_log + ".log")
        if not logging.getLogger(name_log).hasHandlers():
            setup_logger(name_log, path_file)
        self.logger = logging.getLogger(name_log)

    def dump_json_file(self, path_file, data):
        with open(path_file, "w") as outfile:
            json.dump(data, outfile)
