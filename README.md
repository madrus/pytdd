# Notes on the book

This repository contains all the example code from my book, "Test-Driven Web Development with Python", 
available at [www.obeythetestinggoat.com](http://www.obeythetestinggoat.com)

---
## Checking out code for individual chapters

Each chapter in the book has its own branch, which contains all the commits for that chapter. 
So, the state of the code in a branch is the state of the code at the *end* of that chapter.

In other words, if you want to start on a particular chapter in the book,
you should check out the code for the *previous* chapter.

So, eg, [chapter_05](https://github.com/hjwp/book-example/tree/chapter_05) has all the commits up 
to the end of chapter 5, so it's the branch to check out if you want to skip to the beginning of chapter 6.

Branches follow the syntax chapter_XX, so they're zero-padded.

Here are some [notes on this book](http://webseitz.fluxent.com/wiki/TestDrivenDevelopmentWithPython) by somebody else.

Another useful notes on [Python in VSCode](https://github.com/DonJayamanne/pythonVSCode).

---
## Chapter 1

1. deleted `accounts`, `lists` and `superlists` from the from git imported folder.
2. in `functional_tests` folder deleted everything except `__init__.py`.
2. `django-admin startproject superlists`. This has created `superlist` folder with another `superlist` subfolder.
3. copied subfolder to the root and deleted the `manage.py` inside `superlist`.
4. `python manage.py migrate`. now we are ready.
5. run a single test:
```bash
python functional_tests\functional_tests.py
```
6. run the web server:
```bash
python manage.py runserver
```
