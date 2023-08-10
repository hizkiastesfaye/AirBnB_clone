import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    # def do_emptyline(self,line):
    #     '''do nothig just pass'''
    #     pass

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program using keyboard'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
