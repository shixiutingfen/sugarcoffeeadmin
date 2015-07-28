# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from flask import  jsonify
import json
import urllib
import random
import os
import re
import datetime
import utils

def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    '''文件上传函数

    本函数未做上传类型判断及上传大小判断。
    '''
    result = {"err": "", "msg": {"url": "", "localfile": ""}}

    if request.method == 'POST' and 'filedata' in request.files:
        # 传统上传模式，IE浏览器使用这种模式
        fileobj = request.files['filedata']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        fileobj.save(os.path.join(app.static_folder, 'upload', rnd_name))
        result["msg"]["localfile"] = fileobj.filename
        result["msg"]["url"] = '!%s' % \
            url_for('static', filename='%s/%s' % ('upload', rnd_name))

    elif 'CONTENT_DISPOSITION' in request.headers:
        # HTML5上传模式，FIREFOX等默认使用此模式
        pattern = re.compile(r"""\s.*?\s?filename\s*=\s*['|"]?([^\s'"]+).*?""", re.I)
        _d = request.headers.get('CONTENT_DISPOSITION').encode('utf-8')
        if urllib.quote(_d).count('%25') > 0:
            _d = urllib.unquote(_d)
        filenames = pattern.findall(_d)
        if len(filenames) == 1:
            result["msg"]["localfile"] = urllib.unquote(filenames[0])
            fname, fext = os.path.splitext(filenames[0])
        img = request.data
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        with open(os.path.join(app.static_folder, 'upload', rnd_name), 'wb') as fp:
            fp.write(img)

        result["msg"]["url"] = '!%s' % \
            url_for('static', filename='%s/%s' % ('upload', rnd_name))

    return json.dumps(result)


@app.route('/uploadremote/', methods=['POST'])
def uploadremote():
    """
    xheditor保存远程图片简单实现
    URL用"|"分隔，返回的字符串也是用"|"分隔
    返回格式是字符串，不是JSON格式
    """
    localdomain_re = re.compile(r'https?:\/\/[^\/]*?(localhost:?\d*)\/', re.I)
    imageTypes = {'gif': '.gif', 'jpeg': '.jpg', 'jpg': '.jpg', 'png': '.png'}
    urlout = []
    result = ''
    srcUrl = request.form.get('urls')
    if srcUrl:
        urls = srcUrl.split('|')
        for url in urls:
            if not localdomain_re.search(url.strip()):
                downfile = urllib.urlopen(url)
                fext = imageTypes[downfile.headers.getsubtype().lower()]
                rnd_name = '%s%s' % (gen_rnd_filename(), fext)
                with open(os.path.join(app.static_folder, 'upload', rnd_name), 'wb') as fp:
                    fp.write(downfile.read())
                urlreturn = url_for('static', filename='%s/%s' % ('upload', rnd_name))
                urlout.append(urlreturn)
            else:
                urlout.append(url)
    result = '|'.join(urlout)
    return result
