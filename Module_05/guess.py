#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: guess.py
#
"""

Ch 5 Programming Assignment, Part B

Create a simple "guess the number" game in a program called guess.py.
Generate a random number between 1 and 10 and then ask the user to guess it;
let the user know if their guess was high, low, or correct.
Keep repeating until they correctly guess the number.

Note: to generate a random number, see the randint() function in zyBooks 5.3.2.
Don't forget to import random.
If you have trouble getting this to work, you can skip the "randomness"
and just pick a number to be guessed.

"""

"""
Variable List

String variables:
job     - which job ("W" for wait staff, "H" for host, "K" for kitchen staff)
job_title_dic   - dictionary list of job titles to simple character label, both key and data are strings
employee_first_name - employee's first name only

Floating point numbers:
hours_worked    - hours worked in the last week
wage_rate       - hourly rate, based on job and years employed

Integers numbers: 
years_employed  - number of years employed in the current position

"""

"""
Copied in from Bash Scripting assignment

function Random
{
# Option C - Has the user try to guess the number the computer has picked,
#        at random between 1 to 10.

	local RandomNumber Guess

	RandomNumber=$(( $RANDOM%10 + 1 ))

	clear; echo; echo
	echo "   The computer has picked a number between 1 and 10."
	echo; read -p "      Please enter your guess within that range: " Guess

	if [[ ( $Guess -lt 1 ) || ( $Guess -gt 10 ) ]]
	then

		echo; echo "   Your guess was either less than 0 or "
		echo "      was greater than 10."
		echo; sleep 2

	else

		if [[ $RandomNumber -eq $Guess ]]
		then

			echo; echo "   Great guess, you were right."; sleep 2

		elif [[ $RandomNumber -gt $Guess ]]
		then

			echo; echo "   Sorry your guess was to small."; sleep 2

		else

			echo; echo "   Sorry your guess was to large."; sleep 2

		fi 

	echo; echo "   The computer picked $RandomNumber and you guessed $Guess"

        sleep 3

	fi

}

"""



# End of program
