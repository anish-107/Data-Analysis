# Mean
def mean(data):
    if len(data):
        return sum(data) / len(data)        
    else:
        return "Something went wrong"

# Median
def median(data):
    if len(data):
        data.sort()
        
        if len(data) % 2 != 0:
            return data[len(data) // 2]
        else:
            return (data[len // 2] + data[(len // 2) + 1] / 2)

    else:
        return "Something went wrong"


# Mode
def mode(data):
    if len(data):
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1

        max_frequency = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_frequency]

        if len(modes) == 1:
            return modes[0]
        else:
            return "No Unique values"

    else:
        return "Something went wrong"


# Driver Code
try:
    data = list(map(float, input("Enter the data set in space separated values : ").split()))

    while True:
        print('''
Options available 
1. Mean
2. Median
3. Mode
4. Data
5. Exit''')

        option = int(input("Choose an option : "))

        match option:
            case 1:
                print(f"The mean of the data set is : {mean(data)}")
            case 2:
                print(f"The median of the data set is : {median(data)}")
            case 3:
                print(f"The mode of the data set is : {mode(data)}")
            case 4:
                print(f"The data set : {data}")
            case 5:
                print(f"Exiting the program ....")
                break
            case _:
                print("Select a valid option")

except ValueError:
    print("An invalid number was given as input !!!")
