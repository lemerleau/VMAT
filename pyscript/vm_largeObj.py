"""
@author: Nono Saha Cyrille Merleau
@email: cyrille.nono@lancaster.ac.uk

"""
# Here import the libraries
import os
import mmap

def main():
    # Create a large file on disk to map into memory
    filename = "large_file.bin"
    size = 1024 * 1024 * 100  # 100 MB

    with open(filename, "wb") as f:
        f.seek(size - 1)
        f.write(b"\0")

    with open(filename, "r+b") as f:
        # Memory-map the file, size 0 means the whole file
        mm = mmap.mmap(f.fileno(), 0)
        # Read/write data via virtual memory
        print("First byte before:", mm[0])
        mm[0] = 123  # Write to first byte
        print("First byte after:", mm[0])

        # Accessing a "page" that may not physically be in RAM yet
        LARGE_INDEX = 1024 * 1024 * 75
        print("75MB-th byte before:", mm[LARGE_INDEX])
        mm[LARGE_INDEX] = 42
        print("75MB-th byte after:", mm[LARGE_INDEX])

        mm.close()

    os.remove(filename)

if __name__ == '__main__':
    main()
