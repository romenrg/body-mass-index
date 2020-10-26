class Bmi:
    ranges_i18n = {
        0: {
            "en": "Underweight",
            "es": "Bajo peso"
        },
        1: {
            "en": "Healthy",
            "es": "Peso saludable"
        },
        2: {
            "en": "Overweight",
            "es": "Sobrepeso"
        },
        3: {
            "en": "Obese | Class I",
            "es": "Obesidad | Clase I"
        },
        4: {
            "en": "Obese | Class II",
            "es": "Obesidad | Clase II"
        },
        5: {
            "en": "Obese | Class III",
            "es": "Obesidad | Clase III"
        }
    }
    def hello(self):
        return "This util calculates the Body Mass Index"

    @staticmethod
    def calculate(weight_kg, height_m):
        exact_value = weight_kg / pow(height_m, 2)
        rounded_value = round(exact_value, 1)
        print("Exact value: "+ str(exact_value) + "; Rounded value: "+ str(rounded_value))
        return rounded_value

    @classmethod
    def range(cls, bmi, lang="en"):
        if bmi < 18.5:
            return cls.ranges_i18n[0][lang]
        elif (bmi >= 18.5) and (bmi < 24.9):
            return cls.ranges_i18n[1][lang]
        elif (bmi >= 25) and (bmi < 29.9):
            return cls.ranges_i18n[2][lang]
        elif (bmi >= 30) and (bmi < 34.9):
            return cls.ranges_i18n[3][lang]
        elif (bmi >= 35) and (bmi < 39.9):
            return cls.ranges_i18n[4][lang]
        else:
            return cls.ranges_i18n[5][lang]

    @classmethod
    def complete_info(cls, weight_kg, height_m, lang="en"):
        bmi = cls.calculate(weight_kg, height_m)
        range = cls.range(bmi, lang)
        return bmi, range