{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":6,"state":"start","mode":"ace/mode/python"}},"hash":"16d5013d8203c8d661f1e5064f6c8bb799533df9","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","","","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":1}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["\"\""],"id":2}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["\""],"id":3}],[{"start":{"row":9,"column":43},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["\"\""],"id":6}],[{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["\""],"id":7}],[{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"remove","lines":["\""],"id":8},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"remove","lines":["\""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["\""]}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":["\""],"id":9},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":["\""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["\""]}]]},"timestamp":1566488183491}