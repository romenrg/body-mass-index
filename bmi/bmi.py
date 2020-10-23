class Bmi:
    def hello(self):
        return "This util calculates the Body Mass Index"
    @staticmethod
    def calculate(weight_kg, height_m):
        exact_value = weight_kg / pow(height_m, 2)
        rounded_value = round(exact_value, 1)
        print("Exact value: "+ str(exact_value) + "; Rounded value: "+ str(rounded_value))
        return rounded_value
