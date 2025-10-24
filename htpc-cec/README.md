# Control devices over HDMI-CEC

This project creates 2 programs:
- `htpc-cecd`: a daemon that opens the Pulse-Eight adapter device using libcec, then listens for commands on a posix message queue.
- `htpc-cec`: a client program that sends commands to the daemon using the message queue. This is what should be called when the buttons on a remote are pressed.

## Local Development

1. Install dependencies by running `install_deps_ubuntu.sh`. If on Bazzite, it will need to be run inside an ubuntu distrobox container.
2. `uv sync`

Make a change
run the client: `uv run src/htpc-cec`
run the daemon: `uv run src/htpc-cec-daemon`

## Build both client and daemon as single-file executables:

`just build-htpc-cec`

The executables will be in the `dist` folder. They will also be copied into the `system_files/usr/bin` folder so the Containerfile will grab them when building the full image.

`just build` has a dependency on `build-htpc-cec`, so it will always run first.
