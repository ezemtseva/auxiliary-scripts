#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from genestack_client import (GenestackServerException, get_connection,
                              make_connection_parser)

from importers import TemplateImporter
from importers import format as tf


def main():
    parser = make_connection_parser()
    parser.add_argument('paths', metavar='<path>', nargs='+',
                        help='one or more paths to configuration files')
    args = parser.parse_args()

    config_paths = args.paths
    print('Number of templates to be updated: %d' % len(config_paths))

    connection = get_connection(args)
    importer = TemplateImporter(connection)
    for path in config_paths:
        try:
            importer.create_from_config(path)
        except GenestackServerException as e:
            print(tf.colored("  Got an error from server:\n{}".format(e.message),
                             tf.Color.RED), file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
