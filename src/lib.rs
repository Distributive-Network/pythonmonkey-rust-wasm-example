use wasm_bindgen::prelude::*;

// This is our rust code we'll call from Python. A simple function
// that returns the sum of two integers.
#[wasm_bindgen]
pub fn add(a: u32, b: u32) -> u32{
  a + b
}

