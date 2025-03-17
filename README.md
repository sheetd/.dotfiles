# Dotfiles

Clone repo into new hidden directory.

```zsh
git clone https://github.com/sheetd/.dotfiles.git ~/.dotfiles
```

## Mac Setup

1. Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.

```zsh
xcode-select --install
```

2. Install OMZ

```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

3. Setup 1Password CLI (as described in the docs)

https://developer.1password.com/docs/cli/get-started/

4. Run the init script to set-up links

```zsh
cd ~/dotfiles
./install
```

5. Install Homebrew, followed by the software listed in the Brewfile.

```zsh
# These could also be in an install script.

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then pass in the Brewfile location...
brew bundle
```

## Linux Setup

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

5. Install typical apps using `apt`

- iperf3

## Windows Setup

1. Run the install script

2. Install typical apps (1password CLI) using winget

## Upgrading dotbot module

- create a new git branch
- `cd ~/.dotfiles`
- `git submodule update --remote`
- commit a change to the branch
- merge the branch back to main

## TODO

- [ ] Make links work on Windows
- [ ] move omz to a submodule?
- [ ] Learn how to use [`defaults`](https://macos-defaults.com/#%F0%9F%99%8B-what-s-a-defaults-command) to record and restore System Preferences and other macOS configurations.
- [ ] Revisit the list in [`.zshrc`](.zshrc) to customize the shell.
