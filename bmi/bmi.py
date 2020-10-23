class Bmi:
    def hello(self):
        return "This util calculates the Body Mass Index"

    @staticmethod
    def calculate(weight_kg, height_m):
        exact_value = weight_kg / pow(height_m, 2)
        rounded_value = round(exact_value, 1)
        print("Exact value: "+ str(exact_value) + "; Rounded value: "+ str(rounded_value))
        return rounded_value

    @staticmethod
    def range(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif (bmi >= 18.5) and (bmi < 24.9):
            return "Healthy"
        elif (bmi >= 25) and (bmi < 29.9):
            return "Overweight"
        elif (bmi >= 30) and (bmi < 34.9):
            return "Obese | Class I"
        elif (bmi >= 35) and (bmi < 39.9):
            return "Obese | Class II"
        else:
            return "Obese | Class III"

