#!/bin/env bash

if [ -f ~/INSTALL_DONE ]; then
    exit 0
fi

# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="~/.local/bin:$PATH"
# create working workplace
mkdir ~/workspace
cd ~/workspace
# init uv project
uv init
# install ansible and argcomplete
uv add ansible
uv add argcomplete
# activate argcomplete
activate-global-python-argcomplete

