total_sum = 0

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")  # Removed duplicate input statement
    
    if user_input.lower() == "stop":  # Check for stop condition
        break
    
    try:
        number = float(user_input)  # Convert input to a float
        total_sum += number  # Add number to total sum
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")

print("The total sum is:", total_sum)  # Moved outside the loop to print final sum