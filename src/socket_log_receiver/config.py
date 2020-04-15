import logging

from resconfig import ResConfig

default = {
    "log": {
        "filename": None,
        "filemode": "a+",
        "format": logging.BASIC_FORMAT,
        "datefmt": None,
    }
}

config = ResConfig(default, skip_load_on_init=True)


def configure_logging():
    handlers = []

    filename = config["log.filename"]
    if filename:
        mode = config["log.filemode"]
        handlers = [logging.handlers.WatchedFileHandler(filename, mode=mode)]

    if not any(type(h) == logging.StreamHandler for h in logging.root.handlers):
        handlers.append(logging.StreamHandler())

    format = config["log.format"]
    datefmt = config["log.datefmt"]
    formatter = logging.Formatter(format, datefmt)

    for handler in handlers:
        handler.setFormatter(formatter)
        logging.root.addHandler(handler)

    logging.root.setLevel("INFO")
