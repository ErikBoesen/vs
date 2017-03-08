#!/usr/bin/env python3

import argparse
import os
import json

parser = argparse.ArgumentParser(description='Process VictiScout data.')
parser.add_argument('command', type=str, help='What you want to do.')

args = parser.parse_args()

if args.command.startswith('cons'):
    files = ['%s/%s' % (os.getcwd(), f) for f in os.listdir(os.getcwd()) if f.endswith('.json')]
    if len(files):
        matches = []

        for f in files:
            matches += json.loads(open(f).read())
            os.remove(f)

        open('%s/data.json' % (os.getcwd()), 'w').write(json.dumps(matches))
    else:
        print('Error: No valid scouting JSON in the current directory.')
else:
    print('Unknown tool %s.' % (args.tool))
