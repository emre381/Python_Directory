
---

# Phone Directory Program

## Overview

This Python program allows users to manage a simple phone directory through a text-based interface. It provides functionalities to:
- Add new contacts.
- Delete contacts.
- View the entire phone directory.

The program runs continuously, prompting the user for actions until terminated manually.

## Features

1. **Add Contact**: Allows the user to add a contact to the phone directory by entering a name and a phone number.
2. **Delete Contact**: Deletes a contact from the directory by name.
3. **Show Directory**: Displays the current list of contacts along with the number of entries in the directory.

## Functions

### `ph_no_add(x)`
This function allows the user to add a contact. The user is prompted to input their name and phone number, which are then stored in the phone directory dictionary.

**Parameters**: 
- `x`: The phone directory dictionary where the contact will be added.

### `ph_direct_show(x)`
This function displays the total number of contacts and all the contacts in the directory.

**Parameters**: 
- `x`: The phone directory dictionary to display.

### `no_del(x)`
This function deletes a contact from the directory based on the name entered by the user.

**Parameters**: 
- `x`: The phone directory dictionary from which a contact will be deleted.

## Usage

1. Run the script.
2. You will be greeted with a menu that allows you to perform three actions:
   - `1`: Add a contact.
   - `2`: Delete a contact.
   - `3`: Show the current directory.
3. After each action, the program will ask if you want to continue. You can either proceed with another action or close the program manually.

## Example

```
***Welcome to Directory***
Pick a number to perform an action:
1-Add
2-Delete
3-Show Directory
```

If you choose `1` (Add Contact):

```
***Welcome to the phone directory***
please enter your name to: John
please enter your phone number: 123456789
John, your name and number have been added to the directory...
```

## Requirements

- Python 3.x

## Improvements

Some potential improvements:
1. Input validation: Ensure that phone numbers are valid and names aren't duplicated.
2. Error handling: Handle cases where a user tries to delete a non-existent contact.
3. Exit option: Implement a clear way to exit the program.

---

