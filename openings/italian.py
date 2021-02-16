import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.StringReader import StringReader
from src.TreeMaker import TreeMaker
import src.Utils as Utils

# print(Utils.is_valid_nametag(sys.argv[1]))

if len(sys.argv) < 2:
    print("Usage: python3 <opening>.py <filename>")
    print("opening: The name of the opening you want to generate.")
    print("filename: The name of the file to save the flowchart in.")
    exit(0)

branches = [
    "$(start) e2-e4 e7-e5 Ng1-Ng3 Nb8-Nc6 Bf1-Bc4 Ng8-Nf6 d2-d4 $(1) $(2) $(3)",
    "$(1) Nf6xe4 e4xe5 Bf8-Bc5 Qd1-Qd5 !W",
    "$(2) Nc6xd4 Bc4xf7 Ke8xBf7 Nf3xe5 Kf7-Ke8 Qd1xd4 !W",

    "$(3) e5xd4 o-o Bf8-Bc5 e4-e5 $(4) $(5) $(8)",
    "$(4) Nf6-Ng4 Bc1-Bf4 o-o h2-h3 Ng4-Nh6 Bf4xBh6 g7xh6 !W",
    "$(5) Nf6-Ne4 Rf1-Re1 d7-d5 e.p. $(6) $(7)",

    "$(6) Bc8-Bf5 d6xc7 Qd8xQc7 Nb1-Nd2 !W",
    "$(7) f7-f5 d6xc7 Qd8xQc7 Nb1-Nd2 Bc5-Be7 Nd2xe4 f5xNe4 Re1xe4 !W",

    "$(8) d7-d5 e5xNf6 d5xBc4 Rf1-Re1 Bc8-Be6 Nf3-Ng5 $(9) $(10) $(11) $(12) $(15) $(18)",
    
    "$(9) Qd8xf6 Ng5xBe6 f7xNe6 Qd1-Qh5 !W",
    "$(10) g7xf6 Ng5xBe6 f7xNe6 Qd1-Qh5 !W",
    "$(11) Qd8-Qd7 Ng5xBe6 f7xNe6 Qd1-Qh5 !W",
    "$(12) Qd8-Qd6 Ng5-Ne4 $(13) $(14)",

    "$(13) Qd6-Qf8 f6xg7 Qf8xg7 Ne4xBc5 !W",
    "$(14) Qd6-Qd5 f6xg7 Rh8-R57 Ne4-Nf6 !W",

    "$(15) o-o f6-g7 $(16) $(17)",
    "$(16) Kg8xg7 Re1xBe6 f7xRe6 Ng5xe6 !W",
    "$(17) Rf8-Re8 Qd1-Qh5 Be6-Bf5 Qh5xf7 #",

    "$(18) Qd8-Qd5 Nb1-Nc3 $(19) $(20) $(23)",
    "$(19) d4xNc3 Qd1xQd5 !W",
    "$(20) Qd5-Qd6 Nd2-Ne4 $(21) $(22)",
    "$(21) Qd6-Qd5 f6xg7 Rh8-R57 Ne4-Nf6 !W",
    "$(22) Qd6-Qf8 f6xg7 Qf8xg7 Ne4xBc5 !W",

    "$(23) Qd5-Qf5 Nc3-Ne4 $(24) $(27)",
    "$(24) g7xf6 g2-g4 $(25) $(26)",
    "$(25) Qf5-Qg6 Nf5xBe6 f7xNe6 Ne4xBc5 !W",
    "$(26) Qf5-Qe5 Nf5-Nf3 Qe5-Qd5 Ne4-Nf6 !W",

    "$(27) o-o-o g2-g4 $(28) $(29)",
    "$(28) Qf5xg4 Qd1xQg4 Be6xQg4 Ng5xf7 !W",
    "$(29) Qf5-Qe5 $(30) $(33)",
    "$(30) Ng5-Nf3 Qe5-Qd5 f6xg7 Rh8-Rg8 Ne4-Nf6 $(31) $(32)",
    "$(31) Qd5-Qd6 Nf6-Ne4 =",
    "$(32) Nf6xRg8 Rd8xNg8 !B",
    "$(33) Ng5xBe6 ="
]

branch_dict = StringReader.read_strings(branches)

for branch in branch_dict:
    print("********************************************************")
    print(branch_dict[branch])
    print("********************************************************")

TreeMaker.generate_dot_flowchart(branch_dict, sys.argv[1])