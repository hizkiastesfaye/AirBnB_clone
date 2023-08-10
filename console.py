"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):

    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    # def do_emptyline(self,line):
    #     '''do nothig just pass'''
    #     pass

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''EOF signal to exit the program.\n'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
