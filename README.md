# Plugin Template

Download this repository into your ~/.FLIKA/plugins directory and modify to make a plugin for [flika](https://github.com/flika-org/flika).

# Plugin Requirements
All plugins are required to have the following files
- \_\_init__.py - Plugins are python modules and have to be imported.
- about.html - The html in this file will be displayed by flika's plugin manager.
- info.xml - This specifies plugin metadata that flika's plugin manager will use and display.

# Sample Plugins
- [Sample Plugin #1](https://github.com/flika-org/sample_plugin_1) - demonstrates how to specify dependencies, how to connect a menu to multiple functions, and how to subclass the 'BaseProcess'.
