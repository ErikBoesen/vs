#!/usr/bin/env python3

import argparse
import os
import json

parser = argparse.ArgumentParser(description='Process VictiScout data.')
parser.add_argument('tool', type=str, help='What you want to do.')
parser.add_argument('-d', dest='dir', help='Directory to process files from.')

args = parser.parse_args()
print(args.tool)

if args.tool == 'gather':
    # TODO: Is there an easier way to get full paths to listed directories?
    files = ['%s/%s' % (args.dir, f) for f in os.listdir(args.dir) if f.endswith('.json')]
    print(files)
    matches = []

    for f in files:
        matches += json.loads(open(f).read())
        os.remove(f)

    open('%s/data.json' % (args.dir), 'w').write(json.dumps(matches))

else:
    print('Unknown tool %s.' % (args.tool))
