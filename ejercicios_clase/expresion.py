class Expresion:
    def __init__(self, coheficiente, parteLiteral):
        self.coheficiente = coheficiente
        self.parteLiteral = parteLiteral

    def __add__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coheficiente+other.coheficiente), self.parteLiteral))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coheficiente+other.coheficiente), ""))
        return f"{self.coheficiente}{self.parteLiteral} + {other.coheficiente}{other.parteLiteral}"

    def __sub__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coheficiente-other.coheficiente), self.parteLiteral))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coheficiente-other.coheficiente), ""))
        return f"{self.coheficiente}{self.parteLiteral} - {other.coheficiente}{other.parteLiteral}"

    def __mul__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coheficiente*other.coheficiente), self.__changeExponent(self.parteLiteral, 2*self.__getExponent())))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coheficiente*other.coheficiente), ""))
        elif (self.parteLiteral != other.parteLiteral):
            return str(Expresion((self.coheficiente*other.coheficiente), f"{other.parteLiteral}"))
        return f"{self.coheficiente}{self.parteLiteral} * {other.coheficiente}{other.parteLiteral}"

    def __truediv__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                if (self.__getExponent() == 1):
                    return str(Expresion(round(self.coheficiente/other.coheficiente, 2), ""))
                return str(Expresion(round(self.coheficiente/other.coheficiente, 2), self.__changeExponent(self.parteLiteral, self.__getExponent()/2)))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion(round(self.coheficiente/other.coheficiente, 2), ""))
        return f"{self.coheficiente}{self.parteLiteral} / {other.coheficiente}{other.parteLiteral}"

    def __pow__(self, other):
        if (self.parteLiteral != ""):
            return f"{self.coheficiente}{self.parteLiteral} ** {other.coheficiente}{other.parteLiteral}"
        return str(Expresion((self.coheficiente**other.coheficiente), ""))

    def __str__(self):
        return f"{self.coheficiente}{self.parteLiteral}"

    def __getExponent(self):
        res = ""
        startGet = False
        for item in self.parteLiteral:
            if startGet:
                res += item
            elif (item == "^"):
                startGet = True
        if (res == ""):
            return 1
        return float(res)

    def __changeExponent(self, parteLiteral, exponente):
        if ("^" in parteLiteral):
            if (exponente == 1):
                return parteLiteral[0:parteLiteral.index("^")]
            return parteLiteral[0:parteLiteral.index("^")]+f"^{exponente}"
        else:
            return parteLiteral+f"^{exponente}"
