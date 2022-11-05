
class Imc:
    def __init__(self,peso, altura, sexo):
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo

    def calcular_Imc(self):
        imc = self.__peso / (self.__altura * self.__altura)
        if self.__sexo == "F":
            if imc < 19.1:
                return "abaixo do peso";
            else:
                if imc < 25.8:
                    return "no peso normal";
                else:
                    if imc < 27.3 :
                        return "marginalmente acima do peso";
                    else:
                        if imc < 32.3 :
                            return "acima do peso ideal";
                        else:
                            return "obeso";
        else:
            if imc < 20.7:
                return "abaixo do peso";
            else:
                if imc < 26.4:
                    return "no peso normal";
                else:
                    if imc < 27.8:
                        return "marginalmente acima do peso";
                    else:
                        if imc < 31.1:
                            return "acima do peso ideal";
                        else:
                            return "obeso";
