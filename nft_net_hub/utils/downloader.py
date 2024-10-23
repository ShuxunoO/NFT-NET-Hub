from utils.io_tool_box import IOBox
from utils.u2c_tool_box import Up2Cloud as U2C
import os
from thefuzz import fuzz, process
import pandas as pd
import hashlib
import zipfile

class Downloader:
    def __init__(self, cloud_dataset_name: str, local_dataset_path: str):
        """
        Args:
            name (str): the name of target NFT dataset
            repo_path (str): local path to store the data
        """
        self.cloud_dataset_name = cloud_dataset_name
        self.local_dataset_path = local_dataset_path
        self.password = IOBox.load_json(os.path.join(os.path.dirname(__file__), "..", "info", "password.json"))[self.cloud_dataset_name]
        self.u2c = U2C(self.password["user_access_key"], self.password["repo_id"], self.password["repo_type"])

    def calculate_checksum(self, NFT_name):
        """
        Calculates the SHA256 hash of a file.

        @param NFT_name: NFT name of the file to calculate the SHA256.
        @return: SHA256 hash as a hexadecimal string.
        """
        file_path = os.path.join(self.local_dataset_path, self.cloud_dataset_name, f"{NFT_name}.zip")
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    
    def checksum(self, NFT_name: str):
        """ 

        Args:
            NFT_name (str): _description_

        Returns:
            _type_: _description_
        """

        file_path = os.path.join(self.local_dataset_path, self.cloud_dataset_name, f"{NFT_name}.zip")
        if os.path.exists(file_path):
            local_checksum = self.calculate_checksum(NFT_name)
            oral_checksum = self.dataset_info["collections"][NFT_name]["checksum_sha256"]
            if local_checksum == oral_checksum:
                print(f"{NFT_name}.zip checksum pass!")
                return True
            else:
                print(f"{NFT_name}.zip checksum failed!")
                return False

        else:
            return False

    def unzip_(self, NFT_name: str):
        zip_file_path = os.path.join(self.local_dataset_path, self.cloud_dataset_name, f"{NFT_name}.zip")
        if not os.path.exists(zip_file_path):
            print(f"Error: {NFT_name}.zip not found at {zip_file_path}. Skipping...")
            return False
        file_path = os.path.join(self.local_dataset_path, self.cloud_dataset_name, NFT_name)
        os.makedirs(file_path, exist_ok=True)
        print(f"Unzipping {NFT_name}.zip ……")
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(file_path)
        print(f"Unzipping {NFT_name}.zip successfully!")
        # 删除zip文件
        os.remove(zip_file_path)
        return True

class NFT1000(Downloader):
    def __init__(self, cloud_dataset_name: str, local_dataset_path: str):
        """
        Args:
            cloud_dataset_name (str): the name of target NFT dataset
            local_dataset_path (str): local path to store the data
        
        """
        super().__init__(cloud_dataset_name, local_dataset_path)
        self.dataset_info = IOBox.load_json(os.path.join(os.path.dirname(__file__), "..", "info", "NFT1000.json"))
        self.download_info = pd.read_excel(os.path.join(os.path.dirname(__file__), "..", "info", "NFT1000_download_info.xlsx"))
        # Convert columns to target types
        self.download_info = self.download_info.astype({
            "project_name": "str",
            "contract_address": "str",
            "total_supply": "int64",  # Convert to integer after handling NaN
            "actual_collected_quantity": "int64",  # Convert to integer after handling NaN
            "description": "str",
            "official_url": "str",
            "opensea_url": "str",
            "checksum_sha256": "str",
            "successfully_downloaded": "bool"
        })
        self.training_project_list = self.dataset_info["data_partitioning"].get("training_list")
        self.validation_project_list = self.dataset_info["data_partitioning"].get("validation_list")
        self.testing_project_list = self.dataset_info["data_partitioning"].get("test_list")


    def download_(self, NFT_name : str):
        """
        Downloads a file from the cloud to the local directory.

        @param NFT_name: NFT name of the file to download.

        """
        cloud_file_path = self.cloud_dataset_name + f"/{NFT_name}.zip"
        print("########## Start to download {NFT_name} ##########")
        self.u2c.download_from_huggingface(cloud_file_path, self.local_dataset_path)


    def update_download_info(self, NFT_name: str):
        """
        Updates the local download_info.xlsx

        @param NFT_name: NFT name of the file to update.

        """
        # Retrieve the data to be updated
        update_info = self.dataset_info["collections"][NFT_name]
        update_info.update({"successfully_downloaded": True})

        # Find the row with the specified project name
        idx = self.download_info[self.download_info["project_name"] == NFT_name].index

        if not idx.empty:
            # Update the values in the DataFrame for each key-value pair in update_info
            for key, value in update_info.items():
                self.download_info.loc[idx, key] = value
        else:
            # If no corresponding row is found, append a new row
            new_info_df = pd.DataFrame([update_info])
            self.download_info = pd.concat([self.download_info, new_info_df], ignore_index=True)

        # Save the updated information to a local file
        self.download_info.to_excel(os.path.join(os.path.dirname(__file__), "..", "info", "NFT1000_download_info.xlsx"), index=False)


    def download(self, name_list: list):
        """
        Downloads a list of NFT Projects from the cloud to the local directory.

        Args:
            name_list (list): A list of NFT names to download.
        """
        NFT1000_name_list = list(self.dataset_info["collections"].keys())
        for NFT_name in name_list:
            if NFT_name not in NFT1000_name_list:
                match_results = Downloader_Helper.get_similar_names(NFT_name, NFT1000_name_list)
                print(f"Error: {NFT_name} not in repo_info, do you mean {match_results}?")
                exit()
            
            # 检查是否已经下载过判断name所在下载信息那一行的successfully_downloaded 字段是否为true
            elif self.download_info[self.download_info["project_name"] == NFT_name]["successfully_downloaded"].eq(True).any():
                print(f"{NFT_name}.zip had been downloaded successfully")
                continue

            # 如果目标目录中已有该项目文件，则进行校验
            elif self.checksum(NFT_name):
                print(f"{NFT_name}.zip had been downloaded successfully! ")
                self.update_download_info(NFT_name)
                continue
            
            else:
                # 如果目标目录中没有该项目文件，则进行下载
                self.download_(NFT_name)
                if self.checksum(NFT_name):
                    print(f"{NFT_name}.zip had been downloaded successfully! ")
                    self.update_download_info(NFT_name)
                else:
                    print(f"{NFT_name}.zip failed to download")
                    continue

    def download_all(self):
        """
        Downloads all NFT Projects from the cloud to the local directory.
        """
        name_list = list(self.dataset_info["collections"].keys())
        self.download(name_list)

    def unzip(self, NFT_name_list: list):
        """
        Unzips a list of NFT Projects from the local directory.

        Args:
            NFT_name_list (list): A list of NFT names to unzip.
        """
        for NFT_name in NFT_name_list:
            if self.download_info[self.download_info["project_name"] == NFT_name]["unziped"].eq(True).any():
                print(f"{NFT_name}.zip had been unziped successfully")
            else:
                if self.unzip_(NFT_name):
                    self.download_info.loc[self.download_info["project_name"] == NFT_name, "unziped"] = True
                    self.download_info.to_excel(os.path.join(os.path.dirname(__file__), "..", "info", "NFT1000_download_info.xlsx"), index=False)

    def unzip_all(self):
        """
        Unzips all NFT Projects from the local directory.
        """

        NFT_name_list = list(self.dataset_info["collections"].keys())
        self.unzip(NFT_name_list)

    def query(self, query: str):
        """
        Query the NFT dataset by the query string.

        Args:
            query (str): the query string

        Returns:
            list: the list of NFT projects that match the query string
        """
        if fuzz.ratio(query, "training") >= 40:
            return self.training_project_list
        elif fuzz.ratio(query, "validation") >= 40:
            return self.validation_project_list
        elif fuzz.ratio(query, "testing") >= 40:
            return self.testing_project_list
        else:
            if query not in self.dataset_info["collections"].keys():
                match_results = Downloader_Helper.get_similar_names(query, list(self.dataset_info["collections"].keys()))
                print(f"Error: {query} not in repo_info, do you mean {match_results}?")
                return None
            match_results = self.dataset_info["collections"].get(query)
            return match_results

    def get_NFT_name_list(self):
        """
        Get the list of NFT names in the NFT1000 dataset.

        Returns:
            list: the list of NFT names
        """
        return list(self.dataset_info["collections"].keys())


class Downloader_Helper():
    @staticmethod
    def get_similar_names(name: str, NFT_name_list: list):
        """
        Get the similar names in the NFT dataset.

        Args:
            name (str): the name to query
            NFT_name_list (list): the list of NFT names

        Returns:
            list: the list of NFT names that are similar to the query name
        """
        match_results = process.extract(name, NFT_name_list, scorer=fuzz.ratio, limit=3)
        # match_results = process.extract(name, NFT_name_list, scorer=fuzz.partial_ratio, limit=3)
        # 将匹配结果中的概率值整数值变成小数值，小数点后保留两位
        match_results = [(item[0], float(f"{item[1] / 100:.2f}")) for item in match_results]
        return  match_results




