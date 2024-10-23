import json
from pathlib import Path

class IOBox:
    def __init__(self):
        pass

    @staticmethod
    def check_dir(dir_path):
        """
        check if the directory exists, if not, create it

        Args:
            dir_path (str): The path to the directory
        """
        dir_path = Path(dir_path)

        if not dir_path.exists():
            try:
                dir_path.mkdir(parents=True)
            except Exception as e:
                raise e

    @staticmethod
    def load_json(json_path):
        """
        Loads a json file from the given path

        Args:
            config_path: The path to the json file

        Returns:
            A dictionary

        """
        with open(json_path, 'r', encoding='UTF-8') as f:
            return json.load(f)
        
    @staticmethod
    def save_json(save_path, data):
        """
        Saves the data to a file with the given filename in the given path

        Args:
            :param save_path: The path to the folder where you want to save the file
            :param filename: The name of the file to save
            :param data: The data to be saved

        """
        with open(save_path, 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
