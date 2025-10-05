#!/bin/bash

set -ouex pipefail

### Install packages

# Packages can be installed from any enabled yum repo on the image.
# RPMfusion repos are available by default in ublue main images
# List of rpmfusion packages can be found here:
# https://mirrors.rpmfusion.org/mirrorlist?path=free/fedora/updates/39/x86_64/repoview/index.html&protocol=https&redirect=1

dnf5 -y python3-devel

# ========== keyd ==========
dnf5 -y copr enable alternateved/keyd
dnf5 -y install keyd
dnf5 -y copr disable alternateved/keyd
systemctl enable keyd

# ========== ydotool ==========
# comes pre-installed on bazzite
systemctl enable ydotool

# ========== Papirus icons ==========
# https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
wget -O papirus.tar.gz https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/master.tar.gz
tar -xzf papirus.tar.gz -C papirus
cp -R papirus/* /home/bazzite/.local/share/icons

# ========== Prevent user-switching ==========
patch < /ctx/multiuser.patch
