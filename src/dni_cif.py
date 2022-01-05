
class DNI:

    def __init__(self, chain=''):

        self.dni = chain
        self.healthy_number = False
        self.healthy_letter = False
        self.table = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D',
                      'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    ### Public methods ###

    def set_dni(self, chain):
        self.dni = chain

    def get_dni(self):
        return self.dni

    def set_healthy_number(self, value):
        self.healthy_number = value

    def get_healthy_number(self):
        return self.healthy_number

    def set_healthy_letter(self, value):
        self.healthy_letter = value

    def get_healthy_letter(self):
        return self.healthy_letter

    def calculate_letter(self):
        return int(self.dni[:-1]) % len(self.table)

    def obtain_letter(self):
        if self.get_healthy_number():
            return self.table[self.calculate_letter()]

        else:
            return False

    def ensure_letter(self):
        if self.get_healthy_number():
            return self.obtain_letter() == self.dni[-1]

        else:
            return False

    def check_dni(self):
        self.set_healthy_number(
            self.check_length() and self.check_number())

        return self.get_healthy_number

    def check_letter(self):
        if self.get_healthy_number():
            self.set_healthy_letter(
                self.check_alpha() and self.ensure_letter())
            return self.get_healthy_letter()

        else:
            return False

    def check_cif(self):
        return self.check_dni() and self.check_letter()

    ### Private methods ###

    def check_length(self):
        return len(self.dni) == 9

    def check_number(self):
        return self.dni[:-1].isdigit()

    def check_alpha(self):
        return self.dni[-1] in self.table


if __name__ == '__main__':

    import math
    import random

    ### Casos test ALEATORIOS ###

    casosTest = []
    numeroCasos = 25

    for i in range(1, numeroCasos + 1):
        caso = ""
        for j in range(1, 9):
            # random.randrange(start, stop[, step])
            # numeroAleatorio = random.randint(0, 9)
            # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
            # generamos un numero aleatorio entre 48 y 58
            caracterAscii = random.randrange(48, 58 + 1, 1)
            # convertimos el numero ASCII a caracter. chr() toma el argumento como codigo ASCII de un caracter
            caso = caso + chr(caracterAscii)
        # en la ultima posicion añado una letra A-Z
        caso = caso + chr(random.randrange(65, 90 + 1, 1))
        casosTest = casosTest + [caso]

    print(casosTest)

    for dni in casosTest:
        objeto = DNI(dni)
        print(objeto.get_dni())
        objeto.check_cif()
        print('DNI --->', objeto.get_healthy_number())
        # print(objeto.calcularLetra())
        print('Letter --->', objeto.get_healthy_letter())
        print('The letter is', objeto.ensure_letter())

    ### Casos test OK ###

    casosTest = [  # casos OK
        "78484464T", "72376173A", "01817200Q", "95882054E", "63587725Q",
        "26861694V", "21616083Q", "26868974Y", "40135330P", "89044648X",
        "80117501Z", "34168723S", "76857238R", "66714505S", "66499420A", "41660450K"]

    print("\n #### CASOS OK #### \n")

    for dni in casosTest:
        objeto = DNI(dni)
        print(objeto.get_dni())
        objeto.check_cif()
        print('DNI --->', objeto.get_healthy_number())
        # print(objeto.calcularLetra())
        print('Letter --->', objeto.get_healthy_letter())
        print('The letter is', objeto.ensure_letter())
