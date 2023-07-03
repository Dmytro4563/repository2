if __name__ == "__main__":
    # # name = "John"
    # # surname = "Patrick"
    # # fathers_name = "Doe"
    # #
    # # print(fathers_name[::-1])
    # #
    # # print(f"{surname.title()} {name[0].upper()} {fathers_name[0].upper()}")
    #
    # users = [
    #     {
    #         "name": "John",
    #         "age":31
    #     },
    #     {
    #         "name":"Jane",
    #         "age":27
    #     },
    #     {
    #         "name": "Jack",
    #         "age": 15
    #     },
    #     {
    #         "name": "John",
    #         "age": 31
    #     },
    # ]
    # print(users)
    # temp_age = 6
    # temp_name = users[1]['name']
    # print(temp_age, temp_name)
    #
    # if temp_age >= 18:
    #     print("U can buy drink in UA")
    # elif temp_age <= 18:
    #     print("U children now)) Sorry:)")
    # else:
    #     print("WHO ARE U ?")\
    #
    # c = int (input () )
    # f = c * 9/5 + 32
    # print (f)

    def celsius_to_fahrenheit(celsius):
        """Convert temperature from Celsius to Fahrenheit"""
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit

    def fahrenheit_to_celsius(fahrenheit):
        """Convert temperature from Fahrenheit to Celsius"""
        celsius = (fahrenheit - 32) / 1.8
        return celsius

    choice = input(
        "Введіть '1', щоб конвертувати з Цельсія в Фаренгейта, або '2', щоб конвертувати з Фаренгейта в Цельсія: ")
    temperature = float(input("Введіть температуру: "))

    if choice == '1':
   converted_temperature = celsius_to_fahrenheit(temperature)
   print(f"{temperature} градусів Цельсія дорівнює {converted_temperature} градусів Фаренгейта")

    elif choice == '2':
        converted_temperature = fahrenheit_to_celsius(temperature)
   print(f"{temperature} градусів Фаренгейта дорівнює {converted_temperature} градусів Цельсія")

    else:
        print("Некоректний вибір операції. Введіть '1' або '2'")