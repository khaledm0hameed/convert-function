def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def inches_to_cm(inches):
    """Converts inches to centimeters"""
    cm = inches * 2.54
    return cm

def cm_to_inches(cm):
    """Converts centimeters to inches"""
    inches = cm / 2.54
    return inches

# Main program
print('''
1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
3. Inches to Centimeters
4. Centimeters to Inches
''')
choice = int(input("Enter choice (1-4): "))

if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

elif choice == 3:
    inches = float(input("Enter length in inches: "))
    cm = inches_to_cm(inches)
    print(f"{inches} in = {cm:.2f} cm")

elif choice == 4:
    cm = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm)
    print(f"{cm} cm = {inches:.2f} in")

else:
    print("Invalid choice")
