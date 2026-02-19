import zipfile
import tempfile
import os


def extract_zip(zip_file):
    """
    Extract uploaded zip file to a temporary directory
    and return the extracted folder path.
    """
    temp_dir = tempfile.mkdtemp()

    zip_path = os.path.join(temp_dir, "uploaded.zip")
    zip_file.save(zip_path)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    return temp_dir
