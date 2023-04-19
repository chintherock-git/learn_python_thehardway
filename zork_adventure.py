from sys import argv
script,user=argv
prompt = '> '
print("\nHi {} ,I'm the {} script".format(user,script))
print("\nI'd love to ask you a few questions")
print("\nDo you like me {} ?".format(user))
like=input(prompt)
print("Where do u live {} ?".format(user))
live=input(prompt)
print("What kind of computer do u have {} ?".format(user))
comp=input(prompt)

print('''Alrighty, So you said {} about liking me
you live in {} .Don't know where that is
And you  have a {} computer'''.format(like,live,comp))
