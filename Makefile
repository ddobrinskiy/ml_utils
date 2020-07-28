SRC = $(wildcard ./*.ipynb)

all:
	make build
	make test
	make docs

build: $(SRC)
	#####################################
	#   BUILDING NOTEBOOKS IN ./nbs/    #
	#####################################
	nbdev_build_lib
	touch ml_utils

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	#####################################
	#   RUNNING TESTS                   #
	#####################################
	nbdev_test_nbs --timing true

# editable install
pip_install:
	pip install -e .


release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
