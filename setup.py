from setuptools import setup

setup(name='fab-polish',
      version='1.2.0',
      description='Polish git versioned source code using Fabric',
      url='https://github.com/practo/FabPolish',
      author='J Kishore Kumar',
      author_email='kishore@practo.com',
      license='MIT',
      packages=['fabpolish'],
      install_requires=[
          'fabric3<2'
      ],
      zip_safe=False)
