#!/usr/bin/env python3

import argparse
import os
import json
import csv
from termcolor import colored

parser = argparse.ArgumentParser(description='Process VictiScout data.')
parser.add_argument('command', type=str, help='What you want to do.')

args = parser.parse_args()

if args.command.startswith('cons'):
    files = ['%s/%s' % (os.getcwd(), f) for f in os.listdir(os.getcwd()) if f.endswith('.json')]
    dest = '%s/data.json' % os.getcwd()
    if len(files):
        matches = []

        for f in files:
            print('Parsing %s...' % f)
            try:
                matches += json.loads(open(f).read())
            except json.decoder.JSONDecodeError:
                files.remove(f)
                print(colored('File \'%s\' has parsing errors. Resolve and run again.' % f.split('/')[-1], 'red'))

        for f in files:
            os.remove(f)

        open(dest, 'w').write(json.dumps(matches))
        print('Data moved into %s successfully.' % dest)
    else:
        print('Error: No valid scouting JSON in the current directory.')
elif args.command == 'csv' or args.command == 'ss' or args.command == 'spreadsheet':
    if os.path.exists('%s/data.json' % os.getcwd()):
        try:
            os.remove('%s/data.csv' % os.getcwd())
        except OSError:
            pass
        matches = json.loads(open('data.json').read())
        dest = csv.writer(open('data.csv', 'w+', newline=''))

        # Write header
        dest.writerow([k for k in matches[0].keys()])

        for match in matches:
            dest.writerow([match[i] for i in match])

    else:
        print('Error: No valid scouting JSON in the current directory.')
else:
    print('Unknown command %s.' % args.command)
