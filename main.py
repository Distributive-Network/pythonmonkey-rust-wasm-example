#!/usr/bin/env python3
"""
Main entry point. This is a Python program that executes Rust code
compiled into the `hello_wasm` project.

Make sure to run ./build.sh before running this code.
"""

import pythonmonkey as pm

test = pm.require("./pkg/my_rust_library");

print(test.add(1,2)) # this will pring 3.0

