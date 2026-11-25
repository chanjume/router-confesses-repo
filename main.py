#!/usr/bin/env python3
"""The Router Confesses: write one excuse line to /output/entry.txt.

Craft: one concrete time (11:47), one named thing (NETGEAR-5G), one
specific movie moment (the killer unmasking himself), and a petty
grievance — the router kept the network alive for years and never got
a thank you. The excuse is the router's, in its own voice, landing in
one breath with no setup that needs explaining.
"""
import os

ENTRY = 'I cut out at 11:47, right as the killer unmasked himself — you named me NETGEAR-5G and never once said thank you.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
