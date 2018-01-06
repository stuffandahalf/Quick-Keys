use quickkeys::QuickKeys;
use std::thread;
use std::sync::Arc;

#[derive(Debug)]
pub struct QKDev {
    device: QuickKeys,
}

impl QKDev {
    
    pub fn new(port: &str) -> QKDev {
        let qk = QKDev {
            device: QuickKeys::new_on(port),
        };
        qk.start();
        return qk;
    }
    
    pub fn start(&self) {
        let local_dev = self.device.clone();
        let handle = thread::spawn(move || {
            local_dev.start();
        });
        handle.join();
    }
    
    pub fn test(&mut self) {
        self.device.set_symbol(2, ":^)");
    }
    
    pub fn device(&self) -> &QuickKeys {
        return &self.device;
    }
}
