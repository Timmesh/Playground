# PACKAGES

# A package is a way of organizing related modules into a single directory structure. It provides a hierarchical structure for managing and organizing modules.
# A package is represented as a folder or directory containing a special file named __init__.py. This file can be empty, but it's required for Python to recognize the folder as a package.
# Packages can also contain sub-packages, forming a nested structure.

# Advantages of using packages:
# 1. Resolving Naming Conflicts: Packages help avoid naming conflicts by creating separate namespaces for different components.
# 2. Component Identification: Packages allow for clear identification of components by using the package name as a prefix.
# 3. Improved Modularity: Packages improve the modularity of an application by grouping related modules together.
# Directory structure:
# D:\Python_classes\
# |- test.py
# |- com\
# |  |- module1.py
# |  |- __init__.py (empty file)
# |  |- playground\
# |     |- module2.py
# |     |- __init__.py (empty file)

from com.module1 import f1
from com.playground.module2 import f2
f1()  # Hello, this is from module1 present in com
f2()  # Hello, this is from module2 present in com.playground