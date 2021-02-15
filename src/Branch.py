import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

if sys.platform == "linux" or sys.platform == "linux2":
    from src.Color import LinuxColors as Color
else:
    from src.Color import OtherColors as Color

class Branch:

    """
    This class is used to describe a branch.

    :ivar moves: The list of all moves in the branch (ordered).

    :ivar name: The name of the branch.

    :ivar ending_tag: The ending tag of the branch, if the branch does get divided.

    :ivar next_nametags: The next nametags if this branch gets divided.
    """

    def __init__(self, name):
        """
        Creates a new branch object.
        """
        
        # the list of moves (in order)
        self.moves = []

        # the name of this branch
        self.name = name

        # the ending tag, if it exists
        self.ending_tag = None

        # the next nametags if they exist
        self.next_nametags = []

    def add_move(self, move):
        """
        Adds a move to the list of moves.

        :param move: The move to add.
        """
        self.moves.append(move)

    def set_ending_tag(self, tag):
        """
        Sets the ending tag (by definition next_nametags must then be empty but this is not checked).

        :param tag: The ending tag.
        """
        self.ending_tag = tag

    def add_next_nametag(self, nametag):
        """
        Adds a new 'next nametag' for this branch (by definition ending_tag must then be None but this is not checked).

        :param nametag: The nametag to add.
        """
        self.next_nametags.append(nametag)

    def is_divided(self):
        """
        Checks if this branch gets divided (multiple outcomes possible at the end of the branch).

        :return: True if the branch gets divided, False otherwise. It returns None if the Branch is invalid.
        """
        if self.next_nametags == [] and self.ending_tag != None:
            return False

        if self.next_nametags != [] and self.ending_tag == None:
            return True
        
        return None

    def __str__(self):
        """
        To string method.

        :return: A string corresponding to the object.
        """

        string = Color.BLUE.value + "Branch name: " + Color.DEFAULT.value + self.name + "\n"
        string += Color.GREEN.value + "Has ending tag: " + Color.DEFAULT.value + ("Yes (" + self.ending_tag.value + ")" 
                                                                                  if self.ending_tag != None else "No") + "\n"
        string += Color.ORANGE.value + "Gets divided: " + Color.DEFAULT.value + ("Yes" 
                                                                                 if self.next_nametags != [] else "No") + "\n"

        if self.next_nametags != []:
            string += "\nList of divisions: \n"
        i = 0
        for tag in self.next_nametags:
            string += Color.MAGENTA.value + "- Division " + str(i) + Color.DEFAULT.value + ": " + tag + "\n"
            i += 1

        string += "\nList of moves: \n"
        i = 0
        for m in self.moves:
            string += Color.MAGENTA.value + "- Move " + str(i) + Color.DEFAULT.value + ": " + m

            if i != len(self.moves) - 1:
                string += "\n"
            i += 1

        return string

