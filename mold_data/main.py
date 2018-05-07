#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function

import argparse
import sys
import urllib2
import json

from mold_data import metadata


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    url = 'http://open.canada.ca/data/en/api/3/action/package_search?q=spendingpackage_search?q='
    final_url = url + 'spending'
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    result = data['result']
    results = result['results']
    for item in results:
        print(item['license_title'])

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
