import instaloader
import os
from cfonts import render, say

def instagram_osint_tool(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile of the given username
        profile = instaloader.Profile.from_username(loader.context, str(username))

        # Get the profile link
        profile_link = f"https://www.instagram.com/{username}/"

        # Get the account details
        account_details = f"Username: {profile.username}\n" \
                          f"Full Name: {profile.full_name}\n" \
                          f"Bio: {profile.biography}\n" \
                          f"Followers: {profile.followers}\n" \
                          f"Following: {profile.followees}\n" \
                          f"Posts: {profile.mediacount}"

        # Clear the console
        os.system('clear')

        # Print the tool name in large size
        say("IG HUNTER", font='block', colors=['green'], align='center')

        # Print the account details and profile link
        print(f"Profile Link: {profile_link}")
        print(account_details)

        # Save the output in a text file
        with open(f"{username}_output.txt", "w") as file:
            file.write(f"Profile Link: {profile_link}\n\n")
            file.write(account_details)
            print("Output saved in a text file.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")

# Prompt the user to enter the Instagram username
username = input("Enter the Instagram username: ")

# Call the Instagram OSINT tool function
instagram_osint_tool(username)
