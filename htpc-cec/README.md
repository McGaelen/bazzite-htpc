# Control devices over HDMI-CEC

## Local Development

1. Install dependencies by running `install_deps_ubuntu.sh`. If on Bazzite, it will need to be run inside an ubuntu distrobox container.
2. `uv sync`

Make a change
run the client: `uv run src/htpc-cec`
run the daemon: `uv run src/htpc-cec-daemon`

## Build both client and daemon as single-file executables:

`just build-htpc-cec`

The executables will be in the `dist` folder. They will also be copied into the `../build_files` folder so the Containerfile will grab them when building the full image.

`just build` has a dependency on `build-htpc-cec`, so it will always run first.
