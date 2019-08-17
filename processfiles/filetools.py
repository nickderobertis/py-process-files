from typing import Any
import time


def write_to_file_with_retries(filepath: str, content: Any, retries_remaining: int = 10):
    try:
        with open(filepath, 'w') as f:
            f.write(str(content))
    except (OSError, PermissionError) as e:
        if retries_remaining < 1:
            raise e
        time.sleep(.1)
        write_to_file_with_retries(filepath, content, retries_remaining=retries_remaining - 1)


def open_file_with_retries(filepath: str, retries_remaining: int = 10) -> str:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            return content
    except (OSError, PermissionError) as e:
        if retries_remaining < 1:
            raise e
        time.sleep(.1)
        return open_file_with_retries(filepath, retries_remaining=retries_remaining - 1)