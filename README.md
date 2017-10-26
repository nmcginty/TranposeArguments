# Tranpose Arguments
Easily Transpose arguments of functions with this Sublime Text 3 Plugin.

## Overview
For now the commands will work within parentheses

<!-- Cycle left to right transposition -->

![tranposeg](https://user-images.githubusercontent.com/16642720/30751380-31d23566-9f87-11e7-9346-b99d18deb05e.gif)

<br/> 

<!-- Random -->

![tranposerandom](https://user-images.githubusercontent.com/16642720/30754119-7e9be3ee-9f8f-11e7-9030-bd2d938425f9.gif)

<!-- Select All Arguments -->

![selectall](https://user-images.githubusercontent.com/16642720/32073427-ff610006-ba63-11e7-984b-942f5a419c1e.gif)

## Installing

### Package Control
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Install Package`
<!-- * Search for `TransposeArguments` to see the list of available commands -->

## Keymaps

* Please download the  **MarkAndMove** to enable the `Select All Args` - [MarkAndMove](https://github.com/colinta/SublimeMarkAndMove)

* This can easily be downloaded from `Package Control`. Just search for MarkAndMove.

* Along with this make sure to set the `mark_and_move_do_it_all` command in your personal key bindings. 
* `Sublime Tool Bar --> Prefences --> Key Bindings`.

* I have mine set as `ctrl+alt+m`. This can whatever you like just make sure whatever you decide doesn't conflict with another command.

### Windows

`ctrl+alt+t`: Transpose arguments left --> right

`ctrl+shift+alt+t`: Transpose arguments right --> left 

`ctrl+alt+r`: Random Transposition

`ctrl+alt+a`: Select All Arguments --> need to download special package for this


### OS X and Linux
The super keys for Linux and OS X are the Windows and command key respectively.

`super+alt+t`: Transpose arguments left --> right

`super+shift+alt+t`: Transpose arguments right --> left 

`super+alt+r`: Random Transposition

`super+alt+a`: Select All Arguments --> need to download special package for this

<!-- ## Versioning -->

## Supported
`char foo(long size, (int x, int y))`: an instance like this would not be supported unless you are trying to transpose arguments; x & y


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The link below will take you to a great page detailing the importance of a good README. I used their template when designing the one for this plugin. 

* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)