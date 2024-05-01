def permute(digits, current, repeat, result):
    if len(current) == len(digits):
        result.append(' '.join(map(str, current)))
    else:
        for digit in digits:
            if not repeat and digit in current:
                continue
            current.append(digit)
            permute(digits, current, repeat, result)
            current.pop()
def generate_permutations(digits, repeat=False):
    result = []
    permute(digits, [], repeat, result)
    return result

def main():
    digits = input ("Enter the digits (separated by spaces): ").split()
    repeat = input("Allow repetition? (yes/no): ").lower() == "yes"
    
    permutations = generate_permutations(digits, repeat)
    
    print ("\nPermutations:")
    for permutation in permutations:
        print (permutation)

if __name__ == "__main__":
    main()