import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

import logging
from util.constant import local_headers
from util.getEncoding import getEncoding

if __name__=='__main__':
    print()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
    # with open('README.md', "r") as f:
    #     lines=f.read().replace('**','').split('---')
    #     with open('README_LIST.md','a+')as w:
    #         for i in lines[2:]:
    #             fenzu=i.split('\n\n')
    #             if len(fenzu)==5:
    #                 name=fenzu[1].split(':')
    #                 print(name[0]+'--'+':'.join(name[1:]))
    #                 w.write('|['+name[0]+']'+'('+':'.join(name[1:]).replace('\n','')+')|'+fenzu[2]+'|'+fenzu[3].replace('\n','')+'|\n')
    #             elif len(fenzu)==4:
    #                 name = fenzu[1].split(':')
    #                 print(name[0] + '--' + ':'.join(name[1:]))
    #                 w.write('|[' + name[0] + ']' + '(' + ':'.join(name[1:]).replace('\n', '').strip() + ')|' + fenzu[2] + '||\n')

        # print(lines)
        # wrongtype=[]
        # for i in lines[2:]:
        #     fenzu=i.split('\n\n')
        #     # print(fenzu)
        #     if(len(fenzu)==5):
        #         wrongtype.append(fenzu)
        #     name=fenzu[1].split(':')
        # for i in wrongtype:
        #     print(i)