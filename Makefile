clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rfv dist build *.egg-info

package:
	python -m build

release:
	twine upload dist/*
