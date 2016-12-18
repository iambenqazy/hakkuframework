#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os
import sys

def main():
	path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/"
	return path

def modules():
	path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/modules/"
	return path

def core():
	path = os.path.dirname(os.path.abspath(__file__)) + "/"
	return path

def lib():
	path = os.path.dirname(os.path.abspath(__file__)) + "/lib/"
	return path

def tools():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tools/"
	return path

def conf():
	path = os.path.dirname(os.path.abspath(__file__)) + "/conf/"
	return path

def tmp():
	path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/core/tmp/"
	return path
