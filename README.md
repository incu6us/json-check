# Check JSON data
```sh
usage: launcher.py [-h] [-u URL] [-k KEY] [-e EXIST] [-n NOTEXIST]

JSON Check

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Full address to check
  -k KEY, --key KEY     Put the key to check a value. Can be used some keys:
                        "testkey1 testkey2"
  -e EXIST, --exist EXIST
                        Return true if exist, else - false
  -n NOTEXIST, --notexist NOTEXIST
                        Return true if not exist, else - false
```

### Examples:
output of RESTfull service:

<code>
{
    "test1": "disconnected",
    "test2": "connected",
    "test2": "connected"
}
</code>


example 1:
```sh
$ ./launcher.py -u http://example.com/rest/getSystemIdConnectionStatus/all -k test2
```
output: connected

example 2:
```sh
$ ./launcher.py -u http://example.com/rest/getSystemIdConnectionStatus/all -k "test1 test2"
```
output: disconnected connected

example 3:
```sh
$ ./launcher.py -u http://example.com/rest/getSystemIdConnectionStatus/all -k test1 -e disconnected
```
output: true

example 4:
```sh
$ ./launcher.py -u http://example.com/rest/getSystemIdConnectionStatus/all -k "test1 test2" -n disconnected
```
output: false
