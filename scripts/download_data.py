import gdown
import os

def download_from_gdrive(url: str, output: str, filename: str) -> bool:
    """
    function to download files from gdrive

    Args:
        url      (str) :   gdrive url of that file e.g. 'https://drive.google.com/uc?id=<file_id>'
        output   (Str) :   output path e.g. './data/raw'
        filename (str) :   name to downloaded file

    Returns:
        True    (bool) :   download successfull.
        False   (bool) :   need to check
    """

    output_path = os.path.join(output, filename)
    if os.path.exists(output_path):
        print("file already exist")
        return False

    try:
        gdown.download(url, output_path, quiet=False)
        print(f"Downloaded at : {output_path}")
        return True

    except Exception as e:
        print(f"An error occured : {e}")
        return False


raw_data_url = "https://drive.google.com/uc?id=1GpZPTAlMxa6ZrQ9Eu3CnkNLZUVPsIJFY"
raw_output_path = "./data/raw"

download_from_gdrive(raw_data_url, output=raw_output_path, filename="city_hour.csv")
