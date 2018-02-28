class DPP:
    def __init__(self, alphabet, parents):
        self.alphabet = alphabet
        self.parents = parents
        self.resolutions = {}
    def resolveOver(self, parents, var):
        pos = []
        neg = []
        newparents = []
        for clause in parents:
            if var in clause:
                pos.append(set(filter(lambda x: x != var, clause)))
            elif "-" + var in clause:
                neg.append(set(filter(lambda x: x != "-" + var,clause)))
            else:
                newparents.append(clause)
        for pclause in pos:
            for nclause in neg:
                resolution = pclause.union(nclause)
                newparents.append(resolution)
        return newparents

    def keepClause(self, clause):
        for a in self.alphabet:
            if a in clause and "-" + a in clause:
                return False
        return True
    def dpp(self, alphabet, parents): #recursive so requires alphabet and parents parameters. These are not necessarily the same as self.alphabet, self.parents.
        if not parents:
            return True
        else:
            resolution = self.resolveOver(parents, alphabet[0])
            self.resolutions[alphabet[0]] = resolution
            if set() in resolution:
                return False
            else:
                return self.dpp(alphabet[1:], list(filter(lambda x: self.keepClause(x), resolution)))
    def resolve(self):
        outcome = self.dpp(self.alphabet, self.parents)
        if outcome:
            self.outcome = "Satisfiable"
        else: 
            self.outcome = "Not Satisfiable"
        return outcome
    def __str__(self):
        alphabet = "Alphabet: " + ",".join(self.alphabet) + "\n"
        parents = "Parents: " + ", ".join(list(map(lambda x: "[" + ",".join(list(x)) + "]", self.parents))) + "\n"
        ret = alphabet + parents
        if self.resolutions:
            resolutions = []
            for key, val in self.resolutions.items():
                resolutions.append("Resolving over {}: {}".format(key, ",".join(list(map(lambda x: "[" + ",".join(list(x)) + "]", val)))))
            ret = ret + "\n".join(resolutions) + "\n" + "Outcome of DPP: {}".format(self.outcome)
        return ret
