#!/bin/env bash

SERVER_LIST="server01 server02 server03"

for h in $SERVER_LIST; do
    ip=$(dig +search +short $h)
    ssh-keygen -R $h
    ssh-keygen -R $ip
    ssh-keyscan -H $ip >> ~/.ssh/known_hosts
    ssh-keyscan -H $h >> ~/.ssh/known_hosts
done