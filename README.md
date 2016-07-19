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

1. created a new virtual environment and installed the necessary packages,
Django among others (`pip install -r requirements.txt`)
2. activated the virtual environment.
3. `django-admin startproject superlists`. This has created `superlist` folder with another `superlist` subfolder.
4. `cd superlists`
5. create the database: `python manage.py migrate`
6. test it's working: `python manage.py runserver`
7. `python manage.py startapp lists`
8. added `lists` to installed applications in `settings.py`
9. `mkdir func_tests`
10. `cd func_tests`
11. `touch __init__.py`
12. `python manage.py migrate`
13. `python manage.py runserver` and open `http://localhost:8000`
14. run a single test: `python func_tests\func_tests.py`
15. run unit tests: `python manage.py tests`

>***
> When refactoring, work on either the code or the tests, but not both
at once!
>***


