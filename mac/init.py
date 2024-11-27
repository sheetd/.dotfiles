# Creates symbolic links for the files/folders in the .dotfiles directory
import os

home_path = os.path.expanduser("~")
print(home_path)


# File paths to process
path_source = "/Users/neil/.dotfiles/"
path_destination = "/Users/neil/"

paths = (
  path_source + ".gitconfig", path_destination + ".gitconfig", \
  path_source + ".zshrc", path_destination + ".zshrc", \
  path_source + ".ssh", path_destination + ".ssh", \
  path_source + ".aws", path_destination + ".aws", \
  path_source + "mac/Brewfile", path_destination + "Brewfile"
)

# Function to create links
def create_sym_link(source, destination):
  try:
    os.symlink(source, destination)
    print("✅ Link created:", source, "--> ", destination)
  except FileExistsError:
    print("🛑 File already exists:", destination)

# Create the links
print("Creating links:")
for i in range(0, len(paths), 2):
  path1 = paths[i]
  path2 = paths[i+1]
  create_sym_link(path1, path2)