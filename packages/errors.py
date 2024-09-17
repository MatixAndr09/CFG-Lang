from rich import print


class Error:
    def __init__(self):
        pass

    def ImportNotFound(self):
        print("[red bold][Core.Error.ImportNotFound] - Import doesn't exist in available libraries.[/]")

    def LibraryNotFound(self):
        print(
            "[red bold][Core.Error.LibraryNotFound] - Library you tried to import is not mentioned in the config file.[/]")

    def VariableNotFound(self):
        print("[red bold][Core.Errors.VariableNotFound] - The variable you mentioned was not found in this scope.[/]")

    def FunctionNotFound(self):
        print("[red bold][Core.Errors.FunctionNotFound] - The function you mentioned was not found in this scope.[/]")

    def ClassNotFound(self):
        print("[red bold][Core.Errors.ClassNotFound] - The class you mentioned was not found in this scope.[/]")

    def MethodNotFound(self):
        print("[red bold][Core.Errors.MethodNotFound] - The method you mentioned doesn't exist.[/]")

    def InvalidSyntax(self):
        print("[red bold][Core.Errors.InvalidSyntax] - Synatx is invalid.[/]")

    def InvalidType(self):
        print("[red bold][Core.Errors.InvalidType] - The type of variable is correct[/]")

    def TypeNotExists(self):
        print("[red bold][Core.Errors.TypeNotExists] - The type you mentioned doesn't exist.[/]")

    def InvalidFileType(self):
        print("[red bold][Core.Errors.InvalidFileType] - The file you provided is not a .cfg file.[/]")


err = Error()