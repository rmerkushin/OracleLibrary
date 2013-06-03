# -*- encoding: utf-8 -*-

import sys, os
from distutils.core import setup
from OracleLibrary import __version__

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def main():
	setup(name 			= "robotframework-oraclelibrary", 
		version 		= __version__, 
		description 	= "Oracle Database utility library for Robot Framework", 
		author 			= "Roman Merkushin", 
		author_email	= "rmerkushin@ya.ru",
		url 			= "https://github.com/rmerkushin/OracleLibrary",
		package_dir 	= { "" : "src"},
		packages		= ["OracleLibrary"]
		)
        

if __name__ == "__main__":
	main()