import os
import getpass
import dotenv


def get_driver_path():

    uid = os.environ.get('USER') or getpass.getuser()
    dotenv.load_dotenv(dotenv_path=f'../settings/{uid}.env', override=True)
