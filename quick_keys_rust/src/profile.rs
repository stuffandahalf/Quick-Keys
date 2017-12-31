use KEYS;

#[derive(Debug, Clone, Copy)]
pub struct Profile<'a> {
    name: &'a str,
    symbols: [&'a str; KEYS],
}

impl<'a> Profile<'a> {
    pub fn new() -> Profile<'a> {
        return Profile {
            name: "Default",
            symbols: ["π",
                      "Σ",
                      "α",
                      "β",
                      "Δ",
                      "Ω"]
            
        };
    }
    
    /*pub fn get_name(&self) -> &str {
        return self.name;
    }*/
    
    /*pub fn get_symbols(&self) -> [&str; KEYS] {
        return self.symbols;
    }*/
    
    pub fn get_symbol(&self, i: usize) -> &str {
        return self.symbols[i];
    }
}

