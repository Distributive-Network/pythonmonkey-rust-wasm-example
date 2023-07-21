# PythonMonkey Rust WebAssembly Example

This example demonstrates compiling a Rust library to WebAssembly, 
creating a JavaScript package api for it, and calling it from Python.

This is accomplished using [PythonMonkey](https://pythonmonkey.io/), a Python library for executing 
JavaScript and WebAssembly from Python. [Check it out on GitHub](https://github.com/Distributive-Network/PythonMonkey)!

## Required Software Installation

Install Rust + Cargo: https://doc.rust-lang.org/cargo/getting-started/installation.html

Install `wasm-pack` using Cargo: `$ cargo install wasm-pack`

Install Python with a minimum version of 3.8.

Install PythonMonkey using pip: `$ pip install pythonmonkey`

## Compile and Run
Compile:
```sh
$ ./build.sh
```

Run:
```sh
$ python3 main.py
```

## Note: Temporary Shim
Support for Node.js libraries with PythonMonkey is currently a work in 
progress so the `build.sh` script is required to convert Node.js specific 
code to PythonMonkey friendly code. This is performed by replacing 
`readFileSync` with Python's `open` and writing a simple pure JS version 
of `join` from the `path` library.

