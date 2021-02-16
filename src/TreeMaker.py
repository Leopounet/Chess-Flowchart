import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.GraphType import GraphType
from src.Color import DotColor
from src.Tags import Tags
import src.Utils as Utils

class TreeMaker:

    """
    This class encapsulates methods used to draw tress represented by a list of branches.
    So far, it only generates a file with the dot format, but it could be extended to other 
    formats as well.
    """

    # type of graph to use (digraph by default)
    graph_type = GraphType.DIGRAPH

    # transition type
    tr_type = ""

    # default tabulation size
    tab_size = "    "

    # start keyword to use
    start_keyword = "start"

    # name of a node (here, nodes will be named q0, q1, q2...) this is only used in the dot file
    # this will not affect how the tree eventually looks
    node_name = "q"

    # current node index in the tree, it has to be resetted each time a new tree is getting generated
    node_index = 0

    def __init__(self):
        pass

    @classmethod
    def draw_node(self, index, name, color, label_color):
        """
        Generates a node with a given name.

        :param index: The current ID of this node.

        :param name: The name to give to this node.

        :param color: Color to fill the node with.

        :return: A string corresponding to the node.
        """
        node = self.node_name + str(index) + "[label = \"" + name + "\", "
        node += "style = \"filled\", fillcolor = \"" + color + "\", "
        node += "fontcolor = \"" + label_color + "\""
        node += "]"
        return node

    @classmethod
    def draw_transition(self, l_index, r_index):
        """
        Generates a transition from the node with index l_index to the node with index r_index.

        :param l_index: Source node.

        :param r_index: Target node.

        :return: A string corresponding to the transition.
        """
        transition = ""
        transition += self.node_name + str(l_index) + " " 
        transition += self.tr_type + " " 
        transition += self.node_name + str(r_index)
        return transition

    @classmethod
    def tag_to_color(self, tag):
        """
        Converts a tag to a dot color.

        :param tag: The tag to convert.

        :return: A string correspoding to the color bound to this tag.
        """

        # white advantage
        if tag == Tags.WHITE_ADV:
            return DotColor.GREEN

        # black advantage
        if tag == Tags.BLACK_ADV:
            return DotColor.RED

        # checkmate
        if tag == Tags.CHECKMATE:
            return DotColor.LIGHT_GRAY
        
        # equivalent situation
        if tag == Tags.EQUIVALENT:
            return DotColor.LIGHT_BLUE

        return DotColor.WHITE
    
    @classmethod
    def _generate_branches(self, current_branch_name, branches, file, previous_index=0, white_turn=True):
        """
        Helper method to generate the branches.

        :param start_branch_name: The name of the current branch to draw.

        :param branches: The dictionnary of branches to use to generate the tree.

        :param file: The file to write in.

        :param previous_index: The index of the previous node, use to draw the arrow between two branches.

        :param turn: If turn is True, then it's whites' turn, otherwise it's blacks' turn.

        :return: True if everything could be generated, False otherwise.
        """

        # checking that the current branch is valid
        if not current_branch_name in branches:
            print("The branch " + current_branch_name + " does not exist.")
            return False

        # get the branch object
        branch = branches[current_branch_name]

        # true if this is the first node of the branch
        first_node = True

        # draw all the moves of this branch
        for move in branch.moves:

            # compute the fill color and the label color depending on whose turn it is
            bg_color = DotColor.WHITE if white_turn else DotColor.BLACK
            label_color = DotColor.WHITE if not white_turn else DotColor.BLACK

            # draw the current node
            file.write(self.tab_size + TreeMaker.draw_node(self.node_index, move, bg_color.value, label_color.value) + ";\n")

            # if this is the first node being drawn of the branch (but not of the tree), draw an arrow with
            # the previous node
            if previous_index != 0 and first_node:
                file.write(self.tab_size + TreeMaker.draw_transition(previous_index, self.node_index) + ";\n")

            # otherwise, draw an arrow with the previous node index as expected
            # except if the current index is 0
            elif self.node_index != 0:
                file.write(self.tab_size + TreeMaker.draw_transition(self.node_index - 1, self.node_index) + ";\n")

            # increase the node index each time
            self.node_index += 1

            # not the first node anymore
            first_node = False

            # change whose turn it is
            white_turn = not white_turn

        # if the this branch is done and does get divided
        if not branch.is_divided():

            # get the color corresponding to the ending tag
            color = TreeMaker.tag_to_color(branch.ending_tag).value

            # change the color of the last node accordingly
            file.write(self.tab_size + TreeMaker.draw_node(self.node_index - 1, move, color, DotColor.BLACK.value) + ";\n")

        # else if it does get divided
        else:

            # set the index to draw an arrow to
            previous_index = self.node_index - 1

            # recursive calls
            for next_branch_name in branch.next_nametags:
                if not TreeMaker._generate_branches(next_branch_name, branches, file, 
                                                    previous_index=previous_index, white_turn=white_turn):
                    return False
        return True

    @classmethod
    def generate_dot_flowchart(self, branches, filename):
        """
        Generates a dot file that represents a tree corresponding to the given branches (if possible).

        :param branches: The dictionnary of branches to use to generate the tree.

        :param filename: The name of the file to save the code in.

        :return: True if the drawing was successful, False otherwise.
        """

        if not Utils.valid_branches(branches):
            print("Branches are invalid.")
            return False

        if not self.start_keyword in branches:
            print("No branch named " + self.start_keyword + ", there should exist one as a starting point.")
            return False

        # opening the file to write into
        with open(filename, "w") as file:
            
            # set the type of graph this is
            file.write(self.graph_type.value[0] + "\n")

            # ste the transition type (depends on the type of graph)
            self.tr_type = self.graph_type.value[1]

            # init the node index
            self.node_index = 0

            # starts generating the tree
            if not TreeMaker._generate_branches(self.start_keyword, branches, file):
                return False

            # close the graph
            file.write("}")
        return True
