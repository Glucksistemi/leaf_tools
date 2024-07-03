
IMAGE_BASE_NAME=leaf_tools
CONTAINER_BASE_NAME=leaf_tools

declare -A COMMANDS


declare -A DOCKER_PARAMS
# launch parameters for every environment
DOCKER_PARAMS["localhost"]=""
DOCKER_PARAMS["test"]=""
DOCKER_PARAMS["prod"]=""

declare -A VOLUMES
# volume setup for every environment

declare -A NETWORK
# docker networking parameters for every environment
NETWORK["localhost"]="--network=host"
NETWORK["test"]="--network=host"
NETWORK["prod"]="--network=host"
