# distributions_tl pypi package

This package has functionality for different types of distribution frameworks. There is currently has functionality for Binomial and Guassian distributions.

Uploaded on pypi.org as part of an exercise for Udacity Machine Learning Engineer Nanodegree Program (Part 1).

**Install:**
```
pip install distributions_tl
```

[![pypi_distributions](https://user-images.githubusercontent.com/19520346/71863081-86123280-3147-11ea-933e-95d872b5aad3.PNG)](https://pypi.org/project/distributions-tl/)

## Steps to upload to pypi

1. Create all relevant files and folders
  * setup.py file
  * distributions_tl folder
    - Distribution.py
    - Binomial.py
    - Gaussian.py
    - __ init__.py (import Gaussian and Binomial)
    - license.txt (Opensource - MIT license)
    - README.md
    - setup.cfg (state name of README)

2. In terminal go to relevant folder with setup.py
```
cd Udacity_ML
```

3. Create virtual environment and activate
``` 
python -m venv ml_venv
./ml_venv/Scripts/activate
```

4. Install package locally
```
pip install .
```

5. Check it runs in python terminal ((ANS: mean 10, standard deviation 7)
```
python
from distributions_tl import Gaussian, Binomial
Gaussian(10,7)
```


6. Upload to test.pypi
```cd Udacity_ML
python setup.py sdist
pip install twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

7. Install locally and then repeat step 5
``` 
pip install --index-url https://test.pypi.org/simple/ dsnd-probability
```

8. Upload to pypi repository
```
twine upload dist/*
```

## About package

### Distribution()

**Attributes:**
- mean
- standard deviation
- list of data

**Methods:**
- read_data_file(file_name): given a file of numbers, reads in data to create list of numbers

### Binomial(Distribution)

**Attributes:**
- Distribution attributions
- probability
- size

**Methods:**
- calculate_mean(): assigns and returns the mean
- calculate_stdev(): assigns and returns the mean
- replace_stats_with_data(): assign prob, size, mean, stdev
- plot_bar(): plot bar graph of data
- pdf(k): Calculate the probability density
- plot_bar_pdf(): Plot bar graph of the pdf
- __add__(other): override +
- __repr__(): override print()

### Gaussian(Distribution)

**Attributes:**
- Distribution attributes

**Methods:**
- calculate_mean(): assigns and returns the mean
- calculate_stdev(): assigns and returns the mean
- plot_histogram(): plot histogram of data
- pdf(x): Calculate the probability density
- plot_histogram_pdf(n_spaces): Plot histogram of the pdf
- __add__(other): override +
- __repr__(): override print()
