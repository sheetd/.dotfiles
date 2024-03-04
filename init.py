import os

# Creates symbolic links for the files/folders in the .dotfiles directory

# function to create links
def create_sym_link(source, destination):
  try:
    os.symlink(source, destination)
    print("✅ Link created:", source, "--> ", destination)
  except FileExistsError:
    print("🛑 File already exists:", destination)

# Simple Function
#path1 = "/Users/neil/.dotfiles-mac/.gitconfig"
#path2 = "/Users/neil/.gitconfig"
#create_sym_link(path1, path2)

# using Tuple
paths = ("/Users/neil/.dotfiles-mac/.gitconfig", "/Users/neil/.gitconfig", \
"/Users/neil/.dotfiles-mac/.zshrc", "/Users/neil/.zshrc", \
"/Users/neil/.dotfiles-mac/.ssh", "/Users/neil/.ssh", \
"/Users/neil/.dotfiles-mac/Brewfile", "/Users/neil/Brewfile", \
"/Users/neil/.dotfiles-mac/.aws", "/Users/neil/.aws" \
)

# path1 = paths[0]
# path2 = paths[1]
# print(path1, " --> ", path2)

# print(paths)
# print(paths[0::2])
# print(paths[1::2])

# for i in range(0, 10, 2):
#   print(i)

print("Creating links:")
for i in range(0, len(paths), 2):
  path1 = paths[i]
  path2 = paths[i+1]
  # print(path1, " --> ", path2)
  create_sym_link(path1, path2)



# TODO: setup variables for the path prefixes like

path_home = "/Users/neil"
path_repo = "/Users/neil/.dotfiles-mac"


# -------


'''
# using a loop
for path in paths:
  # 1, 3, 5...
  path1 = path

  # 2, 4, 6...
  index = paths.index(path)
  index += 1
  path2 = paths.index(index)

  print(path1, " --> ", path2)

  
# try incrementing another way
for i in paths:
  print(paths.index(i))
  print(i)
  # check for even number items in the list
  if paths.index(i) % 2 == 0:
    print(i)
  path2 = paths[i+1]
  print(path2)

for i in range(len(paths)):
  print(i)

size = len(paths)
for i in range(size):
  print(i)


# get a range in a list
print(paths[0:2])
'''