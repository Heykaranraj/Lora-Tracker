#!/usr/bin/env python3
# device_status.py
# Quick utility: checks for an Arduino-like serial device and prints port info.
# Exits with code 1 if no suitable device is found (real-only).

import serial.tools.list_ports
import sys
import argparse

def find_arduino_ports():
    ports = list(serial.tools.list_ports.comports())
    results = []
    for p in ports:
        desc = (p.description or "").lower()
        hwid = (p.hwid or "").lower()
        name = (p.device or "")
        # common signals of Arduino/USB-serial
        if ('arduino' in desc) or ('ch340' in hwid) or ('cp210' in hwid) or ('ftdi' in hwid) or ('usb serial' in desc) or ('usb-serial' in desc):
            results.append(p)
    return results, ports

def main():
    parser = argparse.ArgumentParser(description="Check Arduino-like serial devices connected")
    parser.add_argument('--list-all', action='store_true', help='Show all serial ports (not just likely Arduinos)')
    args = parser.parse_args()

    arduino_ports, all_ports = find_arduino_ports()

    if args.list_all:
        print("All detected serial ports:")
        for p in all_ports:
            print(f"  {p.device} | {p.description} | {p.hwid}")
        if not all_ports:
            print("  (none)")
    else:
        if not arduino_ports:
            print("No Arduino-like serial devices detected.")
            print("Use --list-all to see all serial ports.")
            sys.exit(1)
        print("Likely Arduino-like devices:")
        for p in arduino_ports:
            print(f"  {p.device} | {p.description} | {p.hwid}")
    # success
    sys.exit(0)

if __name__ == '__main__':
    main()
