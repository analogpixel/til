# Python cli template

Simple template for creating a CLI app in python:

```python
#!/usr/bin/env python

import argparse
import toml
import os.path

if __name__ == '__main__':

    # load app configuration
    config_path =os.path.expanduser("~/.app_config.toml")
    if os.path.exists( config_path ):
        config = toml.load( config_path) 

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', dest="dryRun", default=False, action='store_true', help='dryRun', required=False)
    parser.add_argument('non_flag_arg_all', nargs='*', default='')  # everything that wasn't defined

    # add a sub-command
    subparsers = parser.add_subparsers(dest='subparser')
    parser_a = subparsers.add_parser('cmd_a')
    parser_a.add_argument('arg1', nargs='+') 

    args = parser.parse_args()

    if args.subparser == 'arg1':
        pass
```
