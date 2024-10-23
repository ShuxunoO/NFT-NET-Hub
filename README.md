![NFT1000](assets/NFT_NET_HUB.png)

## <div align="center">NFT-NET-HUB: Comprehensive Management Tool for NFT-NET Dataset</div>


[![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20Huggingface-NFT%20NET-orange?style=flat&logoColor=%23FFD21E)](https://huggingface.co/datasets/shuxunoo/NFT-Net)[![Static Badge](https://img.shields.io/badge/arXiv-2402.16872%20-B31B1B?style=flat&logo=arxiv&link=https%3A%2F%2Farxiv.org%2Fabs%2F2402.16872)](https://arxiv.org/abs/2402.16872)[![Open issue](https://img.shields.io/github/issues/ShuxunoO/NFT-NET-Hub)](https://github.com/ShuxunoO/NFT-NET-Hub/issues)[![Closed issue](https://img.shields.io/github/issues-closed/ShuxunoO/NFT-NET-Hub)](https://github.com/ShuxunoO/NFT-NET-Hub/issues)

[中文版](README_ZH.md) | [English Version](README.md)

<br>

## 🚀- NEWS

- [2024-10-15] ⛵ Project Creation；

- [2023-10-25] 🥳 NFT-NET-Hub for [NFT1000](https://huggingface.co/datasets/shuxunoo/NFT-Net/tree/main/NFT1000) released! 🎉；

- ……

<br>

## 📋︎- Introduction of NFT-NET-HUB

**NFT-NET-HUB** is a versatile and user-friendly package management tool specifically designed to accompany the NFT-NET dataset. It provides a highly flexible and efficient way to query, download, and manage data within NFT-NET, ensuring seamless integration and usability for developers and researchers working with NFT datasets.

Key features of **NFT-NET-HUB** include:

- **Data Querying**: Effortlessly search through the NFT-NET dataset to find the data you need;
- **Data Download**: Conveniently download NFT data in a structured format from the cloud;
- **Data Management**: Organize, maintain, and keep track of your NFT data collections with ease;

Whether you're exploring NFT datasets for research or development, **NFT-NET-HUB** streamlines the entire process, making it an essential tool for handling NFT data.

<br>

## ⚙- Usage



### 1. Download and install

Clone the Github repository.

   ```git
   git clone https://github.com/ShuxunoO/NFT-NET-Hub.git
   ```

Install the requirements.
       
 ```bash
 cd NFT-NET-Hub
 pip install -r requirements.txt
 ```



### 2. Downlaod Target NFT Projects

Supports resuming from breakpoints, **please make sure you can visit Huggingface**🪜

```
cd NFT-NET-Hub/nft_net_hub
```

modify the download.py file to download the NFT projects you want.
<br>

   ```python
   
   from utils.downloader import NFT1000
   
   local_repo_path = "path/to/local/repo"
   # modfiy the NFT_name_list to the NFT projects you want to download
   NFT_name_list = ["BoredApeYachtClub", "CRYPTOPUNKS"]
   
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   NFT1000.download(NFT_name_list)
   
   ```

   <br>

   🤔 Sometime you may can't remember the NFT project name clearly ……

   Don't worry, NFT-NET-HUB can give you some suggestions, such as:



   ```python
   
   from utils.downloader import NFT1000
   
   local_repo_path = "path/to/local/repo"
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   NFT1000.download(["BoredApe"])
   
   # Error: BoredApe not in repo_info, do you mean [('DAPE', 0.67), ('BoredApeYachtClub', 0.64), ('BoredApeKennelClub', 0.62)]?
   
   ```

   or

   ```python
   
   from utils.downloader import NFT1000
   
   local_repo_path = "path/to/local/repo"
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   NFT1000.query("BoredApe")
   
   # Error: BoredApe not in repo_info, do you mean [('DAPE', 0.67), ('BoredApeYachtClub', 0.64), ('BoredApeKennelClub', 0.62)]?
   
   ```

   or

   ```python
   
   from utils.downloader import NFT1000
   local_repo_path = "path/to/local/repo"
   
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   print(NFT1000.get_NFT_name_list())
   # ['BoredApeYachtClub', 'CRYPTOPUNKS', 'MutantApeYachtClub', 'Azuki', 'CloneX', 'Moonbirds', 'Doodles',……]
   
   ```

<br>

👋 If you want to download all NFT projects, just：
   ```python
   
   from utils.downloader import NFT1000
   local_repo_path = "path/to/local/repo"
   
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   NFT1000.download_all()
   
   ```

But be careful, this might take a long time, so please ensure your internet connection is stable and fast🚀


<br>

### 3. Unzip NFT Projects

The projects in the NFT1000 dataset are all stored in **.zip** format. After downloading your desired project, you can easily unzip it using the tools provided by the NFT-NET-HUB package. Here is an example of how to do this:

```python
from utils.downloader import NFT1000
local_repo_path = "path/to/local/repo"
NFT1000 = NFT1000("NFT1000", local_repo_path)

NFT_name_list = ["BoredApeYachtClub", "CRYPTOPUNKS"]

NFT1000.unzip(NFT_name_list)
```

<br>

👋 If you want to unzip all NFT projects, just：

```python

from utils.downloader import NFT1000
local_repo_path = "path/to/local/repo"

NFT1000 = NFT1000("NFT1000", local_repo_path)
NFT1000.unzip_all()

```

<br>

### 4. Query

Query the Information of a specific NFT Project.

   ```python
   
   from utils.downloader import NFT1000
   
   local_repo_path = "path/to/local/repo"
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   print(NFT1000.query("BoredApeYachtClub"))
   
   # {'project_name': 'BoredApeYachtClub', 'contract_address': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', 'total_supply': 10000, 'actual_collected_quantity': 10000, 'description': 'The [Bored Ape Yacht Club](https://boredapeyachtclub.com/) NFTs are a collection of 10,000 unique Bored Ape Non Fungible Tokens. A Bored Ape serves as your access to the Yacht Club, and gives access to many members-only features, the first of which is access to THE BATHROOM, a collaborative graffiti board. BAYC is one of many NFT collections by Yuga Labs and has quickly become a cultural phenomenon. ', 'official_url': 'http://www.boredapeyachtclub.com/', 'opensea_url': 'https://opensea.io/collection/boredapeyachtclub', 'checksum_sha256': 'ea1355ed1644a1c8d23b9cd1e5797570af9594c6a331223ae4f55ae9d13805b2'}
   
   ```



Query the Information of a specific NFT Project.

   ```python
   
   from utils.downloader import NFT1000
   
   local_repo_path = "path/to/local/repo"
   NFT1000 = NFT1000("NFT1000", local_repo_path)
   print(NFT1000.query("validation_list"))
   
   # ['Claylings', 'Vogu', 'Not Your Bro', 'Lucky Lion CLub', 'Thingdoms NFT Official', 'Infinity Frogs', 'Los Muertos', 'Pop Art Cats', 'CryptoZombiez', 'Lonely Frog Lambo Club', 'Untamed Elephants', 'Fluffy Polar Bears', 'Non Fungible Frens', 'MEGAMI', 'TCG World Dragons', 'E_Shell', 'Women Tribe', 'Isekai Meta', 'Alien Frens Evolution', 'CryptoPolz', 'Darkflex', 'LostSoulsSanctuary', 'Little Lemon Friends', 'TheWickedStallions', 'The Chimpsons', 'HAPE EXODUS', 'AlphieWhales', 'Lazy Ape Yacht Club', 'Tropical Turtles', 'Tribe Odyssey', 'OnChainBirds', 'Angry Boars', 'Fishy Fam', 'Angry Ape Army Evolution Collection', 'GOBLIN GRLZ', '0xApes', 'AuctionMintContract', 'Pixelated Llama', 'Rebel Seals', 'Mini Supers', 'mems', 'DIOs Genesis', 'HUGO x IO', 'Goopdoods', 'Bibiz', 'Queens+KingsAvatars', 'The Ninja Hideout', 'illogics', 'FoxFam', 'Crypto Bear Watch Club']
   
   ```



👋For more usage and requests, please submit an issue to us.

<br>
<br>

## Contributors

Thank you 🙏 to all our contributors!

<a href="https://github.com/ShuxunoO/NFT-Net/graphs/contributors">
<img src="https://contrib.rocks/image?repo=ShuxunoO/NFT-Net" alt="NFT-NET contributors"></a>

<br>
<br>

## Parters



![Parters](assets/Parter.png)

<br>

## Authors and Citation

   ```
@inproceedings{
wang2024nft,
title={{NFT}1000: A Cross-Modal Dataset For Non-Fungible Token Retrieval},
author={Shuxun Wang and Yunfei Lei and Ziqi Zhang and Wei Liu and Haowei Liu and Li Yang and Bing Li and Wenjuan Li and Jin Gao and Weiming Hu},
booktitle={ACM Multimedia 2024},
year={2024},
url={https://openreview.net/forum?id=xUtNrKH8iB}
}

   ```
