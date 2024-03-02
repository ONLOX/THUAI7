import PyAPI.structures as THUAI7
import platform
import argparse
from typing import List, Callable
from PyAPI.logic import Logic
from PyAPI.AI import AI
from PyAPI.Interface import IAI
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/proto")


def PrintWelcomeString() -> None:
    # Generated by http://www.network-science.de/ascii/ with font "standard"
    welcomeString = r'''

            _____ _   _ _   _   _    ___ _____
           |_   _| | | | | | | / \  |_ _|___  |
             | | | |_| | | | |/ _ \  | |   / /
             | | |  _  | |_| / ___ \ | |  / /
             |_| |_| |_|\___/_/   \_\___|/_/

        ____               _             _            ____ _      _     _
       / ___|_ __ __ _  __| |_   _  __ _| |_ ___     / ___(_)_ __| |___| |
      | |  _| '__/ _` |/ _` | | | |/ _` | __/ _ \   | |  _| | '__| / __| |
      | |_| | | | (_| | (_| | |_| | (_| | ||  __/_  | |_| | | |  | \__ \_|
       \____|_|  \__,_|\__,_|\__,_|\__,_|\__\___( )  \____|_|_|  |_|___(_)


    '''
    print(welcomeString)


def THUAI7Main(argv: List[str], AIBuilder: Callable) -> None:
    pID: int = 0
    sIP: str = "127.0.0.1"
    sPort: str = "8888"
    file: bool = True
    screen: bool = True
    warnOnly: bool = False
    parser = argparse.ArgumentParser(
        description="THUAI7 Python Interface Commandline Parameter Introduction"
    )
    parser.add_argument(
        "-I",
        type=str,
        required=True,
        help="Server`s IP 127.0.0.1 in default",
        dest="sIP",
        default="127.0.0.1",
    )
    parser.add_argument(
        "-P",
        type=str,
        required=True,
        help="Server`s Port 8888 in default",
        dest="sPort",
        default="8888",
    )
    parser.add_argument(
        "-p",
        type=int,
        required=True,
        help="Player`s ID",
        dest="pID",
        choices=[0, 1, 2, 3, 4],
    )
    parser.add_argument(
        "-d",
        action="store_true",
        help="Set this flag to save the debug log to ./logs folder",
        dest="file",
    )
    parser.add_argument(
        "-o",
        action="store_true",
        help="Set this flag to print the debug log to the screen",
        dest="screen",
    )
    parser.add_argument(
        "-w",
        action="store_true",
        help="Set this flag to only print warning on the screen",
        dest="warnOnly",
    )
    args = parser.parse_args()
    pID = args.pID
    sIP = args.sIP
    sPort = args.sPort
    file = args.file
    screen = args.screen
    warnOnly = args.warnOnly
    playerType = THUAI7.PlayerType(0)
    if pID == 4:
        playerType = THUAI7.PlayerType(1)
    else:
        playerType = THUAI7.PlayerType(2)

    if platform.system().lower() == "windows":
        PrintWelcomeString()

    logic = Logic(pID, playerType)
    logic.Main(AIBuilder, sIP, sPort, file, screen, warnOnly)


def CreateAI(pID: int) -> IAI:
    return AI(pID)


if __name__ == "__main__":
    THUAI7Main(sys.argv, CreateAI)
