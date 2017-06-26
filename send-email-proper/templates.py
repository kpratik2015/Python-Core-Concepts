import os


def get_template_path(path):
    # using path.join() makes it work in both windows and linux platform
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path %s"%(file_path))
    return file_path


def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_context(template_string, context):
    # ** is required for passing in dictionary
    return template_string.format(**context) 

file_ = 'templates/email_message.txt'
file_html = 'templates/email_message.html'
template = get_template(file_)
template_html = get_template(file_html)
context = {
    "name": "Pratik",
    "date": None,
    "total": None
}

print(render_context(template, context))
print(render_context(template_html, context))









"""
/abc/ad/file.txt            # for linux
\hi\this\ois\a\file.txt     # for windows
open("\hi\this\ois\a\file.txt").read()
open("/abc/ad/file.txt").read()
"""
