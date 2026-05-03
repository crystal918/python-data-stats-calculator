def get_numbers():
    numbers = []
    print("Enter numbers for analysis. Type 'done' when you’re finished:")
    
    while True:
        user_input = input(f"Enter number {len(numbers)+1} or type 'done' to finish: ")
        
      
        if user_input.lower() == 'done':
            if len(numbers) == 0:
                print("You didn’t enter any numbers. Please enter at least one number.")
                continue  
            break  
        
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number or type 'done' to finish!")
    
    return numbers

def calculate_sum(data):
    return sum(data)

def calculate_average(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def find_min(data):
    return min(data) if data else 0

def find_max(data):
    return max(data) if data else 0

def calculate_range(data):
    return max(data) - min(data) if data else 0

def main():
    print("=== Simple Data Stats Calculator ===")
    data = get_numbers()
    
    print("\n📊 DATA ANALYSIS RESULTS:")
    print(f"Numbers entered: {data}")
    print(f"Total count: {len(data)}")
    print(f"Sum: {calculate_sum(data)}")
    print(f"Average: {round(calculate_average(data), 2)}")
    print(f"Minimum: {find_min(data)}")
    print(f"Maximum: {find_max(data)}")
    print(f"Range: {calculate_range(data)}")
    
    
    avg = calculate_average(data)
    if avg > 100:
        print("\n💡 Insight: Your data average is above 100")
    elif avg > 50:
        print("\n💡 Insight: Your data average is above 50")
    else:
        print("\n💡 Insight: Your data average is 50 or below")

if __name__ == "__main__":
    main()
