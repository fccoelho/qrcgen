from setuptools import setup

setup(name='qrcgen', 
        version = '0.1', 
        author = 'Flavio Codeco Coelho', 
        author_email = 'fccoelho@gmail.com', 
        url = 'http://model-builder.sourceforge.net',
        description = 'Automated generator of Qt resource files (*.qrc), by recursive scanning of directory trees',
        zip_safe = True,
        py_modules = ['qrcgen'],
        scripts = ['qrcgen'],
        license = 'GPLv3',  
      )
