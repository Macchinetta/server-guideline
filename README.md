# Macchinetta Server Framework (1.x) Development Guideline

This guideline provides best practices to develop highly maintainable Web applications using full stack framework focussing on Spring Framework, Spring MVC, Spring Security and MyBatis.

This guideline helps to proceed with the software development (mainly coding) smoothly.

## Source files

Source files of this guideline are stored into following directories.

* Japanese version : `{repository root}/source/`


## Source file format

This guideline is written by the reStructuredText format(`.rst`).
About the reStructuredText format, refer to the [Sphinx documentation contents](http://sphinx-doc.org/contents.html).


## How to build

We build to HTML and PDF files using the [Sphinx](http://sphinx-doc.org/index.html).
About the Sphinx, refer to the [Sphinx documentation contents](http://sphinx-doc.org/contents.html).

### Install the Sphinx

Please install the Python and Sphinx.

* [Python](https://www.python.org/)
* [Sphinx](http://sphinx-doc.org/index.html)

> **Note: Creating PDF file**
>
> If create a PDF file, LaTeX environment is required.

### Clone a repository

Please clone a `Macchinetta/server-guideline` repository or forked your repository.

```
git clone https://github.com/Macchinetta/server-guideline.git
```

or

```
git clone https://github.com/{your account}/server-guideline.git
```

### Build HTML files

Please execute the `build-html.sh` or `build-html.bat`.
If build is successful, HTML files generate to the `{your repository}/build/html/` directory.

Linux or Mac:

```
$ cd {your repository directory}
$ ./build-html.sh
```

Windows:

```
> cd {your repository directory}
> build-html.bat
```

### Build a PDF file

Please execute the `build-pdf.sh`.
If build is successful, PDF file(`MacchinettaServerFrameworkDevelopmentGuideline.pdf`) generate to the `{your repository}/build/latex/` directory.

```
$ cd {your repository directory}
$ ./build-pdf.sh
```

## Terms of use

Terms of use refer to [here](https://github.com/Macchinetta/server-guideline/blob/master/source/Introduction/TermsOfUse.rst).
