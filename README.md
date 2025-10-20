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

### Fixed

- ✅ ssh connexion between ansible container to other server.

### Open

- ❌ argcomplete not working yet.
