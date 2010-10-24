# -*- coding: utf-8 -*- 

response.title = T('web2py Enterprise Web Framework')
response.keywords = T('web2py, Python, Enterprise Web Framework')
response.description = T('web2py Enterprise Web Framework')

session.forget()

@cache('index')
def index():
    return response.render()
    
@cache('what')
def what():
    return response.render()
      
@cache('download')
def download():
    return response.render()
     
@cache('who')
def who():
    return response.render()

@cache('support')
def support():
    return response.render()
    
@cache('documentation')
def documentation():
    return response.render()

@cache('usergroups')
def usergroups():
    return response.render()

def contact():
    redirect(URL('default','usergroups'))

@cache('videos')
def videos():   
    return response.render()
    
def security():
    redirect('http://www.web2py.com/book/default/chapter/01#security')

def api():
    redirect('http://web2py.com/book/default/chapter/04#API')

@cache('license')
def license():
    import os
    filename = os.path.join(request.env.web2py_path,'LICENSE')
    return response.render(dict(license=MARKMIN(open(filename,'r').read())))

def version():
    return request.env.web2py_version

@cache('examples')
def examples():
    return response.render()

@cache('changelog')
def changelog():
    import os
    filename = os.path.join(request.env.web2py_path,'README')
    return response.render(dict(changelog=MARKMIN(open(filename,'r').read())))
