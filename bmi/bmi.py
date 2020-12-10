class Bmi:
    ranges = {
        0: 18.5,
        1: 25,
        2: 30,
        3: 35,
        4: 40
    }
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
        # print("Exact value: "+ str(exact_value) + "; Rounded value: "+ str(rounded_value))
        return rounded_value

    @classmethod
    def range(cls, bmi, lang="en"):
        if bmi < 18.5:
            return cls.ranges_i18n[0][lang]
        elif (bmi >= cls.ranges[0]) and (bmi < cls.ranges[1]):
            return cls.ranges_i18n[1][lang]
        elif (bmi >= cls.ranges[1]) and (bmi < cls.ranges[2]):
            return cls.ranges_i18n[2][lang]
        elif (bmi >= cls.ranges[2]) and (bmi < cls.ranges[3]):
            return cls.ranges_i18n[3][lang]
        elif (bmi >= cls.ranges[3]) and (bmi < cls.ranges[4]):
            return cls.ranges_i18n[4][lang]
        else:
            return cls.ranges_i18n[5][lang]

    @classmethod
    def complete_info(cls, weight_kg, height_m, lang="en"):
        bmi = cls.calculate(weight_kg, height_m)
        range = cls.range(bmi, lang)
        return bmi, range

    @staticmethod
    def calculaute_weight(height_m, bmi):
        weight = bmi * pow(height_m, 2)
        rounded_weight = round(weight, 1)
        # print("Exact value weight: "+ str(weight) + "; Rounded value weight: "+ str(rounded_weight))
        # print("Height: "+ str(height_m) + "; bmi: "+ str(bmi))
        return rounded_weight

    @classmethod
    def your_weight_boundaries(cls, height_m):
        weight_per_range = [
            cls.calculaute_weight(height_m, cls.ranges[0]),
            cls.calculaute_weight(height_m, cls.ranges[1]),
            cls.calculaute_weight(height_m, cls.ranges[2]),
            cls.calculaute_weight(height_m, cls.ranges[3]),
            cls.calculaute_weight(height_m, cls.ranges[4])
        ]
        return weight_per_range

