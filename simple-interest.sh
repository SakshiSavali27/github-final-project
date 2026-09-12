#!/bin/bash

# Simple Interest Calculator

echo "Enter principal amount:"
read principal

echo "Enter rate of interest (%):"
read rate

echo "Enter time period (years):"
read time

# Calculate simple interest: SI = (P * R * T) / 100
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

# Calculate total amount
total=$(echo "scale=2; $principal + $interest" | bc)

echo "Simple Interest: $interest"
echo "Total Amount: $total"
