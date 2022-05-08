#!/bin/bash

./.venv/bin/python -m grpc_tools.protoc --proto_path="./buffers" --python_out="./" --grpc_python_out="./" ./buffers/user.proto