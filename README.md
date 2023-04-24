# TTSSE Lab Version Conrol

This is a test repo to complete the tasks outlined for the lab on Version Control. 

This is part of Module 2 of the Techiques and Technologies for Scientific Software Engineering (TTSSE) course. The tasks are outlined bellow.

## Task 1

Create a repository. Make sure you have rudimentar LICENSE and README.md files.

The repository can be made through the github website on one's account. Both files can be created from the beginning. I have chosen the MIT lisence.

## Task 2

Create at lest one more file.

A python script with a function that prints "Hello" is created

## Task 3

Create a file .gitignore.

Anything file added to .gitignore can't be staged to be added to the repo.

## Task 4

Commit and push the above as one or more commits.

Everything was staged commited and pushed through VScode separately.

## Task 5 

Create an issue.

An issue was raised in this repository. The was done under Issues and it referred to the README file.

## Task 6

Create a branch.

A branch can be created through the CLI using the following git command:
```
git branch branch-1
```

, or through VScode under Source Control > Branch > Create Branch.

You can view all branches in the local repo by typing: 
```
git branch -a
```

## Task 7

Make further, separate changes, on both the original branch and the new branch.

Note that changes have to be staged and commited before switching branches, which can be done within VScode (bottom left). Separate scripts with functions printing "hello" were added.

## Task 8

Switch back to the original branch, make further local changes to some file, stash those changes and then merge in all changes from the other branch.

To stash changes in VScode, select the file in Source Control and click Stash > Stash. To merge be in main and then click Branch > Merge > branch-1

## Task 9

Make five further commits on one of the branches. Make at least one refer to the issue you created.

These five commits included creating a calculator script with addition, subtraction and multiplication functions, along with some comments. The README file was updated with a commit message that included "Fixes issue #1".

## Task 10

Make several separate changes in e.g. README.md and only then stage one paragraph at a time and commit these changes separately.

These task descriptions were staged separately by selectin the file to stage in Source Control, selecting the lines, right click and click "Stage Selected Ranges"