# New mac os computer set-up

1. Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.

```zsh
xcode-select --install
```

2. Clone repo into new hidden directory.

```zsh
# Use SSH (if set up)...
git clone git@github.com:sheetd/.dotfiles-mac.git ~/.dotfiles-mac

# ...or use HTTPS and switch remotes later.
git clone https://github.com/sheetd/.dotfiles-mac.git ~/.dotfiles-mac
```

3. Run the init script to set-up links

```zsh
sh ~/.dotfiles-mac/init.sh
```

4. Setup 1Password CLI
```zsh
# Install the 1Password CLI per their docs
```

5. Install Homebrew, followed by the software listed in the Brewfile.

```zsh
# These could also be in an install script.

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then pass in the Brewfile location...
brew bundle --file ~/.dotfiles-mac/Brewfile

# ...or move to the directory first.
cd ~/.dotfiles-mac && brew bundle
```


# TODO List

- Learn how to use [`defaults`](https://macos-defaults.com/#%F0%9F%99%8B-what-s-a-defaults-command) to record and restore System Preferences and other macOS configurations.
- Organize these growing steps into multiple script files.
- Automate symlinking and run script files with a bootstrapping tool like [Dotbot](https://github.com/anishathalye/dotbot).
- Revisit the list in [`.zshrc`](.zshrc) to customize the shell.
- Make a checklist of steps to decommission your computer before wiping your hard drive.
- Create a [bootable USB installer for macOS](https://support.apple.com/en-us/HT201372).
- Integrate other cloud services into your Dotfiles process (Dropbox, Google Drive, etc.).
- Find inspiration and examples in other Dotfiles repositories at [dotfiles.github.io](https://dotfiles.github.io/).
- And last, but hopefully not least, [**take my course, *Dotfiles from Start to Finish-ish***](https://www.udemy.com/course/dotfiles-from-start-to-finish-ish/?referralCode=445BE0B541C48FE85276 "Learn Dotfiles from Start to Finish-ish on Udemy"
)!
