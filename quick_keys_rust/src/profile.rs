use KEYS;
use std::string::String;

#[derive(Debug, Clone)]
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
    
    /*pub fn get_name(&self) -> &str {
        return self.name;
    }*/
    
    /*pub fn get_symbols(&self) -> [&str; KEYS] {
        return self.symbols;
    }*/
    
    /*pub fn get_symbol(&self, i: usize) -> &str {
        return self.symbols[i];
    }*/
    
    pub fn set_name(&mut self, name: String) {
        self.name = name;
    }
    
    pub fn name(&self) -> &String {
        return &self.name;
    
    pub fn get_symbol(&self, i: usize) -> &str {
        return &*self.symbols[i];
    }
    
    pub fn set_symbol(&mut self, index: usize, symbol: &str) {
        self.symbols[index] = String::from(symbol);
    }
}

