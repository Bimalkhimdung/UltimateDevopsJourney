#!/bin/bash

#This code is made for multipication of two numbers

read -p "Enter first number: " num1
read -p "Enter second number: " num2

mul=$(($num1 * $num2 ))

echo " Multiplication of $num1 and $num2 is : $mul"