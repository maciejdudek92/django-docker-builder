import os
from pathlib import Path

import PyInstaller.__main__



def build() -> None:
    # zip_file = os.path.join(Path(__file__).resolve().parent, "docker.zip")
    # docker_folder = os.path.join(Path(__file__).resolve().parent, "docker")
    # print(docker_folder)

    # if os.path.exists(zip_file):
    #     os.remove(zip_file)

    # with zipfile.ZipFile(zip_file, "w") as _zip:
    #     for folder_name, subfolders, filenames in os.walk(docker_folder):
    #         for filename in filenames:
    #             # Create complete filepath of file in directory
    #             file_path = os.path.join(folder_name, filename)
    #             # Add file to zip
    #             _zip.write(file_path)

    # sys.exit()

    script_path = os.path.join(Path(__file__).resolve().parent, "main.py")
    build_path = os.path.join(Path(__file__).resolve().parent.parent, "release")

    pyi_args = [script_path, "--onefile", "--noconfirm", "--console", f"--distpath={build_path}", "--add-data=docker.zip;."]

    PyInstaller.__main__.run(
        pyi_args,
    )


if __name__ == "__main__":
    build()
