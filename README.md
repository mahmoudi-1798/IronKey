# IronKey Password Manager
IronKey is a local password management project that allows you to securely manage your passwords without relying on any third-party applications. This README provides an overview of the project, its features, and instructions on how to use it effectively.

## Table of Contents
- [About IronKey](#about-ironkey)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Initializing a User](#initializing-a-user)
- [Usage](#usage)
  - [Adding Passwords](#adding-passwords)
  - [Generating Passwords](#generating-passwords)
  - [Deleting Passwords](#deleting-passwords)
  - [Listing All Passwords](#listing-all-passwords)
  - [Updating Passwords](#updating-passwords)
  - [Backing Up Data](#backing-up-data)
  - [Getting Help](#getting-help)
- [Future Developments](#future-developments)
- [Contributing](#contributing)
- [License](#license)

## About IronKey
IronKey is a password management project that prioritizes local storage and security. It aims to provide users with a simple and efficient way to manage their passwords without the need for third-party applications. By keeping your password data on your local device, IronKey ensures that you have full control over your sensitive information.

## Getting Started

### Installation
To use IronKey, you need to have Python installed on your system. Clone this repository to your local machine:
```
git clone https://github.com/mahmoudi-1798/IronKey.git
```

### Initializing a User
Before using IronKey, you need to initialize a user by running the following command:
```
python ironkey.py init
```
You will be prompted to provide a username and password. Please keep this information safe, as it will be needed to access your encrypted passwords.

## Usage
IronKey provides various commands to manage your passwords efficiently. Here's an overview of the available commands:

### Adding Passwords
To add a password to IronKey's database, use the following command:
```
python ironkey.py add
```
You will be prompted to enter a title (label) and the password. IronKey will encrypt and store the password securely.

### Generating Passwords
IronKey can also generate strong passwords for you. Use the following command:
```
python ironkey.py generate
```
You'll need to provide a title (label) and choose an option from 1 to 4 (strongest to weakest). It's recommended to use option 1 for the strongest passwords.

### Deleting Passwords
To delete a stored password, use the following command:
```
python ironkey.py delete
```
You'll need to provide the title of the password you want to delete.

### Listing All Passwords
To list all stored passwords, use the following command:
```
python ironkey.py listall
```

### Updating Passwords
To update a password, use the following command:
```
python ironkey.py update
```
You'll need to provide the title of the password you want to update, choose an option from 1 to 4 to generate a new strong password, and confirm the update.

### Backing Up Data
To create a backup of your IronKey data, use the following command:
```
python ironkey.py backup
```
Please handle backup files with care and ensure they are stored securely.

### Getting Help
For assistance with using IronKey and its commands, use the following command:
```
python ironkey.py help
```

## Future Developments
IronKey is an ongoing project, and future developments may include:

## Enhanced user interface
Improved password generation algorithms
Additional security features

## Contributing
Contributions to IronKey are welcome! Feel free to open issues and pull requests to suggest improvements or report bugs.

## License
This project is licensed under the MIT License.
