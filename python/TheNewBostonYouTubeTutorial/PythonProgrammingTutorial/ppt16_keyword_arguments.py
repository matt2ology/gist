def sentence(subject="She", verb="loves", obj="him"):
    print(subject, verb, obj, "\n")


"""
Keyword arguments allows you to select any arguments
to replace the selected default argument
"""
sentence()
sentence("The woman", "built", "a strong stone wall")
sentence(verb="sings", obj="a song")
sentence(subject="The puppy", obj="chocolate")
sentence(subject="Her cat", verb="licked")
sentence(subject="My family")
sentence(verb="dates")
sentence(obj="the movie")
# Does not matter the order of the keywords
sentence(obj="the play", subject="Many students", verb="loved")
sentence(verb="watered", obj="the flowers", subject="The firemen")

