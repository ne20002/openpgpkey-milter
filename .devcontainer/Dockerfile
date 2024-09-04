# Use the Debian base image
FROM mcr.microsoft.com/devcontainers/base:bookworm

# Install necessary dependencies
RUN apt-get update

# Install Python
RUN apt-get install -y python3 python3-pip \
    python3-unbound \
    python3-milter \
    python3-requests \
    python3-setproctitle

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]