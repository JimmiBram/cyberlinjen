import os
import shutil
import sys


# chatnet.py
# Enkel flertrådet LAN-chat over UDP broadcast (Windows/macOS/Linux).
# API til elever:
#   from chatnet import send, listen
#   stop = listen(callback)  # kører i baggrundstråd
#   send("Hej", "general", "Jimmi")
#   stop()  # stop lytning når du vil

import socket
import json
import time
import threading

PORT = 29123
BROADCAST_ADDR = "255.255.255.255"
ENCODING = "utf-8"

def _pack(message: str, topic: str, name: str) -> bytes:
    payload = {
        "message": str(message),
        "topic": str(topic),
        "name": str(name),
        "ts": time.time(),
    }
    return json.dumps(payload, ensure_ascii=False).encode(ENCODING)

def _unpack(data: bytes):
    try:
        obj = json.loads(data.decode(ENCODING, errors="replace"))
        return {
            "message": obj.get("message", ""),
            "topic": obj.get("topic", ""),
            "name": obj.get("name", ""),
            "ts": obj.get("ts", 0),
        }
    except Exception:
        return None

def send(message: str, topic: str, name: str) -> None:
    """Send en chat-besked til alle på lokalnet (UDP broadcast)."""
    pkt = _pack(message, topic, name)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.sendto(pkt, (BROADCAST_ADDR, PORT))
        except OSError as e:
            print("Kunne ikke sende (tjek firewall/net):", e)

def listen(callback):
    """
    Start lytning i en baggrundstråd og returnér en stop()-funktion.
    callback(message, ip, topic, name) kaldes for hver modtaget besked.
    """
    stop_event = threading.Event()

    def _worker():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                # Ikke på alle OS:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except (AttributeError, OSError):
                pass
            s.bind(("", PORT))
            s.settimeout(0.5)  # så vi kan tjekke stop_event jævnligt

            while not stop_event.is_set():
                try:
                    data, addr = s.recvfrom(65535)
                except socket.timeout:
                    continue
                except OSError:
                    break
                ip = addr[0]
                obj = _unpack(data)
                if obj is None:
                    continue
                try:
                    callback(obj["message"], ip, obj["topic"], obj["name"])
                except Exception:
                    # Undgå at én fejl i elevens callback stopper lytning
                    pass

    t = threading.Thread(target=_worker, daemon=True)
    t.start()

    def stop():
        stop_event.set()
        # Giv tråden et øjeblik til at lukke pænt
        t.join(timeout=1.0)

    return stop

# --- Mini-demo når filen køres direkte (kan slettes) ---
if __name__ == "__main__":
    def demo_cb(message, ip, topic, name):
        print(f"[{topic}] {name}@{ip}: {message}")

    stop = listen(demo_cb)
    print("Lytter i baggrunden. Skriv beskeder (Ctrl+C for at afslutte):")
    try:
        while True:
            txt = input("> ")
            if txt.strip() == "/stop":
                break
            send(txt, "general", "Demo")
    except KeyboardInterrupt:
        pass
    finally:
        stop()
        print("Stopper.")


# --- Konsol-hjælpefunktioner ---
def _get_size():
    """Returnér (cols, rows) for terminalen."""
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines

def clearTop():
    """Ryd alt undtagen de nederste 3 linjer."""
    cols, rows = _get_size()
    # Flyt cursor til top og slet det meste af skærmen (undtagen de sidste 3)
    sys.stdout.write("\033[H")                    # til top
    sys.stdout.write(f"\033[0J")                  # clear fra top til bund
    sys.stdout.flush()

def clearBottom():
    """Ryd de nederste 3 linjer."""
    cols, rows = _get_size()
    for i in range(3):
        # Gå til bund minus i og ryd linjen
        sys.stdout.write(f"\033[{rows - i};1H\033[2K")
    sys.stdout.flush()

def printTop(text):
    """Print tekst i topområdet (uden at forstyrre bund)."""
    clearTop()
    sys.stdout.write("\033[H")  # gå til top
    print(text)
    sys.stdout.flush()

def printBottom(text):
    """Print tekst på de 3 nederste linjer."""
    cols, rows = _get_size()
    clearBottom()
    # del tekst i maks 3 linjer
    lines = text.splitlines()[-3:]
    start_row = rows - len(lines) + 1
    for i, line in enumerate(lines):
        sys.stdout.write(f"\033[{start_row + i};1H{line}\033[0K")
    sys.stdout.flush()
