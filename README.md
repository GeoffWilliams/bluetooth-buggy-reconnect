# bluetooth-buggy-reconnect

A linux command line tool to automatically reconnect buggy trusted bluetooth devices.
This project was forked from bluetooth-autoconnect by Jonathan Rouleau.

## Requirements

* Requires `python3`, `pygobject`, and `bluez`

## Installation

* Install the `bluetooth-buggy-reconnect` script to somewhere in your `PATH`, such as `/usr/local/bin/`
* If you are using systemd, consider installing the `bluetooth-buggy-reconnect.service` file to `/etc/systemd/system/` and modifying it to reflect the location of where you installed the script
  - Enable the service with `sudo systemctl enable bluetooth-buggy-reconnect`

## Usage

```sh
Usage: bluetooth-buggy-reconnect [OPTIONS]...

Automatically connect to trusted buggy bluetooth devices

OPTIONS:
  -h, --help        Print this help message
  -v, --verbose     Show more detailed log messages

```

## License

MIT License

Copyright (c) 2019 Jonathan Rouleau
Copyright (c) 2020 Yuri Konotopov
