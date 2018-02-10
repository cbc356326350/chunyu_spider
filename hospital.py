from scrapy import cmdline
import sys

arg = sys.argv[0]
cmdline.execute(("scrapy crawl "+arg).split())
