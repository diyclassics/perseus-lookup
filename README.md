# Perseus-Lookup
Experimenting with a way to search the Perseus Word Study Tool from the command line using Python and Beautiful Soup. More description in the docstrings for both lookup scripts. Have successfully used this from the command line (using bash) by making the script executable and including an alias for each script in .bash_profile.

## Requirements
10/3/16: Updated to Python3

(Listed in requirements.txt)

    - Beautiful Soup v. 4.5.1
    - Requests v. 2.11.1

## Usage
I was able to use this as a command-line lookup tool (bash) by:

    1. Making latin-lookup.py and greek-lookup.py executable
    2. Adding the following lines to .bash_profile:
        - alias latin="python /[...YOUR DIRECTORY...]/latin-lookup.py"
        - alias greek="python /[...YOUR DIRECTORY...]/greek-lookup.py"

I can now use these scripts from command line as follows:

```
> latin verba
> verba > verbum: a word
```
```
> greek logos
> logos > λόγος: computation, reckoning
```

Last tested on Mac OS 10.11.6 using Terminal (bash). Feedback, suggestions, etc. for other setups welcome.
