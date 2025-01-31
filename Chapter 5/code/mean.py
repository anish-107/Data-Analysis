try:
    data = list(map(float, input("Enter the numbers to find mean : ").split()))
    
    if len(data):
        print(f"Mean of data is : {sum(data) / len(data)}")
    else:
        print("No value was given !!!")

except ValueError:
    print("Invalid numbers were given as inputs !!!")
