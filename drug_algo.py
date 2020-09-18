mockContraindications = [
    ["nr913ng", "blue123"],
    ["red123", "87f2h139049f"],
    ["nr913ng", "j1j81f0"],
    ["blue123", "weed1337"],
    ["red123", "weed1337"]
]

# d = druglib[0] -> d[-1]
Druglib = [
    # cn , cn ...cn  , rxid
    ["Blue pill", "bp", "blue123"],
    ["Red pill", "red123"],
    ["Medicinal Weed", "weed1337"]
]

class Drugs:
    def __init__(self, con, druglib):
        self.contradiction = {}
        for pair in con:
            if pair[0] in self.contradiction.keys():
                self.contradiction[pair[0]].append(pair[1])
            else:
                self.contradiction[pair[0]] = [pair[1]]

            if pair[1] in self.contradiction.keys():
                self.contradiction[pair[1]].append(pair[0])
            else:
                self.contradiction[pair[1]] = [pair[0]]

        self.drugs = {}
        for d in druglib:
            if d[-1] in self.drugs.keys():
                continue
            else:
                self.drugs[d.pop(-1)] = d

        print(self.contradiction)
        print(self.drugs)

    def patient_dcheck_byid(self, rxNorm):

        if rxNorm in self.contradiction.keys():
            return self.contradiction[rxNorm]

    def patient_dcheck_byname(self, drugName):
        pass


def main():
    x = Drugs(mockContraindications, Druglib)

    input = [["Blue pill","blue123"],["Red pill", "red123"],["Medicinal Weed","weed1337"]]

    medlist = set()
    for m in input:
        medlist.add(m[1])

    for i in input:
        print()
        print("Drug name : {}".format(i[0]))
        result = x.patient_dcheck_byid(i[-1])
        if result is None:
            print("None")
        else:
            print("contradictions:")
            for r in result:
                if r in medlist:
                    print("{} ".format(r))


# test
#
main()
