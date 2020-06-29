#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="google-speech-addons",
    version="1.0.0",
    packages=['speech_addons'], #find_packages(),
    package_dir={"": "src"},
    test_suite="speech_addons.test",
    include_package_data=True,
    author="Victor Porton",
    author_email="porton@narod.ru",
    description="Google Text-to-Speech addons",
    long_description="Addons to Google Text-to-Speech (bypass 5000 character limit!)",
    keywords="Google text-to-speech, Google tts, 5000 character limit, max 5000 characters",
    url="https://github.com/vporton/google-speech-addons-python",
    license="GPLv3",
    classifiers=[
        "OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
)
