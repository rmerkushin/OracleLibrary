# -*- encoding: utf-8 -*-

import sys, os
from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def main():
	setup(name 			= "robotframework-oraclelibrary", 
		version 		= "0.1", 
		description 	= "Oracle Database utility library for Robot Framework", 
		author 			= "Roman Merkushin", 
		author_email	= "rmerkushin@ya.ru",
		url 			= "https://github.com/rmerkushin/OracleLibrary",
		package_dir 	= { "" : "src"},
		packages		= ["OracleLibrary"]
		)
        

if __name__ == "__main__":
	main()