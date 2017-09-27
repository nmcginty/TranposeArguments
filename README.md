# Tranpose Arguments
Easily Transpose arguments of functions with this Sublime Text 3 Plugin.

## Overview
For now the commands will work within parentheses

<!-- Cycle left to right transposition -->

![tranposeg](https://user-images.githubusercontent.com/16642720/30751380-31d23566-9f87-11e7-9346-b99d18deb05e.gif)

<br/> 

<!-- Random -->

![tranposerandom](https://user-images.githubusercontent.com/16642720/30754119-7e9be3ee-9f8f-11e7-9030-bd2d938425f9.gif)

## Installing

### Package Control
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Install Package`
<!-- * Search for `TransposeArguments` to see the list of available commands -->

## Keymaps

### Windows

`ctrl+alt+t`: Transpose arguments left --> right

`ctrl+shift+alt+t`: Transpose arguments right --> left 

`ctrl+alt+r`: Random Transposition


### OS X and Linux
The super keys for Linux and OS X are the Windows and command key respectively.

`super+alt+t`: Transpose arguments left --> right

`super+shift+alt+t`: Transpose arguments right --> left 

`super+alt+r`: Random Transposition

## Versioning

## Supported
`char foo(long size, (int x, int y))`: an instance like this would not be supported unless you are trying to transpose arguemnts; x & y


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* A thank to those who worked on the gist for the README :).

* The link below will take you to a great page detailing the importance of a good README. I used their template when designing the one for this plugin. 

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)