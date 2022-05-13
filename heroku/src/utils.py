import os
from pathlib import Path


def is_local_host() -> bool:
    """Register the current environment"""

    if Path(".\\env.py").is_file():
        import env

        env.reg_environ()
