# ytdl

Rust command line app to download youtube videos.

## Install

`ytdl` requires the nightly compiler. Install `rustup` to manage multiple
toolchains and run `rustup override set nightly` to use the nightly compiler
for the current directory.

## Dependencies

`ytdl` depends on the following crates (downloaded automatically by cargo):

- `rustube`
- `pico_args`

## Running

Build the project using `cargo build`. The binary will be present in `./target/debug/ytdl`.
Use `ytdl --help` to see all options.

![ytdl demo](https://i.imgur.com/pzvsmQn.jpg)
