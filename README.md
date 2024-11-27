# New Mac OS computer set-up

1. Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.

```zsh
xcode-select --install
```

2. Clone repo into new hidden directory.

```zsh
# Use SSH (if set up)...
git clone git@github.com:sheetd/.dotfiles.git ~/.dotfiles

# ...or use HTTPS and switch remotes later.
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles
```

3. Install OMZ

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

4. Setup 1Password CLI (as described in the docs)

```zsh
# https://developer.1password.com/docs/cli/get-started/
```

5. Run the init script to set-up links

```zsh
python3 ~/.dotfiles/init.py
```

6. Install Homebrew, followed by the software listed in the Brewfile.

```zsh
# These could also be in an install script.

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then pass in the Brewfile location...
brew bundle
```

# TODO Mac
- [x] move init script to Python code
- [ ] Learn how to use [`defaults`](https://macos-defaults.com/#%F0%9F%99%8B-what-s-a-defaults-command) to record and restore System Preferences and other macOS configurations.
- [ ] Automate symlinking and run script files with a bootstrapping tool like [Dotbot](https://github.com/anishathalye/dotbot).
- [ ] Revisit the list in [`.zshrc`](.zshrc) to customize the shell.
- [ ] Make a checklist of steps to decommission your computer before wiping your hard drive.
- [ ] Create a [bootable USB installer for macOS](https://support.apple.com/en-us/HT201372).
- [ ] Find inspiration and examples in other Dotfiles repositories at [dotfiles.github.io](https://dotfiles.github.io/).
- [ ] And last, but hopefully not least, [**take my course, _Dotfiles from Start to Finish-ish_**](https://www.udemy.com/course/dotfiles-from-start-to-finish-ish/?referralCode=445BE0B541C48FE85276 "Learn Dotfiles from Start to Finish-ish on Udemy")!




# New Linux os set-up

1. Clone repo into new hidden directory.

```zsh
# Use SSH (if set up)...
git clone git@github.com:sheetd/.dotfiles.git ~/.dotfiles

# ...or use HTTPS and switch remotes later.
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles
```

2. If remote host, add `authorized_keys` file to the `~/.ssh` directory

3. Install OMZ

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

4. Run the init script to set-up links

```zsh
sh ~/.dotfiles/init.py
```

# TODO Linux
- [X] Move init script to Python code
- [ ] Typical apt installers (omz, etc.)


# New Windows computer set-up

1. Clone repo into new hidden directory
```powershell
# Use SSH (if set up)...
git clone git@github.com:sheetd/.dotfiles-win.git ~/.dotfiles-win

# ...or use HTTPS and switch remotes later.
git clone https://github.com/sheetd/.dotfiles-win.git ~/.dotfiles-win
```

2. Create symlinks to config files
Open a CMD terminal as admin
```bat
cd /Users/neil/
mklink /H ".gitconfig" "./.dotfiles/.gitconfig"
mklink /J ".ssh" "./.dotfiles/.ssh"
```

3. Install typical apps (1password CLI)

# TODO Windows
- [ ] Typical installers (using winget?)
- [ ] replace links section with init script