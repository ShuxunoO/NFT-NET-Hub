from huggingface_hub import login, HfApi
from huggingface_hub import hf_hub_download
import os

class Up2Cloud:
    def __init__(self, user_access_key, repo_id, repo_type):
        self.user_access_key = user_access_key
        self.repo_id = repo_id
        self.repo_type = repo_type
        # 登录 Hugging Face
        login(self.user_access_key, add_to_git_credential=True)

    # 上传文件到huggingface
    def up2Huggingface_file(self,local_file_path, cloud_file_path):
        api = HfApi()
        # 上传 zip 文件到 Huggingface 数据集
        api.upload_file(
            path_or_fileobj=local_file_path,  # zip 文件的路径
            path_in_repo=cloud_file_path,  # 在数据集中的路径
            repo_id=self.repo_id,  # 数据集的名称
            repo_type=self.repo_type  # 确认上传的是数据集
        )
    # 上传文件夹到huggingface
    def up2Huggingface_folder(self,local_folder_path, cloud_folder_path):
        api = HfApi()
        # 上传 zip 文件到 Huggingface 数据集
        api.upload_folder(
            folder_path=local_folder_path,  # 文件夹的路径
            path_in_repo=cloud_folder_path,
            repo_id=self.repo_id,  # 数据集的名称
            repo_type=self.repo_type  # 确认上传的是数据集
        )

    # 从huggingface下载指定文件
    def download_from_huggingface(self, cloud_file_path, local_file_path):
        # 使用 hf_hub_download 来下载文件
        file_path = hf_hub_download(
            repo_id=self.repo_id,
            filename=cloud_file_path,
            local_dir=local_file_path,
            repo_type=self.repo_type
        )
        print(f"File downloaded to {file_path}")