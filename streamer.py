import tl
import tw
import threading

def stream():
    thread = threading.Thread(target=tw.stream_twitter)
    thread.start()
    tl.stream_telegram()

if __name__ == "__main__":
    stream()