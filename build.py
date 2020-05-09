#!/usr/bin/env python
"""Define the Build class."""

import os
import subprocess
import sys
import traceback
import venv

from typing import List

__all__ = []


########################################################################################################################

USAGE = f"""
build.py <sub-command> <options>*

    This script will perform various activities related to building this
    package and managing tests, development servers, etc.  It provides the
    follow sub-commands:

        clean : remove all generated artifacts from this repository

            --nuke : also remove all the development tools and libraries (will
                require `init` to be run again)

        edit : execute $EDITOR from the context of this packages's Python venv

        mobgen : generate files which control how mobs spawn

            --target <path> : the path into which the file should be generated
            --stdin <path> : the input file for issuing commands to the server
            --watch : (optional) watch the source files and regenerate the
                config file if anything changes

        oregen : generate files which control how ores are placed in the world

            --target <path> : the path into which the file should be generated
            --stdin <path> : the input file for issuing commands to the server
            --watch : (optional) watch the source files and regenerate the
                config file if anything changes

        init : initialize the virtual environment for this package in the
            ./usr directory. This includes making a copy of Python, Pip,
            and installing any dependencies specified in requirements.txt.
            It allows the following options:

        lint : run the linters set up for this project across all files

        python : execute a Python REPL in the context of this package's Python
            venv

        test : execute all automated tests for this package

            --only <app> : only run tests for the specified app. Must be either
                "api", or one of the websites
            --watch : watch for changes to source files, and re-run tests each
                time they change

        verify : check that all prerequisites for committing code have been
            met (linters, tests, etc.)


    In addition, the following options may be provided no matter for all
    subcommands:

        --verbose/-v : Print a full trace of all the shell commands and
            their output

"""


########################################################################################################################

class Build(object):
    """Build is the basis for classes which know how to perform common build operations for a Python package."""

    def __init__(self, argv: List[str]):
        """
        Create a new builder.

        Arguments:
            argv: a list of str objects giving the command line arguments passed to the build script

        """
        self.argv = argv
        self.clean = False
        self.help_requested = False
        self.nuke = False
        self.stdin_path = None
        self.subcommand = None
        self.subcommand_name = None
        self.target_dir = None
        self.watch = False

    # Properties ###################################################################################

    @property
    def activate(self) -> str:
        """Get the path to the command to activate this package's virtual environment."""
        return os.path.join(self.bin_dir, "activate")

    @property
    def bin_dir(self) -> str:
        """Get the path where executables in this package's virtual environment live."""
        return os.path.join(self.venv_dir, "bin")

    @property
    def git_branch(self) -> str:
        """Get the currently checked-out branch in git."""
        return self.read_shell(r"git branch | grep '^\*' | cut -f2 -d' '")

    @property
    def git_hash(self) -> str:
        """Get the most recently committed git hash."""
        return self.read_shell("git log --oneline -n1 | cut -f1 -d' '")

    @property
    def is_git_clean(self) -> bool:
        """Get whether there are any uncommitted changes in the current repository."""
        return self.shell("git status | grep 'working tree clean' -q")

    @property
    def mamba(self) -> str:
        """Get the mamba executable inside this package's virtual environment."""
        return os.path.join(self.bin_dir, "mamba")

    @property
    def package_name(self) -> str:
        """Get the official name of this package."""
        return self.read_shell(r"""cat setup.py | grep name= | sed 's/.*"\(.*\)".*/\1/'""")

    @property
    def pip(self) -> str:
        """Get the pip executable inside this package's virtual environment."""
        return os.path.join(self.bin_dir, "pip")

    @property
    def python(self) -> str:
        """Get the python executable inside this package's virtual environment."""
        return os.path.join(self.bin_dir, "python")

    @property
    def project_root(self) -> str:
        """Get an absolute path to the root of this project's directory."""
        return os.path.realpath(os.curdir)

    @property
    def src_dir(self) -> str:
        """Get the directory containing this package's source files."""
        return os.path.join(self.project_root, "src")

    @property
    def usage(self) -> str:
        """Get the usage string for this builder."""
        return USAGE

    @property
    def venv_dir(self) -> str:
        """Get the directory containing the virtual environment for this package."""
        return os.path.join(self.project_root, "usr")

    # Public Methods ###############################################################################

    def parse_args(self):
        """Parse the argv property to deterime which subcommand and options to use."""
        args = self.argv[1:]
        self._extract_subcommand(args)
        self._consume_args(args)

    def run(self):
        """Execute the build as configured by the argv property set on this builder."""
        if sys.version_info < (3, 5):
            print(f"Python {sys.version} provided, but at least version 3.5 is required.")
            sys.exit(1)

        self.parse_args()
        if self.help_requested:
            self._abort(returncode=0)

        if not os.path.isdir(self.venv_dir) and self.subcommand_name != "init":
            self._abort("Please run `./build.py init` first in order to set up your environment.", show_usage=False)

        try:
            result = self.subcommand()
            print("Done.")
            return result
        except KeyboardInterrupt:
            print("\nCancelled.")
            return True

    def read_user(self, prompt: str) -> str:
        """Read a line of input from the user."""
        sys.stdout.write(f"{prompt}: ")
        sys.stdout.flush()
        return sys.stdin.readline().strip()

    def read_shell(self, script: str) -> str:
        """Read the output from a shell command."""
        result = subprocess.check_output(script, shell=True)
        result = result.decode("utf8").strip()
        return result

    def shell(self, script: str):
        """Execute a line of shell code."""
        print(f"> {script}")

        script = script.replace("'", "'\"'\"'")
        script = f"/usr/bin/env bash -c '{script}'"
        result = subprocess.run(script, shell=True)
        return result.returncode == 0

    # Command Functions ################################################################################################

    def command___help(self) -> bool:
        """Print the usage message for this package."""
        return self.command_help()

    def command_clean(self) -> bool:
        """Remove all generated artifacts from this repository."""
        print("Removing build artifacts...")
        self.shell(";".join(f"rm -rf {path} &>/dev/null" for path in [
            "deploy", "dist", "var"
        ]))
        if self.nuke:
            print("Removing dependencies...")
            self.shell(";".join(f"rm -rf {path} &>/dev/null" for path in [
                ".pip.lock", "node_modules", "package-lock.json", "usr"
            ]))
        return True

    def command_edit(self) -> bool:
        """Start VIM in the context of this package's Python virtual environment."""
        subprocess.run(f"source {self.activate} && $EDITOR", shell=True)
        return True

    def command_mobgen(self):
        """Generate the mob generation files."""
        if self.target_dir is None:
            self.target_dir = "ignore"

        if self.stdin_path is None:
            self.stdin_path = "ignore"

        if self.watch:
            self.shell(" ".join([
                f"source {self.activate} &&",
                f"{self.python} -m packconfig.watchers.watch_mobgen "
                f"{self.python} {self.src_dir} {self.target_dir} {self.stdin_path}",
            ]))
            return True
        else:
            print(f"Generating config file to {self.target_dir}...")
            self.shell(" && ".join([
                f"source {self.activate}",
                f"{self.python} -m packconfig.mobgen.main {self.target_dir} {self.stdin_path}",
            ]))

    def command_oregen(self):
        """Generate the website."""
        if self.target_dir is None:
            self.target_dir = "ignore"

        if self.stdin_path is None:
            self.stdin_path = "ignore"

        if self.watch:
            self.shell(" ".join([
                f"source {self.activate} &&",
                f"{self.python} -m packconfig.watchers.watch_oregen "
                f"{self.python} {self.src_dir} {self.target_dir} {self.stdin_path}",
            ]))
            return True
        else:
            print(f"Generating config file to {self.target_dir}...")
            self.shell(" && ".join([
                f"source {self.activate}",
                f"{self.python} -m packconfig.oregen.main {self.target_dir} {self.stdin_path}",
            ]))

    def command_help(self, topic: str = None) -> bool:
        """Print the usage message for this package."""
        print(f"{self.usage}\n")
        return True

    def command_init(self) -> bool:
        """Download any dependencies for this package and perform other set-up functions."""
        if self.clean:
            print("Removing old dependencies...")
            self.shell(f"rm -rf ./node_modules &>/dev/null")
            self.shell(f"rm -rf ./usr &>/dev/null")

        print("Installing Git Hooks...")
        self.shell(f"cd .git/hooks; ls ../../src/hooks | while read HOOK; do ln -sf ../../src/hooks/$HOOK $HOOK; done")

        print("Creating Python virtual environment...")
        builder = venv.EnvBuilder(symlinks=False, with_pip=True)
        builder.create(self.venv_dir)

        print("Installing Python dependencies...")
        self.shell(f"{self.pip} install --upgrade pip")
        self.shell(f"{self.pip} install -r {self.project_root}/requirements.txt")
        self.shell(f"{self.pip} freeze | grep -v '^-e' > {self.project_root}/.pip.lock")
        self.shell(f"rm -rf {self.venv_dir}/lib/python*/site-packages/mccabe*")

        return True

    def command_lint(self) -> bool:
        """Run a full sweep with all linters."""
        print("Executing linters...")
        return (
            self.shell(f"{self.bin_dir}/pycodestyle src") and
            self.shell(f"{self.bin_dir}/pydocstyle src") and
            self.shell(f"{self.bin_dir}/pyflakes src") and
            True
        )

    def command_python(self) -> bool:
        """Execute a Python REPL in the context of this package's virtual environment."""
        if self.environment is None:
            self.environment = "development"

        subprocess.run(" && ".join([
            f"source {self.activate}",
            f"source {self.env_file}",
            f"{self.python} -i {self.src_dir}/packconfig/console.py",
        ]), shell=True)
        return True

    def command_test(self) -> bool:
        """Execute the automated tests associated with this package."""
        self.environment = "test"

        setup = f"source {self.activate}"
        command = f"{self.mamba} run src"
        if self.watch:
            command = f"{self.python} -m packconfig.watchers.watch_test {self.mamba} {self.src_dir}"

        print("Executing tests...")
        return self.shell(f"{setup} && {command}")

    def command_verify(self):
        """Execute all pre-commit checks set up for this package."""
        success = (
            self.command_lint() and
            self.command_test()
        )
        if not success:
            print("\nVerification failed.")

        return success

    # Private Methods ##############################################################################

    def _abort(self, message: str = None, returncode: int = 1, show_usage: bool = True):
        abort_text = []
        if show_usage:
            abort_text.append(self.usage)

        if message is not None:
            if len(abort_text) > 0:
                abort_text.append("\n")
            abort_text.append(message)

        abort_text.append("\n")

        print("".join(abort_text))
        sys.exit(returncode)

    def _consume_args(self, args: List[str]):  # noqa: C901
        while len(args) > 0:
            arg = args.pop(0)

            if arg == "--":
                while len(args) > 0:
                    self.passthrough_args.append(args.pop(0))
                self.api = True
            elif arg == "--clean":
                self.clean = True
            elif arg == "--help":
                self.help_requested = True
            elif arg == "--nuke":
                self.nuke = True
            elif arg == "--stdin":
                self.stdin_path = args.pop(0)
            elif arg == "--target":
                self.target_dir = args.pop(0)
            elif arg in ["--verbose", "-v"]:
                self.verbose = True
            elif arg == "--watch":
                self.watch = True
            else:
                self._abort(f"Unexpected option: {arg}")

    def _extract_subcommand(self, args: List[str]):
        if len(args) == 0:
            self._abort("Please provide a subcommand.")

        self.subcommand_name = args.pop(0).replace("-", "_")
        if not hasattr(self, f"command_{self.subcommand_name}"):
            self._abort(f"Unknown subcommand: {self.subcommand_name}")

        self.subcommand = getattr(self, f"command_{self.subcommand_name}")
        if not callable(self.subcommand):
            self._abort(f"Unknown subcommand: {self.subcommand_name}")


# Startup Script #######################################################################################################

if __name__ == "__main__":
    try:
        if not Build(sys.argv).run():
            print()
            sys.exit(1)
    except Exception:
        traceback.print_exc()
        print()
        sys.exit(2)

    print()
    sys.exit(0)
