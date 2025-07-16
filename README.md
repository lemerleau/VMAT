# VMAT
Virtual Memory Address Translation in Multi-Process Operating Systems

This repository contains the material, data, and slides used for the lecture on Virtual Memory by @Lemerleau.


The repo is organised as follows:

```
├── LICENSE
├── README.md
├── pyscript
│   ├── vm.py --> the script printing virtual addresses using the function id().
│   └── vm_largeObj.py --> the script demonstrating access to large data that may or may not fit in RAM, showing how the OS can manage virtual memory
├── references -->It contains the material used to prepare this class.
└── tex
    ├── LZSCCslides
    ├── VMAT.pdf --> the lecture note.
    ├── VMAT.tex --> the tex code.
    └── pic --> All the necessary images used in the slides.
```

# Requirements
To be able to run different algorithms, the following softwares are required:

- [Python version 3.11.3](https://www.python.org/downloads/release/python-3113/) or higher

No external libraries were imported.

In case of any need to install a python package, please use the following command for `pip` installation.

```
pip install <package_name>
```

All the Python scripts were tested on the following operating systems:

* MacOS Mojave
* Debian Xfce 4.12

## How to run the program?
First, please clone the git repo using the command:

```
$ git clone [repo link](#)
$ cd VMAT/pyscripts
$ python vm.py
```

## Contact
If you have any questions about this class's content or problems running this code, please contact me at [Dr. Nono Saha](mailto:cyrillecardinale@gmail.com.?subject=[GitHub]%20CART%20Lecture%20Material)


## References
<a id="1" href="https://www.youtube.com/watch?v=3gRBOqf9rRY">[1]</a>
Youtube Course of  Prof. Onur Mutlu, ETH Zürich.

<a id="2" href="https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf">[2] Operating System Concepts, Abraham Silbershatz, Peter Baer G. and Greg Gagne, Tenth Edition, 2018.</a>
