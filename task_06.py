#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long book."""

FHANDLER = open('war_and_peace.txt', 'r')

WORDS = FHANDLER.read()

FHANDLER.close()
# Spliting and then counting number of words in file
WORDCT = len(WORDS.split())
