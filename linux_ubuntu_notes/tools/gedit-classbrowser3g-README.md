gedit-classbrowser3g
====================

Class Browser for gedit

The class browser is located in the side pane and lists functions,
classes, etc. in a tree view. The default parser uses
[exuberant ctags](http://ctags.sourceforge.net/) to support a wide
range of [languages](http://ctags.sourceforge.net/languages.html).
Special parsers are used for Python, HTML, XML/Mallard/DocBook, Diff,
Ruby, Markdown and Changelogs.

This package is a fork of Class Browser Plugin
<http://www.stambouliote.de/projects/gedit_plugins.html>

gedit-classbrowser3g is for gedit versions 3.8 and above.
For older versions see the project page.

Project page: <https://launchpad.net/gedit-classbrowser3g>
Part of Gedit BC Developer Plugins: <https://launchpad.net/~gedit-bc-dev-plugins>


Ubuntu Installation
-------------------
>note by zlf:

>Test Successfully!

For Ubuntu packages are available in the official PPA.
Add `ppa:gedit-bc-dev-plugins/releases` to your system's Software Sources and
install `gedit-classbrowser3g`. You can do this in a terminal:
```shell
sudo add-apt-repository ppa:gedit-bc-dev-plugins/releases
sudo apt-get update #公司网有限制
sudo apt-get install gedit-classbrowser3g-plugin
```

More about this PPA:
<https://launchpad.net/~gedit-bc-dev-plugins/+archive/releases>

Daily builds are available in a PPA:
<https://launchpad.net/~gedit-bc-dev-plugins/+archive/daily-build>
Installation is as above but use `ppa:gedit-bc-dev-plugins/daily-build` instead.


Manual Installation
-------------------
>note by zlf:

>Test failure!

1. Install exuberant-ctags (recommended)
2. Copy the plugin to the gedit plugins folder
        cp -a classbrowser3g.plugin classbrowser3g ~/.local/share/gedit/plugins/
3. Install the gsettings schema with the following commands:
        sudo cp *.gschema.xml /usr/share/glib-2.0/schemas/
        sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
4. Open gedit and click `Edit -> Preferences -> Plugins` and activate the plugin


Feedback
--------

If you find any bugs or even just have a suggestion for an improvement then
please submit a bug report by using the web-based interface at
<https://bugs.launchpad.net/gedit-classbrowser3g/+filebug>.

If you have a question or would otherwise provide feedback, use the answer
tracker: <https://launchpad.net/gedit-classbrowser3g/+questions>


```

```