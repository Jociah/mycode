#!/usr/bin/env python3
"""Author: Jociah Starks | TLG Learning
   CHALLENGE 01 - Solution"""

import time

def main():
    user_input = input("Please enter an IPv4 IP address: ")
    print("You told me the IPv4 address is:", user_input)

    # asking user for 'vendor name'
    vendor = input("Please input the manufacture's name: ")
    print("The name of the vendor is:", vendor)
    time.sleep(1) # Sleep for 1 seconds
    print("Thank You! Have a nice day!")

main()
