from typing import Optional
from logging import FileHandler

CHROME_DRIVER_PATH = "/usr/bin/chromedriver"
FIREFOX_DRIVER_PATH = "/usr/bin/geckodriver"
LOGS_PATH = './Logs'
datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ"

def timestamp_now() -> (str, str):
    from datetime import datetime
    now = datetime.now()
    return now.strftime(datetime_format), str(int(datetime.timestamp(now) * 1000))


def create_log_file_handler(
        file_name: str
):
    from logging import FileHandler, Formatter

    # root_dir = str(Path(os.getcwd()))
    file_handler = FileHandler(f'{LOGS_PATH}/{file_name}.log', 'a')
    formatter = Formatter('%(levelname)s - %(asctime)s: %(message)s')
    file_handler.setFormatter(formatter)

    return file_handler


def override_log_handler(
        log,
        file_handler: FileHandler
):
    """
        Overrides the file handler for the given logger
    """
    if len(log.handlers) > 0:
        if isinstance(log.handlers[-1], FileHandler):
            log.handlers[-1] = file_handler
        else:
            log.addHandler(file_handler)
    else:
        log.addHandler(file_handler)


def replace_log_file(
        log,
        file_name_or_handler: Optional[FileHandler or str]
):
    """
        Switches the logging to another file IF the file_name is not None.
    """
    if file_name_or_handler is not None:
        if isinstance(file_name_or_handler, str):
            file_handler = create_log_file_handler(file_name=file_name_or_handler)
        elif isinstance(file_name_or_handler, FileHandler):
            file_handler = file_name_or_handler
            file_name_or_handler = file_handler.name
        else:
            log.error("Not implemented")
            raise NotImplementedError

        log.debug(f"switching log output to {file_name_or_handler}")
        override_log_handler(
            log=log,
            file_handler=file_handler
        )
        return file_handler.name
    else:
        return None
