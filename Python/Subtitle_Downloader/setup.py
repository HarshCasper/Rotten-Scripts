from setuptools import setup
import sys

setup(name='subtitle-downloader-python3',
      description='Python tool to download subtitles for movies/series',
      version='0.1.0',
      author='Seema Saharan',
      authorEmail='seemasaran642@gmail.com',
      entry_points={
          'console_scripts': ['subtitle-downloader-python3=subtitle_downloader_python3:main'],
      },
      url='https://github.com/seema1711/subtitle-downloader/',
      keywords=['subtitle', 'download', 'utitlity', 'movie'],
      classifiers=[
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities'
      ],
      )
