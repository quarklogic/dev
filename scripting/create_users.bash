#!/bin/bash

# Script name: create_users.bash
# Purpose: Create 50 users

# Define the number of users to create
user_count=50

echo "Creating $user_count users"

# Loop through 1 through 50 
for number in {1..50}
do
	# Define the username
	user_name="testuser$number"
	echo "Creating user name: $user_name"

	# Create the user account
	#useradd -c "$user_name" $user_name

	# Set the password
 	new_password=''
        echo "Setting password"
	#echo -e '$new_password\n$new_password' | passwd $user_name 

done



