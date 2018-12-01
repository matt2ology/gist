#########
# Write #
#########
"""
open() is going to open a file or prepare a file to be created
or written so the first parameter it takes is the name of the file

The next parameter after this is going to take a couple different
characters 'W' and 'R' the first one (W) is w which means open
a file and write to it.
(If the file isn't already available it will create it)
"""
directory_path = "../TheNewBostonYouTubeTutorial/ppt_downloads/"
# Create a file object
file_write = open(directory_path + "ppt23_sample.txt", 'w')
file_write.write("This is from Python Programming Tutorial 23\n"
                 "How to Read and Write Files\n")
file_write.write("I like bacon!\n")
"""
close() doesn't take any parameters.
It basically just frees up on the extra memory the computer isn't wasting
"""
file_write.close()

########
# Read #
########

file_read = open(directory_path + "ppt23_sample.txt", 'r')

"""
Whenever we read this data (from text file) we need somewhere to store 
it because we can't just work with it directly in Python; so, we need a
variable to store that entire string.
"""
# String variable
text = file_read.read()

print(text)
