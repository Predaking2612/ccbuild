import sys
import system
import build_poky
import yaml


def value_exists(search, in_):
	if in_ is None:
		return False

	for i in in_:
		if search == i:
			return True
	return False


class ArgParse:
	__about = ""
	__list = []
	__config_dir = system.current_path() + "/ccbuild-files"

	def print_help_menu(self):
		print(self.__about)
		print("arguments:\n"
		      "  help\t\t\t\tshow this help message and exit\n"
		      "  fetch [args...]\tfetch sources necessary to build calcos")

	def __init__(self, about="", lst=None):
		self.__list = lst
		if len(about) >= 4:
			self.__about = about
		else:
			self.__about = "calcos automation unit\n\n"

	def parse(self):
		if len(sys.argv) <= 1:
			self.print_help_menu()
		else:
			arg = sys.argv
			i = 1
			while i != len(arg):
				if arg[i] == "fetch":
					if arg[i + 1] == "poky":
						if value_exists("poky", self.__list):
							print("Cannot proceed with this option as sources for this already exists.")
							exit(-1)
						else:
							dictionary = [{'fetch': ['poky']}]
							config_file = self.__config_dir + "/ccbuild_config.yaml"
							with open(config_file, 'w') as file:
								docs = yaml.dump(dictionary, file)
							return build_poky.build_poky()
				else:
					print("fetch requires additional arguments: "
					      "\n\t[PhiX, PhiX-cpp, calcos-kern, poky, help]\n"
					      "\tPhiX-cpp\tto build C++ version of front-end\n"
					      "\tPhiX\t\tto build PhiX-lang version of front-end\n"
					      "\tcalcos-kern\tto build custom kernel for the operating system\n"
					      "\tpoky\t\tto build CalcOs running on Embedded Linux Kernel\n"
					      "\thelp\t\tprint this menu and exit\n")
					exit(-1)

				i += 1
