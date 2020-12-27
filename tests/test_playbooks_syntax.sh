#!/bin/bash
# from https://stackoverflow.com/a/4774063
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

for filename in ${SCRIPTPATH}/../playbooks/*.yml; do
  ansible-playbook $filename --syntax-check
done