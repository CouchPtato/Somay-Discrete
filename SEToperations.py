class SET:
    def __init__(self, elements):
        self.elements = elements

    def ismember(self, element):
        return element in self.elements
    
    def powerset(self):
        power_set = [[]]
        for element in self.elements:
            subsets = []
            for subset in power_set:
                subsets.append(subset + [element])

            power_set += subsets
        return power_set
    
    def subset(self, other_set):
        return set(self.elements).issubset(other_set.elements)

    def union (self, other_set):
        return set(self. elements).union(other_set.elements)

    def intersection(self, other_set):
        return set(self. elements).intersection (other_set.elements)

    def complement (self, universal_set):
        return set(universal_set. elements).difference (self . elements) 
    
    def difference (self, other_set):
        return set(self. elements).difference (other_set.elements) 
    
    def symmetric_difference(self, other_set):
        return set(self. elements).symmetric_difference (other_set.elements)
    
    def cartesian_product (self, other_set):
        cartesian = []
        for element1 in self.elements:
            for element2 in other_set.elements:
                cartesian.append((element1, element2))
        return cartesian
 
def main():
    # Input for set1
    set1_elements = input("Enter the elements of the first set separated by commas: ").split(',')
    set1_instance = SET(set1_elements)

    # Input for set2
    set2_elements = input("Enter the elements of the second set separated by commas: ").split(',')
    set2_instance = SET(set2_elements)
    
    print('SET Operations Menu \n')
    print("1. Check membership")
    print("2. Power set")
    print("3. Check subset")
    print("4. Union")
    print("5. Intersection")
    print("6. Complement")
    print("7. Set difference")
    print("8. Symmetric difference")
    print("9. Cartesian product")
    
    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        element = input("Enter the element to check membership for: ")
        print(f"{element} is in set1: {set1_instance.ismember(element)}")
        print(f"{element} is in set2: {set2_instance.ismember(element)}")

    elif choice == 2:
        print("Power set of set1:", set1_instance.powerset())
        print("Power set of set2:", set2_instance.powerset())

    elif choice == 3:
        print("Set1 is a subset of set2:", set1_instance.subset(set2_instance))
        print("Set2 is a subset of set1:", set2_instance.subset(set1_instance))

    elif choice == 4:
        print("Union:", set1_instance.union(set2_instance))

    elif choice == 5:
        print("Intersection:", set1_instance.intersection(set2_instance))

    elif choice == 6:
        universal_set_elements = input("Enter the elements of the universal set separated by commas: ").split(',')
        universal_set_instance = SET(universal_set_elements)
        print("Complement of set1:", set1_instance.complement(universal_set_instance))
        print("Complement of set2:", set2_instance.complement(universal_set_instance))

    elif choice == 7:
        print("Set1 difference set2:", set1_instance.difference(set2_instance))
        print("Set2 difference set1:", set2_instance.difference(set1_instance))

    elif choice == 8:
        print("Symmetric difference:", set1_instance.symmetric_difference(set2_instance))

    elif choice == 9:
        print("Cartesian product:", set1_instance.cartesian_product(set2_instance))

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()