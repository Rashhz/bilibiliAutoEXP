# cookie
import sys

setCookie = sys.argv[1]
cookies = dict([l.split("=", 1) for l in setCookie.split("; ")])
bili_jct = cookies['bili_jct']
SESSDATA = cookies['SESSDATA']
DedeUserID = cookies['DedeUserID']
# server酱
SCKEY = "SCT58751Tta5vXLwIrq9PQM5d0UFwIIfo"

useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"

headers = { "Content-Type": "application/x-www-form-urlencoded",
        "Cookie":"bili_jct=" + bili_jct+ "; SESSDATA=" + SESSDATA + "; DedeUserID=" + DedeUserID,
        "Referer": "https://www.bilibili.com/",
        "User-Agent": useragent}

coinnumber = 2
