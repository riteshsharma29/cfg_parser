# cfg_parser
Python based Configuration file parser to find key-value parameter or information for linux based configuration files.

#Example usage is as follows :

./cfg_parser <path-to-the-file> <parameter-OR-key-search-string> <key-value-separator>

./cfg_parser lru.cfg username :

#Linux binary can also be created by using below command (you will need pyinstaller package though) :

pyinstaller -D -F -n main -c "main.py"
