from argparse import ArgumentParser
from os import system
from os.path import expanduser
from typing import NoReturn

from main import main
from demo import demo
from src.sutils.update import update
from src.misc.signs import Signs


def program_options() -> None | NoReturn:
    """This is an example use of the algorithm via cli program."""

    description: str = (
            "This is a program designed to interact with"
            " face recognition algorithm Capstone Group 5."
        )
    parser: object = ArgumentParser(
            prog="EasyWiz",
            usage="EasyWiz [OPTIONS]",
            description=description
        )

    # all of the functions listed below prompts for the local or
    # temporary password email to the user using python's stdlib smtplib
    # and ssl, this requires internet connection, else the user need to
    # the password they received during the setup.

    # start/use the system
    parser.add_argument(
        "--use", "--use",
        help="Use the system.",
        action="store_true"
    )
    # update the database by calling the fetch database function from src.function
    parser.add_argument(
        "--update", "--update",
        help="Update the system",
        action="store_true"
    )
    # (re)setup the user
    parser.add_argument(
        "--setup", "--setup",
        help=(
                "Setup the user (prompts to input the "
                "passphrase sent via email, if used again)."
            ),
        action="store_true"
    )
    # destroy the system, can be used in case of intruder breach
    parser.add_argument(
        "--destroy", "--destroy",
        help="Destroy the user database.",
        action="store_true"
    )
    parser.add_argument(
        "--demo", "--demo",
        help="Face recognition demonstration.",
        action="store_true"
    )

    args = parser.parse_args()

    try:
        if args.use:
            main(expanduser("~"))
        elif args.update:
            update()
        elif args.setup:
            print(f"{Signs.PROC} Setting up the program ...")
            system("./$HOME/.easywiz/system/setup.sh")
        elif args.destroy:
            print(f"{Signs.PROC} Removing the program ...")
            system("rm -rf $HOME/.easywiz")
        elif args.demo:
            demo()
    except (
            ConnectionError,
            KeyboardInterrupt,
            SystemError
        ) as Err:
        raise SystemExit(f"{Signs.FAIL} {Err}, aborting ...")


if __name__ == "__main__":
    program_options()
