# :snake: Multi Site Python Crawler

Doercity Project ID: 1004

## Problem Statement

You need to develop a multi site python crawler using scrapy (https://scrapy.org/). Input to your program will be (any) Website. You need to scrap the site  recursively for all the pages/subpages in the site. The program should also be able to scrap indic fonts (like Hindi, Kannada, Tamil etc.). You need to use Python 3 for developing this crawler.

## Submission Requirements

[x] Write a program in Python 3 that will recursively crawl all the pages/sub pages of a given website.

[x] Program is able to scrap indic fonts (like Hindi, Kannada, Tamil etc.)

[x] Generate Log File. The log file lists all the pages/sub pages that the program has crawled.

[x] For every Page/Sub Page that the program crawls, the output should be recorded in JSON format as described below:

### Output Format

``` json
{

  "pages": [

    {

      "page": "https://domainname.com/homepage.cms",

      "content": "all the <p> tag values of the page"

    },

    {

      "page": "https://domainname.com/subpage/news.cms",

      "content": "all the <p> tag values of the page"

    },

    .
    .
    .
  ]
}
```

#### Notes:

1. _content_ is string of space seperated and concatenated &lt;p> tag values

---

## Usage

``` shell
crawler.py [-h] [-o --output] url

positional arguments:
  url          url to start crawling from

optional arguments:
  -h, --help   show this help message and exit
  -o --output  specify output file; will be generated if does not exist, will
               truncate previous data if exists
```

If arg `--output` is not specified, program will generate `log.json` to save output.

## Example

``` shell
python crawler.py http://example.com -o example_log.json
```

Program will crawl `http://wxample.com` recursively and generate output in `example_log.json`.

---

**Important** (for pip users): Follow this link (https://superuser.com/questions/1179925/installing-twisted-on-python-3-5-and-virtualenv-using-pip) to install `twisted`(_scrapy dependency_) on Windows.