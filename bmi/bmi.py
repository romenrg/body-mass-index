import logging.config
from os import path

logger = logging.getLogger('bmi')
logging.config.fileConfig(str(path.dirname(path.realpath(__file__))) + '/logging_config.ini')


class Bmi:

    boundaries = [
        0,
        18.5,
        25,
        30,
        35,
        40
    ]

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
            "en": "Obese, Class I",
            "es": "Obesidad, Clase I"
        },
        4: {
            "en": "Obese, Class II",
            "es": "Obesidad, Clase II"
        },
        5: {
            "en": "Obese, Class III",
            "es": "Obesidad, Clase III"
        }
    }

    @staticmethod
    def calculate_bmi(weight_kg, height_m):
        exact_value = weight_kg / pow(height_m, 2)
        rounded_value = round(exact_value, 1)
        logger.debug("Calculated BMI: Exact value: " + str(exact_value) + "; Rounded value: " + str(rounded_value))
        return rounded_value

    @classmethod
    def calculate_bmi_with_info(cls, weight_kg, height_m, lang="en"):
        bmi = cls.calculate_bmi(weight_kg, height_m)
        range = cls.get_bmi_range_info(bmi, lang)
        return bmi, range

    @classmethod
    def get_bmi_range_info(cls, bmi, lang="en"):
        if bmi < cls.boundaries[1]:
            return cls.ranges_i18n[0][lang]
        elif (bmi >= cls.boundaries[1]) and (bmi < cls.boundaries[2]):
            return cls.ranges_i18n[1][lang]
        elif (bmi >= cls.boundaries[2]) and (bmi < cls.boundaries[3]):
            return cls.ranges_i18n[2][lang]
        elif (bmi >= cls.boundaries[3]) and (bmi < cls.boundaries[4]):
            return cls.ranges_i18n[3][lang]
        elif (bmi >= cls.boundaries[4]) and (bmi < cls.boundaries[5]):
            return cls.ranges_i18n[4][lang]
        else:
            return cls.ranges_i18n[5][lang]

    @classmethod
    def get_bmi_ranges_with_info(cls, lang="en"):
        detailed_ranges = []
        logger.debug("Ranges with information")
        for i, boundary in enumerate(cls.boundaries):
            if i + 1 < len(cls.boundaries):
                detailed_ranges.append({"From": boundary, "To": cls.boundaries[i + 1],
                                        "Info": cls.get_bmi_range_info(boundary, lang)})
                logger.debug("From: " + str(boundary) + "; To: " + str(cls.boundaries[i + 1]) +
                             "; Info: " + cls.get_bmi_range_info(boundary, lang))
            else:
                detailed_ranges.append({"From": boundary, "To": "", "Info": cls.get_bmi_range_info(boundary, lang)})
                logger.debug("From: " + str(boundary) + "; To: " + "; Info: " + cls.get_bmi_range_info(boundary, lang))
        return detailed_ranges

    @staticmethod
    def calculate_weight(height_m, bmi):
        weight = bmi * pow(height_m, 2)
        rounded_weight = round(weight, 1)
        logger.debug("Inputs are height: " + str(height_m) + " and bmi: " + str(bmi))
        logger.debug("Exact weight value is: " + str(weight) + "; And rounded weight: " + str(rounded_weight))
        return rounded_weight

    @classmethod
    def calculate_weight_boundaries(cls, height_m):
        weight_per_range = [
            cls.calculate_weight(height_m, cls.boundaries[0]),
            cls.calculate_weight(height_m, cls.boundaries[1]),
            cls.calculate_weight(height_m, cls.boundaries[2]),
            cls.calculate_weight(height_m, cls.boundaries[3]),
            cls.calculate_weight(height_m, cls.boundaries[4]),
            cls.calculate_weight(height_m, cls.boundaries[5])
        ]
        return weight_per_range

    @classmethod
    def calculate_weight_ranges_with_info(cls, height_m, lang="en"):
        weight_boundaries = cls.calculate_weight_boundaries(height_m)
        detailed_weight_boundaries = []
        logger.debug("Ranges weight boundaries information for height: " + str(height_m))
        for i, boundary in enumerate(weight_boundaries):
            if i + 1 < len(weight_boundaries):
                detailed_weight_boundaries.append({"From": boundary, "To": weight_boundaries[i + 1],
                                                   "Info": cls.ranges_i18n[i][lang]})
                logger.debug("From: " + str(boundary) + "; To: " + str(weight_boundaries[i + 1]) +
                             "; Info: " + cls.ranges_i18n[i][lang])
            else:
                detailed_weight_boundaries.append({"From": boundary, "To": "", "Info": cls.ranges_i18n[i][lang]})
                logger.debug("From: " + str(boundary) + "; To: " + "; Info: " + cls.ranges_i18n[i][lang])
        return detailed_weight_boundaries

    @classmethod
    def calculate_healthy_weight(cls, height_m):
        your_weight_boundaries = (cls.calculate_weight_boundaries(height_m))[1:3]
        logger.debug("For height: " + str(height_m) + ", your healthy boundaries are: " + str(your_weight_boundaries))
        return your_weight_boundaries
