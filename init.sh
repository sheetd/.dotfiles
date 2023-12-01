#! /usr/bin/zsh

# Variables
OK="link updated"
KO="link skipped"

# setup links for local dotfiles

# Brewfile
if [ -e ~/.Brewfile ]
then
	echo $KO
else
	ln -s ~/.dotfiles-mac/Brewfile ~/.Brewfile
	echo $OK
fi

# AWS
if [ -e ~/.aws ]
then
	echo $KO
else
	ln -s ~/.dotfiles-mac/.aws ~/.aws
	echo $OK
fi

# Git
if [ -e ~/.gitconfig ]
then
	echo $KO
else
	ln -s ~/.dotfiles-mac/.gitconfig ~/.gitconfig
	echo $OK
fi

# zsh
if [ -e ~/.zshrc ]
then
	echo $KO
else
	ln -s ~/.dotfiles-mac/.zshrc ~/.zshrc
	echo $OK
fi

# SSH
if [ -e ~/.ssh ]
then
	echo $KO
else
	ln -s ~/.dotfiles-mac/.ssh ~/.ssh
	echo $OK
fi