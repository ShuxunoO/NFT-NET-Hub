
from utils.downloader import NFT1000

if __name__ == "__main__":

    # download the NFTs
    local_repo_path = r"C:\Users\Lenovo\Desktop\Web3_Projects\NFT-NET-Hub\dataset\NFT1000"
    # modfiy the NFT_name_list to the NFT projects you want to download
    # NFT_name_list = ["BoredApeYachtClub", "CRYPTOPUNKS"]
    NFT_name_list = ["mfers"]
    NFT1000 = NFT1000("NFT1000", local_repo_path)
    NFT1000.download(NFT_name_list)

    # # download all the NFTs
    # NFT1000.download_all()

    # # unzip the NFTs
    # NFT1000.unzip(NFT_name_list)

    # # unzip all the NFTs
    # NFT1000.unzip_all()

    # # query the NFTs
    # print(NFT1000.query("BoredApeYachtClub"))




