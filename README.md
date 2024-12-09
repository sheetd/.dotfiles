# Mac OS computer set-up

1. Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.

```zsh
xcode-select --install
```

2. Clone repo into new hidden directory.

```zsh
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles
```

3. Install OMZ

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

4. Setup 1Password CLI (as described in the docs)

https://developer.1password.com/docs/cli/get-started/

5. Run the init script to set-up links

```zsh
cd ~/dotfiles
./install
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

- [ ] move omz to a submodule?
- [x] move init script to Python code
- [ ] Learn how to use [`defaults`](https://macos-defaults.com/#%F0%9F%99%8B-what-s-a-defaults-command) to record and restore System Preferences and other macOS configurations.
- [x] Automate symlinking and run script files with a bootstrapping tool like [Dotbot](https://github.com/anishathalye/dotbot).
- [ ] Revisit the list in [`.zshrc`](.zshrc) to customize the shell.

# New Linux os set-up

1. Clone repo into new hidden directory.

```zsh
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles
```

2. If remote host, add `authorized_keys` file to the `~/.ssh` directory

3. Install OMZ

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

4. Run the init script to set-up links

```zsh
  cd ~/dotfiles
./install
```

# TODO Linux

- [x] Move init script to Python code
- [ ] Add typical apt installers (omz, etc.) to script

# New Windows computer set-up

1. Clone repo into new hidden directory

```powershell
# Use SSH (if set up)...
git clone git@github.com:sheetd/.dotfiles.git ~/.dotfiles-win

# ...or use HTTPS and switch remotes later.
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles-win
```

2. Create symlinks to config files
   Open a CMD terminal as admin

```bat
cd /Users/neil/
mklink /H ".gitconfig" "./.dotfiles/win/.gitconfig"
mklink /J ".ssh" "./.dotfiles/.ssh"
```

3. Install typical apps (1password CLI)

# TODO Windows

- [ ] Typical installers (using winget?)
- [ ] replace links section with init script
