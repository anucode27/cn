import threading
import time
import random

class GoBackN:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.sent_frames = 0
        self.acknowledged_frames = 0
        self.lock = threading.Lock()
    
    def send_frame(self, frame):
        print(f"Sender: Sending frame {frame}")
    
    def receive_ack(self, frame):
        print(f"Receiver: Acknowledgment received for frame {frame}")
    
    def transmit(self):
        while self.acknowledged_frames < self.total_frames:
            with self.lock:
                # Transmit all frames in the window
                while self.sent_frames < self.acknowledged_frames + self.window_size and self.sent_frames < self.total_frames:
                    self.send_frame(self.sent_frames)
                    self.sent_frames += 1
                
            # Simulate acknowledgment and loss
            time.sleep(1)  # wait before checking for acknowledgments
            
            with self.lock:
                for frame in range(self.acknowledged_frames, self.sent_frames):
                    if random.random() > 0.2:  # 80% chance of successful delivery
                        self.receive_ack(frame)
                        self.acknowledged_frames += 1
                    else:
                        print(f"Receiver: Frame {frame} lost, retransmitting...")
                        self.sent_frames = self.acknowledged_frames
                        break  # Go back to the oldest unacknowledged frame

def main():
    window_size = 4
    total_frames = 10
    
    gbn = GoBackN(window_size, total_frames)
    
    sender_thread = threading.Thread(target=gbn.transmit)
    sender_thread.start()
    sender_thread.join()
    
    print("Transmission Complete")

if __name__ == "__main__":
    main()
