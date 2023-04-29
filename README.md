# IronKey

## about IronKey
this a project to help you manage your passwords localy without any thirdpart app
you need to be carful when you are using this app for more info check Security

### instructions
all basic commands of IronKey are:

```
IronKey init
IronKey add
IronKey generate
IronKet delete
IronKey listall
IronKey update
IronKey backup
IronKey help
```


#### init command
this command initialize a user for app
it take two input **username** and **password** 
if you initialized user ***you cannot do it again*** for now maybe I put that feature in the future but for now you have to be carful with your password to remeber it because if you don’t it will be problematic when you want to decrypt passwords


#### add command
this let you to put your passwords that already exist to IronKey database
It take two input **title or label** and **password** and it encrypt password then store it in database
**I suggest you to use generate command to generate new password and edit your related account password to new password that has been generated**
if title already exit you need to choose another title or use **update command**


#### generate command
this command take two input **title** and **option** 
title as a label and in option you need to choose a number from 1 to 4, 1 is strongest password and 1 is weakest password **just always use 1 option to keep it strong**
if label exist you won’t be able to add it and you need to choose different label or might you want to update the label you need to use **update command**

#### delete command
be careful with this command and use it consciously as it sounds like it is for deleting a password
it take title and it delete title and password if title exist

#### listall command
this simple command will list you all label that exists and if it is not then show in console **there is nothing here**

#### update command
this command take three input one for update specific title that you want ot update if it is not exist mission will stop
if it is exist the other input will show up first for title second is option from 1 to 4, that you should use 1 to generate new strong password

#### backup command
this command will backup database or hole app for you to as a backup
please be careful with backup file, you have to be professional with this and don’t put it somewhere unsafe 

#### help command
this command will show you all instructions you need to work with IronKey perfectly


in progress.....
