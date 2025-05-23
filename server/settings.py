import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

load_dotenv()
# load_dotenv(os.path.join(BASE_DIR, '.env'))


def str2bool(s):
    """
    如果 s 为 '0', 'n', 'no', 'false' ，返回 False
    其他情况返回 True
    """
    if isinstance(s, bool):
        return s
    return s.lower() not in ('0', 'n', 'no', 'false')


DEBUG = True
ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL", '')
DATABASE_URL = os.getenv("DATABASE_URL", '')
