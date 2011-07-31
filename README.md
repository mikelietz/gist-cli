Though it currently doesn't use it (I hear there's a bug in urllib2), this expects to find the following block in ~/.gitconfig:

```
[github]
user = <your username>
password = <your password>
```

Note also that if your existing .gitconfig has tabs in there, you'll need to strip those out.