"""
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
 language governing permissions and limitations under the License.
"""


from distutils import log as logger
from setuptools import Command
from subprocess import check_call
from shutil import rmtree


class bdist_docker(Command):
    """Build docker image with package and dependencies"""

    user_options = [('tag=', 't', 'docker image tag')]

    def __build_dependencies(self):
        logger.info('Making Wheels for dependencies')
        check_call(['pip3', 'wheel', '--wheel-dir', '.docker_data/wheelhouse', '.'])

    def __build_docker_image(self):
        logger.info('Building docker')
        docker_cmd = ['docker', 'build', '--pull', '--no-cache']
        if self.tag:
            docker_cmd.extend(['--tag', self.tag])
        docker_cmd.append('.')
        check_call(docker_cmd)

    def __build_wheel(self):
        logger.info('Making Wheel')
        bdist_wheel = self.reinitialize_command('bdist_wheel')
        bdist_wheel.dist_dir = '.docker_data/dist'
        self.run_command('bdist_wheel')

    def initialize_options(self):
        self.tag = None

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.__build_wheel()
            self.__build_dependencies()
            self.__build_docker_image()
        finally:
            # cleanup the docker build files
            logger.info('Cleaning up the build directory')
            rmtree('.docker_build')