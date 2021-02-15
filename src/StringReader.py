import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.Tags import Tags
from src.Branch import Branch
import src.Utils as Utils

"""
This class reads a string and converts it to a tree.
"""

class StringReader:

    """
    This class is used to convert string to trees.

    Expected format of a given string:

    $(tag) move move move $(tag1) $(tag2)

    Here, 'move' represents a move in chess (doesn't have to be valid though, could be checked).
    $(tag) is just a name for this specific branch.
    $(tag1/2) are the names of the two following branch, meaning that after the last 'move', we can either
    end up in the situation described by $(tag1) or $(tag2).

    Special characters:

    $(tag) move move #

    The # means that the branch is done and that it ends in a checkmate (the last player doing a move won).

    $(tag) move move !W

    The !W tag means that the branch is done and that at this point the Whites have a serious advantage. There also
    exists the !B tag when the Blacks are in the lead.

    $(tag) move move =

    The = tag means that the branch is done and that both players are in equivalent positions.
    """

    @classmethod
    def read_branch(self, branch):
        """
        Given a branch (a string describing one specific branch of the flow), returns the corresponding Branch
        object.

        A branch is valid if it starts with a valid tag (basically letters/numbers/apostrophes/underscore/dashes).

        :param branch: The branch to read.

        :return: A new Branch object corresponding to the given branch if the branch is valid, Nine otherwise.
        """

        # separates the branch according to the spaces
        branch = branch.split(" ")

        # checks that the first element is a valid nametag (and gets it)
        nametag = Utils.get_nametag(branch[0])

        # if there are no starting nametags, this is illegal
        if nametag == None:
            return None

        # creates a new branch object
        branch_obj = Branch(nametag)
        
        # removes the first nametag
        branch = branch[1:]

        # checks that the following elements do not contain special characters (except the last one)
        # it does allow for special characters $() if all the last elements contain these special character
        # (and only those!)

        # True if nametags have been found previously
        only_name_tags = False

        # the index of the current element of the branch
        index = 0

        # flag to make sure the last element is a tag
        last_is_tag = False

        # parse all the elements in the branch
        for b in branch:

            # converts the current element to a nametag if possible
            nametag = Utils.get_nametag(b)

            # if a nametag has previously been found but this element is not a nametag, abort
            if only_name_tags and nametag == None:
                return None

            # if a nametag has been found set the flag to True, after this element, only nametags can be found
            if nametag:
                only_name_tags = True
                last_is_tag = True
                branch_obj.add_next_nametag(nametag)
                continue

            # flag to make sure there always is only one tag per element
            found_tag = False

            # parse all the possible tags
            for tag in Tags:

                # if incomplete nametags are found, it's illegal
                if tag == Tags.NAMETAG_START and tag.value in b:
                    return None

                # if incomplete nametags are found, it's illegal
                if tag == Tags.NAMETAG_END and tag.value in b:
                    return None

                # if a tag has been found and it is not the last element of the branch, this is illegal
                if tag.value in b and index != len(branch) - 1:
                    return None

                # there can not be multiple tags within the same element
                if tag.value in b and found_tag:
                    return None

                # if a tag has been found, set the flag
                if tag.value in b:
                    last_is_tag = True
                    found_tag = True
                    branch_obj.set_ending_tag(tag)

            # if no tag has been found, this is a move
            if not found_tag:
                branch_obj.add_move(b)

            index += 1

        # if the last element was not a tag, this is a illegal
        if not last_is_tag:
            return None

        return branch_obj


    @classmethod
    def read_strings(self, strings):
        """
        Converts the given strings into a dictionnary of branches according to the method described above.

        :param strings: The string to convert.

        :return: A dictionnary of branches if the strings are valid, None otherwise.
        """
        branches = {}
        for s in strings:
            branch = StringReader.read_branch(s)
            if branch == None:
                return None
            branches[branch.name] = branch
        return branches