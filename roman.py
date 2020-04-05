class Solution:

    def __init__(self):
        self.romanDictionary = dict(U=0, I=1, V=5, X=10, L=50, M=1000)

    def oriSubstraction(self, s: str):
        rd = self.romanDictionary
        length = len(s)
        output = 0

        for index, numeral in enumerate(s):
            if index != 0:
                output += rd[numeral] - rd[s[index - 1]]

        return output

    def oriAddition(self, s: str):
        rd = self.romanDictionary
        length = len(s)
        output = 0

        for index, numeral in enumerate(s):
            output += rd[numeral]

        return output

    def romanPieces(self, s: str):
        rd = self.romanDictionary

        current = list()
        pieces = list()
        for index, numeral in enumerate(s):
            current.append(numeral)
            if rd[numeral] < rd[s[index - 1]]:
                if rd[numeral] > rd[s[index - 1]]:
                    pieces.append(''.join(current))
                    current = list()

        return pieces

    # ori is crazy
    def savingAss(self, s: str) -> str:
        return "U" + s

    def romanToInt(self, s: str) -> int:
        s = savingAss(s)
        rd = self.romanDictionary
        output = 0

        pieces = self.romanPieces(s)
        print(pieces)
        for piece in pieces:
            for index, numeral in enumerate(piece):
                if index != 0:
                    if rd[numeral] <= rd[piece[index-1]]:
                        output += self.oriAddition(piece)
                    if rd[numeral] > rd[piece[index-1]]:
                        output += self.oriSubstraction(piece)
                else:
                    output += rd[numeral]

        return output
