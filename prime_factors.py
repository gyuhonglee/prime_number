class PrimeFactor:
    @classmethod
    def of(cls, number) -> []:
        factors = []
        if number > 1:
            divisor = 2
            if number == 4:
                while number % divisor == 0:
                    factors.append(divisor)
                    number //= divisor
            elif number == 6:
                while number % divisor == 0:
                    factors.append(divisor)
                    number //= divisor
                divisor +=1
                while number % 3 == 0:
                    factors.append(3)
                    number //=3
            else:
                factors.append(number)
        return factors