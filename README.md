# `vs`
Convenient CLI app for manipulation of [VictiScout](https://github.com/frc1418/VictiScout) data. Also works with any compatible JSON-format data.

## Installation
* Install `python3`.
* Clone the `vs` repository and move into it:

        git clone https://github.com/frc1418/vs && cd vs

* Copy `vs.py` to an executable location, for example:

        cp vs.py /usr/local/bin/vs

    Make sure to use `chmod +x vs.py` first to mark the script as executable if necessary.

## Commands
Commands are being added as needed, so for now they're few. That will gradually change.
* `vs cons` - consolidate all JSON scouting data files in the working directory into one.
* `vs csv`/`spreadsheet`/`ss` - convert raw JSON file into a CSV spreadsheet. [drv](https://github.com/ErikBoesen/drv) can be used to easily send this file to Google Drive for manipulation without any proprietary programs.
* `vs conf` - remove duplicate matches.
