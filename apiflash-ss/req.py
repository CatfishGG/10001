from urllib.parse import urlencode
from urllib.request import urlretrieve

params = urlencode(dict(access_key="a96159e0141a452882c3550c8989a820",
                        url="https://inverse.sh"))
urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "inverse.jpeg")

# 