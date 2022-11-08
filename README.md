# Twitch Interactor
This project is my representation of interacting with Twitch's API.

# Set Up
1) Follow API set up steps on Twitch's website
2) Create a local json file on your machine called `twitch_api_constants.json`
3) Copy and paste the example file from `examples/twitch_api_constants.json`
4) Replace the values in your json file with all the actual values.
5) Change path under `src/constants/constants.py` to the path of the json file you just created.

# Scripts
## random_follower_generator.py
How to Run:
1) Make sure you followed all Set Up steps above.
2) Make sure you have `"my_user_id"` in your json file set to your twitch account's user_id.
3) In terminal, enter the command `python3 random_follower_generator.py` and follow prompt.