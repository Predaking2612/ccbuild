#!/bin/env python

import ArgParse as ap


def config_check():
	import system
	import os
	import yaml

	config_dir = system.current_path() + "/ccbuild-files"
	config_file = config_dir + "/ccbuild_config.yaml"
	if not system.is_dir(config_dir):
		print("Creating ccbuild-files directory at", config_dir)
		os.mkdir(config_dir)
		return
	else:
		if not system.is_file(config_file):
			print("Generating ccbuild_config.yaml in configuration directory")
			file = open(config_file, "w+")
			file.close()
		else:
			config_data = open(config_file)
			parsed = yaml.load(config_data, Loader=yaml.FullLoader)
			return parsed.get("fetch")


def parse_cli(config_list):
	args = ap.ArgParse(lst=config_list)
	fetch = args.parse()


def init():
	config_list = config_check()
	parse_cli(config_list)


"""
	Upon initialization, script will check for 'ccbuild_config.yaml' file
	This will be used to get flag values
"""
if __name__ == '__main__':
	init()
