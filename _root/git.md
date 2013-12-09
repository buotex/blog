{
  "title": "Git",
  "date": "2013-12-08",
  "categories": [
    
  ],
  "tags": [
    
  ]
}

git remote add origin git@github.com:buotex/repo
git branch --set-upstream-to=origin/<branch> master

~~~bash
Remove the three lines from .gitmodules

[submodule "vendor/plugins/cucumber"]
  path = vendor/plugins/cucumber
  url = git://github.com/cucumber/cucumber.git
Remove the two lines from .git/config

[submodule "vendor/plugins/cucumber"]
  url = git://github.com/cucumber/cucumber.git
Delete the git reference file that holds the submodule’s SHA commit id. Note the important lack of a trailing slash.

git rm --cached vendor/plugins/cucumber
Git will now see the entire directory as new files, because it’s no longer a submodule. Now you are free to delete the whole lot.

rm -rf vendor/plugins/cucumber/
~~~
