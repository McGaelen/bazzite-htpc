# Control devices over HDMI-CEC

## Local Development

1. Install dependencies by running `install_deps_ubuntu.sh`. If on Bazzite, it will need to be run inside an ubuntu distrobox container.
2. `uv sync`

Make a change then run `uv build`
run the client: `uv run -m htpc-cec`
run the daemon: `uv run -m htpc-cec-daemon`
