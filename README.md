# `vs`
Convenient CLI app for manipulation of [VictiScout](https://github.com/frc1418/VictiScout) data.

## Installation
* Install `python3`.
* Clone the `vs` repository and move into it:

        git clone https://github.com/frc1418/vs && cd vs

* Copy `vs.py` to an executable location, for example:

        cp vs.py /usr/local/bin/vs

    Make sure to use `chmod +x vs.py` to mark the script as executable if necessary.

## Tools
Tools are being added as needed, so for now they're few. That will gradually change.
* `gather <directory>` - combine many different JSON scouting data files into one.

        vs gather collection

    would compile all valid scouting data files in the directory `collection/` into `collection/data.json`.
