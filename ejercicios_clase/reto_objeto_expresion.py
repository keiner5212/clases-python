class Expresion:
    def __init__(self, coeficiente, parteLiteral):
        self.coeficiente = coeficiente
        self.parteLiteral = parteLiteral

    def __add__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coeficiente+other.coeficiente), self.parteLiteral))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coeficiente+other.coeficiente), ""))
        return f"{self.coeficiente}{self.parteLiteral} + {other.coeficiente}{other.parteLiteral}"

    def __sub__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coeficiente-other.coeficiente), self.parteLiteral))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coeficiente-other.coeficiente), ""))
        return f"{self.coeficiente}{self.parteLiteral} - {other.coeficiente}{other.parteLiteral}"

    def __mul__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                return str(Expresion((self.coeficiente*other.coeficiente), self.__changeExponent(self.parteLiteral, 2*self.__getExponent())))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion((self.coeficiente*other.coeficiente), ""))
        elif (self.parteLiteral != other.parteLiteral):
            return str(Expresion((self.coeficiente*other.coeficiente), f"{other.parteLiteral}"))
        return f"{self.coeficiente}{self.parteLiteral} * {other.coeficiente}{other.parteLiteral}"

    def __truediv__(self, other):
        if (self.parteLiteral != ""):
            if (self.parteLiteral == other.parteLiteral):
                if (self.__getExponent() == 1):
                    return str(Expresion(round(self.coeficiente/other.coeficiente, 2), ""))
                return str(Expresion(round(self.coeficiente/other.coeficiente, 2), self.__changeExponent(self.parteLiteral, self.__getExponent()/2)))
        elif (self.parteLiteral == other.parteLiteral):
            return str(Expresion(round(self.coeficiente/other.coeficiente, 2), ""))
        return f"{self.coeficiente}{self.parteLiteral} / {other.coeficiente}{other.parteLiteral}"

    def __pow__(self, other):
        if (self.parteLiteral != ""):
            return f"{self.coeficiente}{self.parteLiteral} ** {other.coeficiente}{other.parteLiteral}"
        return str(Expresion((self.coeficiente**other.coeficiente), ""))

    def __str__(self):
        return f"{self.coeficiente}{self.parteLiteral}"

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
