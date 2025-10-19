#!/bin/bash

set -ouex pipefail

### Install packages

# Packages can be installed from any enabled yum repo on the image.
# RPMfusion repos are available by default in ublue main images
# List of rpmfusion packages can be found here:
# https://mirrors.rpmfusion.org/mirrorlist?path=free/fedora/updates/39/x86_64/repoview/index.html&protocol=https&redirect=1

# ========== keyd ==========
dnf5 -y copr enable alternateved/keyd
dnf5 -y install keyd
dnf5 -y copr disable alternateved/keyd
systemctl enable keyd

# ========== ydotool ==========
# comes pre-installed on bazzite
systemctl enable ydotool

# ========== htpc-cec ==========
cp /ctx/htpc-cec /usr/bin
cp /ctx/htpc-cecd /usr/bin
systemctl enable htpc-cec

# ========== disable steam from starting up automatically ==========
mv /etc/xdg/autostart/steam.desktop /etc/xdg/autostart/steam.desktop.DISABLED