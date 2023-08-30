# IronKey Password Manager
![alt text](https://github.com/mahmoudi-1798/IronKey/blob/master/images/Menu_image.png?raw=true)
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
  - [Deleting Your Account](#deleting-your-account)
  - [About](#about)
- [Future Developments](#future-developments)
- [Contributing](#contributing)
- [License](#license)

## About the Development of IronKey
This project is built upon the foundation laid by @heydyvex, this project has seen substantial development and customization on my part. The result is an even more robust and enhanced version.

## Getting Started

### Installation
To use IronKey, you need to have Python installed on your system. Clone this repository to your local machine:
```
git clone https://github.com/mahmoudi-1798/IronKey.git
```

### Initializing a User   
Before using IronKey, you need to Create an account by running the following command:
```
python ironkey.py init
```
You will be prompted to provide a username and password. Please keep this information safe, as it will be needed to access your encrypted passwords.

## Usage
IronKey provides various commands to manage your passwords. Here's an overview of the available commands:

### Adding Passwords
To add a password to IronKey's database, use the following command:
```
IronKey> add
```
You will be prompted to enter a title (label) and the password. IronKey will encrypt and store the password securely.

### Generating Passwords
IronKey can also generate strong passwords for you. Use the following command:
```
IronKey> generate
```
You'll need to provide a title (label) and choose an option from 1 to 4 (strongest to weakest). It's recommended to use option 1 for the strongest passwords.

### Deleting Passwords
To delete a stored password, use the following command:
```
IronKey> delete
```
You'll need to provide the title of the password you want to delete.

### Listing All Passwords
![alt text](https://github.com/mahmoudi-1798/IronKey/blob/master/images/listall_image.png?raw=true)
To list all stored passwords, use the following command:
```
IronKey> listall
```

### Updating Passwords
To update a password, use the following command:
```
IronKey> update
```
You'll need to provide the title of the password you want to update, You have the option to either generate a new password or input one manually, and confirm the update.

### Backing Up Data
To create a backup of your IronKey data, use the following command:
```
IronKey> backup
```
Please handle backup files with care and ensure they are stored securely.

### Deleting Your Account
![alt text](https://github.com/mahmoudi-1798/IronKey/blob/master/images/purge_image.png?raw=true)
To permanently delete your account and erase all stored passwords, use the following command:
```
IronKey> purge
```
This command is irreversible and will remove all data associated with your account.

### About
About the project:
```
IronKey> help
```

## Future Developments
IronKey is an ongoing project, and, we'll be regularly updating the project to enhance its features and usability. Future developments may include:
- Enhanced user interface
- Improved password generation algorithms
- Additional security features

## Contributing
Contributions to IronKey are welcome! Feel free to open issues and pull requests to suggest improvements or report bugs.

