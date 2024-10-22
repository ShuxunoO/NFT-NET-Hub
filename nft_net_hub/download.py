
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nft_net_hub.utils.downloader import NFT1000

if __name__ == "__main__":  
    downloader = NFT1000("NFT1000", r"C:\Users\Lenovo\Desktop\Web3_Projects\NFT-NET-Hub\dataset")
    # downloader.download(["BoredApeYachtClub"])
    downloader.unzip_("CRYPTOPUNKS")



