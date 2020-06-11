After cloning this project, you need to provide details of the Darktrace appliance you want to connect to.
To do this:
1. Create a new file called apitoken.py in the same folder
2. Copy in the following content:
authparams={'server': 'https://darktrace.example.com', 'private': 'xxxxxxxxxxx', 'public':'yyyyyyyyyyyyy'}

3. Edit that line with the URL and tokens of your appliance. (You can find the tokens on the /config page)