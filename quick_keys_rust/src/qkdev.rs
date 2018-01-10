use quickkeys::QuickKeys;
use std::thread;
use std::sync::mpsc::{channel, Sender, Receiver};

#[derive(Debug)]
pub struct QKDev {
    device: QuickKeys,
    handle: Option<thread::JoinHandle<()>>,
    tx: Option<Sender<bool>>,
}

impl QKDev {
    pub fn new(port: &str) -> QKDev {
        let (tx, rx) = channel::<bool>();
        let mut qk = QKDev {
            device: QuickKeys::new_on(port),
            handle: None,
            tx: Some(tx),
        };
        qk.init(rx);
        return qk;
    }
    
    pub fn new_from(device: QuickKeys) -> QKDev {
        return QKDev {
            device: device,
            handle: None,
            tx: None,
        };
    }
    
    fn init(&mut self, rx: Receiver<bool>) {
        let local_dev = self.device().clone();
        self.handle = Some(thread::spawn(move || {
            local_dev.start(rx);
        }));
    }
    
    pub fn start(&mut self) {
        let (tx, rx) = channel::<bool>();
        self.tx = Some(tx);
        self.init(rx);
    }
    
    /*pub fn stop(&mut self) {
        if let Some(tx) = self.tx.clone() {
            let _res = tx.send(true);
            self.tx = None;
            if let Some(ref handle) = self.handle {
                handle.join();
            }
            self.handle = None;
        }
        else {
            println!("tx is not initialized");
        }
    }*/
    
    pub fn stop(mut self) -> QKDev {
        if let Some(tx) = self.tx.clone() {
            let _res = tx.send(true);
            self.tx = None;
            if let Some(handle) = self.handle {
                let _res2 = handle.join();
            }
            self.handle = None;
        }
        else {
            println!("tx is not initialized");
        }
        return QKDev::new_from(self.move_device());
    }
    
    pub fn device(&mut self) -> &mut QuickKeys {
        return &mut self.device;
    }
    
    fn move_device(self) -> QuickKeys {
        return self.device;
    }
    
    pub fn handle(&self) -> &Option<thread::JoinHandle<()>> {
        return &self.handle;
    }
}
