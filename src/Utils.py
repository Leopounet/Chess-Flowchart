import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.Tags import Tags

##################################################################################################
################################## VARIABLES #####################################################
##################################################################################################

##################################################################################################
################################## METHODS #######################################################
##################################################################################################

def is_letter(c):
    """
    Checks if the given character is a letter.

    :param c: The character to test.

    :return: True if the character is a letter, False otherwise.
    """
    return 'A' <= c  <= 'Z' or 'a' <= c <= 'z'

def is_number(c):
    """
    Checks if the given character is a number.

    :param c: The character to check.

    :return: True if the character is a number, False otherwise.
    """
    return '0' <= c <= '9'

def get_nametag(nametag):
    """
    Checks if the given nametag is valid, that it only contains letters, numbers,
    dashes, underscores and apostrophes. It must also start with the given tags in `Tags.py <Tags.py>`.
    And returns the nametag if it is valid.

    :param nametag: The nametag to check (string).

    :return: The nametag if the nametag is valid, None otherwise.
    """
    # start must be valid
    if not nametag.startswith(Tags.NAMETAG_START.value):
        return None

    # removes the start of the tag
    nametag = nametag[len(Tags.NAMETAG_START.value):]

    # end must be valid
    if not nametag.endswith(Tags.NAMETAG_END.value):
        return None

    # removes the end of the tag
    nametag = nametag[:(len(nametag) - len(Tags.NAMETAG_END.value))]

    # no empty nametags
    if nametag == "":
        return None

    # checks that every single character is valid
    for c in nametag:
        if (not is_letter(c) and
            not is_number(c) and
            c != "-" and c != "_" and c != "'"):
            return None
    return nametag

def is_nametag_reachable(nametag, branches):
    """
    Checks whether the given nametag is reachable by another branch or not. This means that the given
    nametag must appear in at least one branch as an end tag.

    :param nametag: The nametag to check the accessibility of.

    :param branches: The list of branches.

    :return: True if the nametag is reachable, False otherwise.
    """
    for branch in branches:
        for next_nametag in branches[branch].next_nametags:
            if next_nametag == nametag:
                return True
    return False

def branch_exists(nametag, branches):
    """
    Checks whether the given nametag is indeed labelling a branch.

    :param nametag: The nametag to check the accessibility of.

    :param branches: The list of branches.

    :return: True if the nametag exists, False otherwise.
    """
    for branch in branches:
        if branches[branch].name == nametag:
            return True
    return False

def valid_branches(branches):
    """
    Checks that the given branches are valid (every single branch is supposed valid). The idea here is to make
    sure that every ending nametag leads to another branch and that every branch is reachable.

    Note: This does not exactly gurantess that the branches are absolutely valid (for instance there could be 
    some hidden recursion or multiple disconnected subgraphs). But this would be a bit more difficult to check (not
    impossible), let's just assume this will be used correctly.

    :param branches: The list of branches to check.

    :return: True if the branches are valid, False otherwise.
    """

    # for every branch in the list
    for branch in branches:

        # make sure it is either reachable or has the special tag "start"
        if branches[branch].name != "start" and not is_nametag_reachable(branches[branch].name, branches):
            return False

        # make sure all ending tags refer to existing branches
        for nametag in branches[branch].next_nametags:
            if not branch_exists(nametag, branches):
                return False

    return True




