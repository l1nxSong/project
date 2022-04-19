#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:wgdScan
Author:wanggangdan
Copyright (c) 2019
'''
import sys
from lib.core.Spider import SpiderMain


def main():
    root = "http://www.4399.com/"
    threadNum = 10
    # spider
    wgd = SpiderMain(root, threadNum)
    wgd.craw()


if __name__ == '__main__':
    main()
