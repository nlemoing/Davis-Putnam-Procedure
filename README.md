# Davis-Putnam-Procedure
Given an alphabet and a set of clauses, determines if the argument is satisfiable or not.

Sample Usage: The program below is an example to prove the disjunctive syllogism by negating the conclusion.

First argument: alphabet. A list of strings comprising the alphabet.

Second argument: clauses. A list of sets of strings representing the initial clauses for the system.


from dpp import DPP

DisjSyll = DPP(["A", "B"], [set(["A", "B"]), set(["-A"]), set(["-B"]))

print(DisjSyll) #prints alphabet, parents

DisjSyll.resolve() #returns true if the system is satisfiable, false if it is not

#resolve has a boolean argument indicating whether resolution steps should be stored. The default is True.

print(DisjSyll) #prints alphabet, parents, resolution steps, and outcome
