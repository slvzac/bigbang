import json

def generate_big_bang_array():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("BIG BANG")
        elif i % 3 == 0:
            result.append("BIG")
        elif i % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(i))
    return result

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    big_bang_array = generate_big_bang_array()
    save_to_json(big_bang_array, 'output.json')
    print("Output saved to output.json")

# main()
# will ensure module works fine 
if __name__ == "__main__":
    main()
