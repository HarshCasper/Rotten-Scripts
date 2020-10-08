### json parsing in bash

`find_flag.sh` script will tell you how to use [jq](https://stedolan.github.io/jq/) command to parse JSON file in bash with an example (`sample.json`)

The script will run below 3 commands and find the flag from the `sample.json` file

```bash
$ cat sample.json | jq "." | head -n 13
```

```bash
$ cat sample.json | jq ".data.allPosts.edges[0:3]"
```

```bash
$ cat sample.json | jq ".data.allPosts.edges" | grep -E -o 'RotteN{.*}' | grep -v 'harder'
```