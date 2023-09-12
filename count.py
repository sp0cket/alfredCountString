#coding=utf-8

import sys
import json

args = sys.argv[1]
result = {
        "items": [
            {
                "type": "file",
                "title": '这个字符串包含 {} 个字符'.format(len(args)),
                "subtitle": "复制到剪贴板",
                "arg": len(args),
            }
        ]}
finalResult = json.dumps(result)

print(finalResult)
