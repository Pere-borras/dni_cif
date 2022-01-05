
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
