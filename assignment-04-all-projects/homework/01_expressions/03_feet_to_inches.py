def main():
    # Ask the user for a measurement in feet
    feet = float(input("Enter the measurement in feet: "))

    # Convert to inches
    inches = feet * 12

    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == '__main__':
    main()