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
dnf5 -y install python3-devel libcec-devel
# pip needs to install things in /usr/local/lib64.
# But this directory doesn't exist at this point in the build (I have no idea when/who creates it.)
# According to https://www.bootc-dev.github.io/bootc/filsystem.html#usrlocal, the /usr/local directory is symlinked to /var/usrlocal.
# Not even usrlocal exists at this point, so we just create it so pip is happy.
# As soon as I added this, `bootc container lint` started getting mad, and it's going to stay mad until I figure out the correct way to do this.
mkdir -p /var/usrlocal/lib64
pip install /ctx/htpc_cec-0.1.0-py3-none-any.whl
systemctl enable htpc-cec
