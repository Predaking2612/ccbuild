import sys
import build_poky


class ArgParse:
    __about = ""

    def print_help_menu(self):
        print(self.__about)
        print("arguments:\n"
              "  help\t\t\t\tshow this help message and exit\n"
              "  fetch [args...]\tfetch sources necessary to build calcos")

    def __init__(self, about=""):
        if len(about) >= 4:
            self.__about = about
        else:
            self.__about = "calcos automation unit\n\n"

    def parse(self):
        if len(sys.argv) <= 1:
            self.print_help_menu()
        else:
            for i, arg in enumerate(sys.argv):
                if arg == "fetch":
                    if arg[i + 1] == "poky":
                        return build_poky.build_poky
                else:
                    print("fetch requires additional arguments: "
                          "\n\t[PhiX, PhiX-cpp, calcos-kern, poky, help]\n")
                    print("\tPhiX-cpp\tto build C++ version of front-end\n"
                          "\tPhiX\t\tto build PhiX-lang version of front-end\n"
                          "\tcalcos-kern\tto build custom kernel for the operating system\n"
                          "\tpoky\t\tto build CalcOs running on Embedded Linux Kernel\n"
                          "\thelp\t\tprint this menu and exit\n")
                    exit(-1)
