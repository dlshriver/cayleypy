from distutils.core import setup

setup(name="cayley",
	  version="0.2",
	  description="Python client for the Cayley graph database",
	  author="David Shriver",
	  author_email="davidshriver@outlook.com",
	  url="https://dlshriver.github.io/cayleypy",
	  packages=["cayley"],
	  requires=["requests"]
)
