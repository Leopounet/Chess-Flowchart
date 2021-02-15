import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.StringReader import StringReader

import src.Utils as Utils

# print(Utils.is_valid_nametag(sys.argv[1]))

branches = [
    "$(start) e2-e4 e7-e5 Ng1-Ng3 Nb8-Nc6 Bf1-Bc4 Ng8-Nf6 d2-d4 $(Nf6xe4)",
    "$(Nf6xe4) Nf6xe4 e4xe5 Bf8-Bc5 Qd1-Qd5 !W"
]

branch_dict = StringReader.read_strings(branches)

print(Utils.valid_branches(branch_dict))

for branch in branch_dict:
    print("********************************************************")
    print(branch_dict[branch])
    print("********************************************************")