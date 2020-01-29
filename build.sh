#!/bin/bash

pandoc content.md --metadata pagetitle="..." --template=templates/template.tex -o resume.pdf
pandoc content.md --metadata pagetitle="..." --template=templates/template.html -o index.html
pandoc content.md --metadata pagetitle="..." --template=templates/man-template.html -o micah.1.html
pandoc content.md --metadata pagetitle="..." --template=templates/man-template.man -o micah.1
