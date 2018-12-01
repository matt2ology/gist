from urllib import request
"""
Whenever you're working with ile paths it's always good to have 
r (raw), so you can type a file and not have to escape every character
"""
directory_path = r"../TheNewBostonYouTubeTutorial/ppt_downloads/"
# What we want to download
groups_url = r'http://insight.dev.schoolwires.com/HelpAssets/' \
             r'C2Assets/C2Files/C2ImportGroupsSample.csv'
"""
Tell our Python program to connect to the internet first so what we're 
going to be doing is calling a function but it's easier if you store it
in a variable called 'response'
"""


def download_stock_data(csv_url):
    """
    URL open function the only parameter that it takes or that we're
    going to be passing in is the URL of a CSV file on the internet;
    again, it's the URL of any web page but it goes that URL and then
    it's going to store the connection to that web page in this variable
    'response.'
    """
    # Connect
    response = request.urlopen(csv_url)
    """
    Take that response and call a function on it called "read" this is
    going to read the data from whatever URL you're pointing to; so,
    we're reading in all the data (a large amount of text). 
    We have that text stored in a variable called "CSV" we don't know if
    that's string data, maybe it's numerical data, or maybe it's date data;
    so, we want to guarantee that data that we just read in is a string.
    """
    # Save as string
    csv = response.read()
    csv_str = str(csv)
    """
    The data is in one long string (one big line); however, if we ever read
    that in a file of course it's going to be confusing. What we want to do 
    is we want to take it and break it up in lines.
    Function split takes a string a huge long string and it breaks it up 
    every 10 characters. It takes a long string and it breaks it up whenever
    it comes across this new character. 
    """
    # Make a file on our computer
    """
    Inside the split() we are using an extra backslash as an escape character,
    this will basically tell python that read '\n' as a new line
    """
    lines = csv_str.split("\\n")
    dest_url = r"family_relationships.csv"
    """
    Now that we have a file open and we can write to it.
    """
    # Open and write to file
    file = open(directory_path + dest_url, 'w')
    """
    Loop through what we just downloaded and print it on the file.
    "lines" is going to loop through the string and for each individual line
    """
    for line in lines:
        """
        Take the open file and write to it.
        For each line, each chunk it broke off, print to file
        and after each line print a new line (\n).
        """
        file.write(line + "\n")
        # Close file object, so we don't waste memory on computer
    file.close()

# Call function


download_stock_data(groups_url)

