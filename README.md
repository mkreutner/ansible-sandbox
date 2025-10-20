# ansible-sandbox

Ansible Sandbox

## Requirements

- docker
- just

## Getting start

```shell
# initialise environment file
just setup
# build image
just build
# start stack
just up
# connect into ansible
just shell
# prepare working environment
install_all.sh
init_ssh.sh
# enjoy !
cd workspace
uv run ansible --help
```

## Known issues

- [FIXED] argcomplete not working yet
