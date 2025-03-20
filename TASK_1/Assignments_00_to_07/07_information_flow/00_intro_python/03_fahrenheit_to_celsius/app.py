# 🌡️ Temperature Converter: Fahrenheit to Celsius
# 📝 This script converts temperature from Fahrenheit to Celsius.

def fahrenheit_to_celsius(fahrenheit):
    """
    📌 Convert Fahrenheit to Celsius.
    
    🔢 Formula: (°F - 32) × 5/9 = °C
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    # 🏁 Prompt user for input
    try:
        fahrenheit = float(input("❄️ Enter temperature in Fahrenheit: "))
        
        # 🔄 Convert temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        # 📢 Display the result
        print(f"✅ Temperature: {fahrenheit}°F = {celsius:.2f}°C 🌡️")
    
    except ValueError:
        print("⚠️ Please enter a valid number! 🚫")

# 🚀 Run the script when executed
if __name__ == '__main__':
    main()
