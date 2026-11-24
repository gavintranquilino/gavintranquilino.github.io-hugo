# Shared development environment. See README.md in this directory.
#
# This stage is named "dev" so that build and runtime stages can be added to
# the same file later without changing devcontainer.json.

ARG UBUNTU_VERSION=26.04
FROM ubuntu:${UBUNTU_VERSION} AS dev

ARG USERNAME=dev

ENV LANG=C.UTF-8

# General tools for working in any repository. Python 3 runs the repository
# checks in tools/scripts/.
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bash-completion \
        ca-certificates \
        curl \
        git \
        less \
        nano \
        openssh-client \
        python3 \
        sudo \
        unzip \
        xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Hugo builds and previews the site. The deploy workflow reads this version
# from this line, so change it only here. The standard edition is enough,
# because the site uses no Sass and no WebP encoding. The release checksum is
# verified before Hugo is installed.
ARG HUGO_VERSION=0.127.0
RUN arch="$(dpkg --print-architecture)" \
    && archive="hugo_${HUGO_VERSION}_linux-${arch}.tar.gz" \
    && checksums="hugo_${HUGO_VERSION}_checksums.txt" \
    && cd /tmp \
    && curl -fsSLO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${archive}" \
    && curl -fsSLO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${checksums}" \
    && grep " ${archive}\$" "${checksums}" | sha256sum -c - \
    && tar -xzf "${archive}" -C /usr/local/bin hugo \
    && rm "${archive}" "${checksums}" \
    && hugo version

# Ubuntu images include a user named ubuntu with ID 1000, the usual ID of the
# first user on a Linux host. Rename it so the container user owns files in
# the mounted workspace the same way the host user does. The user can run sudo
# without a password, to try out packages before adding them to this file.
RUN usermod --login "${USERNAME}" --move-home --home "/home/${USERNAME}" ubuntu \
    && groupmod --new-name "${USERNAME}" ubuntu \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > "/etc/sudoers.d/${USERNAME}" \
    && chmod 0440 "/etc/sudoers.d/${USERNAME}"

USER ${USERNAME}
