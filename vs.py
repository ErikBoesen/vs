#!/usr/bin/env python3

import argparse
import os
import json
import csv
from termcolor import colored as c


class VS:
    """Manage data operations independent of user input."""

    def dump(self, data):
        """
        Output list of match data into `data.json` file.

        :param data: List (or, in theory, other data) to dump.
        """
        with open('data.json', 'w') as f:
            f.write(json.dumps(data))

    def load(self, filename):
        """
        Load JSON data from file.

        :param file: Name of file to load data from.
        """
        try:
            with open(filename) as f:
                return json.loads(f.read())
        except OSError:
            return []

    def consolidate(self, directory):
        """
        Load all JSON files in a directory and consolidate them into one file.

        :param directory: Directory to find JSON files in.
        """
        # TODO: Unbundle all file I/O from this method.
        files = [f for f in os.listdir(directory) if f.endswith('.json')]
        if len(files) and not files[0].endswith('data.json'):
            matches = []

            for f in files:
                print('Parsing %s...' % f)
                try:
                    matches += self.load(f)
                except json.decoder.JSONDecodeError:
                    files.remove(f)
                    print(c('File \'%s\' has parsing errors. Resolve and run again.' % f.split('/')[-1], 'red'))

            for f in files:
                os.remove(f)

            matches.sort(key=lambda match: (match['team'], match['match']))

            return matches
        else:
            return []

    def conflict(self, data):
        """
        Handle conflicting and duplicate match data.

        :param data: Scouting data to search for duplicates and conflicts.
        """
        remove = []
        if len(data) > 1:
            for i in range(1, len(data)):
                pre = data[i]
                cur = data[i-1]
                if pre == cur:
                    remove.append(i-1)
                elif pre['match'] == cur['match'] and pre['team'] == cur['team']:
                    print(c('Team #%s was scouted differently twice in match #%s. Here are the two data:' % (pre['team'], cur['match']), 'red'))
                    print(('%s: ' % (i-1)) + str(pre))
                    print(('%s: ' % i) + str(cur))
                    choice = int(input(c('Please select the data you want to remove by typing 1 or 2: ', 'blue')))
                    remove.append(i + (choice - 2))

        for index in reversed(remove):
            print('Removing duplicate data point %s...' % index)
            del data[index]

        print(c('All conflicts and duplication eliminated.' if len(remove) else 'No duplicate or conflicting data found.', 'green'))

        return data

    def csv(self, data, csvfile):
        """
        Convert JSON scouting data into a CSV spreadsheet.

        :param data: Scouting data to convert.
        :param csvfile: Name of file to output CSV content to.
        """
        try:
            os.remove('%s.csv' % csvfile)
        except OSError:
            pass

        dest = csv.writer(open('data.csv', 'w+', newline=''))

        # Write header
        dest.writerow([k for k in data[0].keys()])

        for match in data:
            dest.writerow([match[i] for i in match])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VictiScout data.')
    parser.add_argument('command', type=str, help='What you want to do.')

    args = parser.parse_args()

    vs = VS()
    try:
        data = vs.load('data.json')
    except json.decoder.JSONDecodeError:
        data = []

    if args.command.startswith('cons'):
        consolidated = vs.consolidate(os.getcwd())
        if consolidated == []:
            print(c('No unconsolidated scouting JSON in current directory.', 'blue'))
        else:
            print(c('Data successfully consolidated.', 'green'))
            vs.dump(consolidated)
    elif args.command.startswith('conf'):
        vs.dump(vs.conflict(data))
    elif args.command == 'csv' or args.command == 'ss' or args.command == 'spreadsheet':
        if os.path.exists('data.json'):
            vs.csv(data, 'data')
        else:
            print('Error: No valid scouting JSON in the current directory.')
    else:
        print('Unknown command %s.' % args.command)
