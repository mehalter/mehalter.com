#!/bin/bash

pandoc micah.1.md -s -t man -o micah.1

pandoc micah.1.md -s -t html -H man.css -o ../micah.1.html
