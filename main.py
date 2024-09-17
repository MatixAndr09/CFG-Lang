
try:
    from rich import console
except ImportError:
    print("\033[0;31m[Core.Import.Error]\033[0m  Please install rich library by running: pip install rich")
    exit()

from packages.errors import err
import time
import sys

cmd = console.Console()

cmd.print("[blue bold][Core.main][/] [white]Initializing program...[/]")
time.sleep(0.5)
cmd.print("[blue bold][Core.main][/] [white]Initializing lexer[/]")
time.sleep(0.7)
cmd.print("[blue bold][Core.main][/] [white]Initializing parser[/]")
time.sleep(1)
cmd.print("[blue bold][Core.main][/] [white]Initializing interpreter...[/]")
time.sleep(2.5)
cmd.print("[blue bold][Core.main][/] [white]Done![/]")

if len(sys.argv) > 1:
    path = sys.argv[1]
    if path.endswith(".cfg"):
        pass
    else:
        err.InvalidFileType()
        exit()