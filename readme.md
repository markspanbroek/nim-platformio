Nim for PlatformIO
==================

A plugin for [PlatformIO][2] that allows you to use the [Nim][1] programming
language for embedded development.

Installation
------------

To add Nim support to a PlatformIO project, edit `platformio.ini` and add the
following dependency:

```ini
lib_deps = 
  https://github.com/markspanbroek/nim-platformio
```

Also, make sure that [Nim][1] is installed, and that the `nim` executable is
visible on the `PATH`.

Usage
-----

Add a file `main.nim` to the `src` folder of the PlatformIO project. Write your
embedded code in this file.

Compilation of `main.nim` happens in two steps: first Nim is compiled to C++, 
and then these C++ files are compiled for your device. The intermediate C++
files are generated in the `src/nimcache` folder, so you might want to add that
folder to your `.gitignore` file.

For an example using Arduino, check out [Arduino for Nim][3].

[1]: https://nim-lang.org
[2]: https://platformio.org
[3]: https://github.com/markspanbroek/nim-arduino