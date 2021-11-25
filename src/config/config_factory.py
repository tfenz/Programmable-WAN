import glob
import importlib
import inspect
import logging
import os

from config.generic_config import GenericTestSetup

__CONFIG_MODULE_PATH = "config"


def __load_all_modules_from_dir(config_file_name):
    config_file_name = config_file_name.replace(".py", "")
    path = glob.glob(os.path.join(os.path.dirname(__file__), f"{config_file_name}.py"))[0]
    name, ext = os.path.splitext(os.path.basename(path))
    return importlib.import_module("config." + name)


def get_test_setup(config_file_name: str, setup_class: str) -> GenericTestSetup:
    """ return the requested setup-object: setup_class defined in file: config_file_name (config/*.py)"""
    try:
        config_module = __load_all_modules_from_dir(config_file_name)
    except Exception as ex:
        msg = f"config file could not be loaded from: {__CONFIG_MODULE_PATH}/{config_file_name}.py: {str(ex)}"
        logging.error(msg)
        print(msg)
        raise ex

    # 2. instantiate class with the requested class name
    config_object = None
    for name, setup_cls in inspect.getmembers(config_module, inspect.isclass):
        if setup_class.lower() == name.lower():
            return setup_cls()

    if config_object is None:
        msg="setup class not found in config"
        logging.error(msg)
        raise Exception(msg)


def get_setup_list(config_file_name: str):
    """ returns all available setups in the given config_file"""
    try:
        config_module = __load_all_modules_from_dir(config_file_name)
    except Exception as ex:
        msg = f"config file could not be loaded from: {__CONFIG_MODULE_PATH}/{config_file_name}.py: {str(ex)}"
        print(msg)
        logging.error(msg)
        raise ex

    setup_list = [
        name for name, setup_cls in inspect.getmembers(config_module, inspect.isclass) if not name.startswith("Generic")
    ]
    return setup_list
