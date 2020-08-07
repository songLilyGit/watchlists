1  #!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #宋丽丽

import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you sercet'



