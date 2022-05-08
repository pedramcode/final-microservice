import requests
from config import settings
import subprocess


def prepare_contract():
    res = requests.get(f"http://{settings.CONTRACT_HOST}:{settings.CONTRACT_PORT}/contract/user")
    with open("./buffers/user.proto", "w") as _file:
        _file.write(res.text)
    script = subprocess.Popen(["./compile_protoc.sh"], stdin=subprocess.PIPE)
    script.wait()
