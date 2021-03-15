#!/bin/env python

import ArgParse as ap


def parse_cli():
    args = ap.ArgParse()
    fetch = args.parse()


def init():
    parse_cli()


if __name__ == '__main__':
    init()
