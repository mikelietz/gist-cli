This expects to find the following block in ~/.gitconfig to post via your account:

```
[github]
user = <your username>
password = <your password>
```

Note also that if your existing .gitconfig has tabs in there, you'll need to strip those out.

This can take a list of files, or can accept input from stdin and creates a gist (and prints the url)

Other options:

    usage: gist [-h] [--description DESCRIPTION] [--private]
                [infile_list [infile_list ...]]

    Create a github gist from a file, or from stdin

    positional arguments:
      infile_list - Not Required, if ommitted, will accept from stdin

    optional arguments:
      -h, --help            show this help message and exit
      --description DESCRIPTION, -d DESCRIPTION
      --private, -p

if you run setup.py, it will install the mkgist binary.
