from setuptools import find_packages,setup
def get_requirements(file_path:str)->list[str]:
    from typing import List
    '''this function will return a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='gazal',
        author_email='gazal15092005@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt')
    )
