from setuptools import setup, find_packages

setup(
    name="bootstrap4_row",
    version="0.0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        'django-cms>=3.7.0',
    ],
)
