from git import Repo
import os
import system


def fetch_sources():
    # Validate that we are cloning into correct directory
    verification_file = system.current_path() + "/ccbuild-files/is_correct_file"
    verification_source = system.current_path() + "/ccbuild-files/.sources_exist"

    if system.is_file(verification_file):
        first_buffer = system.readf(verification_file)
        # Is correct file
        if not first_buffer.find("true"):
            raise Exception("\n\tPoky-build verification failed\n")
    # Not in correct directory
    else:
        raise Exception("\n\tThis command should be executed within the "
                        "root directory of poky clone.\n"
                        "\trun: 'ccbuild fetch poky' before "
                        "executing this command\n")

    # Validate whether previous sources exists
    if system.is_file(verification_source) is False:
        print("\n\tSources already exists. Proceeding without "
              "fetching the new sources")
        return

    # Initialize the process
    print("Initializing process to fetch meta-data\n")


class build_poky:
    __source_dir = os.getcwd()
    __sources_path = []
    __upstream_sources = []

    def __init__(self, raspberry=False):
        self.__upstream_sources.append(["git://git.yoctoproject.org/meta-security",
                                        "git://git.yoctoproject.org/meta-arm",
                                        "git://git.yoctoproject.org/meta-openssl102",
                                        "git://git.yoctoproject.org/dbus-wait",
                                        "git://github.com/meta-qt5/meta-qt5.git",
                                        "git://git.yoctoproject.org/qemugl",
                                        "git://git.yoctoproject.org/eclipse-yocto",
                                        "git://git.yoctoproject.org/yocto-buildstats",
                                        "git://git.yoctoproject.org/meta-external-toolchain",
                                        "git://git.yoctoproject.org/meta-yocto"])
        if raspberry is True:
            self.__upstream_sources.append("git://git.yoctoproject.org/meta-raspberrypi")

    def sources_exist(self):
        # Append directory view
        for i in range(len(self.__upstream_sources)):
            link = self.__upstream_sources[i]
            data = link[link.rfind('/'):]
            self.__sources_path.append(self.__source_dir + data)

    @staticmethod
    def print_menu():
        print("\nCalcOs poky builder"
              "\n\t-f\t--fetch\t\tfetch meta data and related tools"
              "\n\t-h\t--help\t\tprint this menu and exit"
              "\n\t-r\t--raspberry\tbuild project for raspberry-pi range of devices")
        exit(SystemExit)
