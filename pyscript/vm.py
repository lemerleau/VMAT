"""
@author: Nono Saha Cyrille Merleau
@email: cyrille.nono@lancaster.ac.uk

"""
# Here import the libraries

def main():

    a = 42
    b = [1, 2, 3, 4, 5]
    c = "hello world"

    print(f"The 'virtual address' of integer a: {hex(id(a))}")
    print(f"The 'virtual address' of list b: {hex(id(b))}")
    print(f"The 'virtual address' of string c: {hex(id(c))}")

    # Modify b and see if its address changes
    b.append(6)
    print(f"After modifying b, its address: {hex(id(b))}")


if __name__ == '__main__':
    main()
