from scrapy import cmdline
import sys

arg = sys.argv[1]
cmdline.execute(("scrapy crawl "+arg).split())
