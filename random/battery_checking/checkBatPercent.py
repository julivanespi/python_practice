#!/usr/bin/python
import time


def main():
    i = 0
    while i < 100:
        power_now = open(
            "/sys/class/power_supply/BAT0/charge_now", "r").readline()
        power_full = open(
            "/sys/class/power_supply/BAT0/charge_full", "r").readline()
        power_percent = float(power_now)/float(power_full) * 100
        print(round(power_percent, 2), "%")
        time.sleep(15)
        i += 1


if __name__ == "__main__":
    main()
