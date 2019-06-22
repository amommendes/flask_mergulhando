#!/bin/bash
C_GREEN='\e[32m'
C_RED='\e[31m'
C_ORANGE='\e[33m'
C_CYAN='\e[35m'
C_WHITE='\e[37m'
C_NONE='\e[0m'

info=" ${C_GREEN} [INFO] ${C_NONE}"
error=" ${C_RED} [ERROR] ${C_WHITE}"


echo $(date "+%Y-%m-%d %H:%M:%S") ${info}Starting Mergulhando Application
cd docker
echo $(date "+%Y-%m-%d %H:%M:%S") ${info}Stopping Services
docker-compose stop
echo $(date "+%Y-%m-%d %H:%M:%S") ${info} Starting Services:
docker-compose up -d

rc=$?

if [ "${rc}" -eq "0" ]; then
    echo $(date "+%Y-%m-%d %H:%M:%S") ${info} Containers started
else
    echo $(date "+%Y-%m-%d %H:%M:%S") ${error} Error while starting containers
    exit 1
fi
exit 0