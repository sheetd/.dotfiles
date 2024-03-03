import os

# Created symbolic links for the files/folders in the .dotfiles directory
def create_sym_link(source, destination):
  try:
    #os.symlink(source, destination)
    print("Link created:", source, "--> ", destination)
  except FileExistsError:
    print("File already exists:", destination)

# Simple Function
#path1 = "/Users/neil/.dotfiles-mac/.gitconfig"
#path2 = "/Users/neil/.gitconfig"
#create_sym_link(path1, path2)


# ---------------------------------------------------------
# Function using Tuple
paths = ("/Users/neil/.dotfiles-mac/.gitconfig", "/Users/neil/.gitconfig", \
"/Users/neil/.dotfiles-mac/.zshrc", "/Users/neil/.zshrc")

'''
# how to increment this?
for path in paths:
  print("Link created:", paths[0], "--> ", paths[1])
'''

# try incrementing another way
for i in paths:
  print(paths.index(i))
  print(i)
  # check for even number items in the list
  if paths.index(i) % 2 == 0:
    print(i)
  path2 = paths[i+1]
  print(path2)


'''
for i in range(len(paths)):
  print(i)

size = len(paths)
for i in range(size):
  print(i)
'''


