from setuptools import setup, find_packages

setup(
    name='BrentOil-Price-Analysis',
    version='0.1.0',
    author='Adane Moges',
    author_email='adanemoges6@gmail.com',
    description='A project that analyzes how major political and economic events impact Brent oil prices.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask',
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'jupyter',
        'statsmodels',
        'pymc3',
        'requests',
        'flask-cors',
        'dash',
        'plotly',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)