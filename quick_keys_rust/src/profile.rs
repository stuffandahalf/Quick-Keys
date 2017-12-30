use std::string::String;

use KEYS;

//#[derive(Debug, Clone, Copy]
pub struct Profile {
    name: String,
    symbols: [String; KEYS],
}

impl Profile {
    pub fn new() -> Profile {
        return Profile {
            name: String::from("Default"),
            symbols: [String::from("π"),
                      String::from("Σ"),
                      String::from("α"),
                      String::from("β"),
                      String::from("Δ"),
                      String::from("Ω")]
            
        };
    }
    
    pub fn get_name(&self) -> &str {
        return &*self.name;
    }
    
    pub fn get_symbols(&self, i: usize) -> &str {
        return &*(self.symbols[i]);
    }
}
