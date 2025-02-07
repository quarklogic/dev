#!/bin/bash

# Script name: remove_users.bash
# Purpose: Remove 50 users

# Define the number of users to create
user_count=50

echo "Remove $user_count users"

# Loop through 1 through 50 
for number in {1..50}
do
	# Define the username
	user_name="testuser$number"
	echo "Removing user name: $user_name"

	# Create the user account
	userdel $user_name

done



