# {{site_name}}
# {{server_admin}}
import os
import shutil
import sys
import zipfile
from pathlib import Path

import click

BASE_DIR = Path(sys.argv[0]).resolve().parent
TEMP_DIR = sys._MEIPASS
# TEMP_DIR = os.path.join(BASE_DIR, "temp")
DOCKER_ZIP = os.path.join(TEMP_DIR, "docker.zip")


def main() -> None:
    if os.path.exists(os.path.join(DOCKER_ZIP, "docker")):
        shutil.rmtree(os.path.join(DOCKER_ZIP, "docker"))

    with zipfile.ZipFile(DOCKER_ZIP, "r") as _zip:
        _zip.extractall(TEMP_DIR)

    DOCKER_BASE_DIR = os.path.join(TEMP_DIR, "docker")
    DOCKER_BUILD_DIR = os.path.join(BASE_DIR, "build")

    # docker.compose.up()
    # docker.run("hello-world")
    print("BASE_DIR", BASE_DIR)
    print("TEMP_DIR", TEMP_DIR)
    print("DOCKER_ZIP", DOCKER_ZIP)
    print("DOCKER_BASE_DIR", DOCKER_BASE_DIR)
    print("DOCKER_BUILD_DIR", DOCKER_BUILD_DIR)

    project_name = click.prompt("Enter django project name", type=str, default="django")
    server_admin_email = click.prompt("Enter server admin email", type=str, default="admin@admin.com")

    to_edit = [
        r"docker-compose.yml",
        r"apache_django.conf",
        r"Dockerfile",
    ]

    if os.path.exists(DOCKER_BUILD_DIR):
        shutil.rmtree(DOCKER_BUILD_DIR)
    # os.mkdir(DOCKER_BUILD_DIR)
    shutil.copytree(DOCKER_BASE_DIR, DOCKER_BUILD_DIR)

    for file in to_edit:
        file_path = os.path.join(DOCKER_BUILD_DIR, file)
        new_lines = []
        with open(file_path) as f_read:
            for line in f_read.readlines():  # noqa: FURB129
                _line = line
                if "{{site_name}}" in line:
                    _line = line.replace("{{site_name}}", project_name)
                if "{{server_admin}}" in line:
                    _line = line.replace("{{server_admin}}", server_admin_email)
                new_lines.append(_line)

        with open(file_path, "w+") as f_write:
            f_write.writelines(new_lines)
    print(DOCKER_BUILD_DIR)
    # ./docker-compose.yml  ->  {{site_name}}
    #  apache_django ->  {{site_name}} | {{server_admin}}
    # ./Dockerfile ->  {{site_name}}


if __name__ == "__main__":
    main()
