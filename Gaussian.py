import math
import matplotlib.pyplot as plt

from .Distribution import Distribution

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
      Distribution.__init__(self, mu, sigma)
    

    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.
       
        Returns: 
            float: mean of the data set  
        """     
        self.mean = sum(self.data) / len(self.data)
        return self.mean
                

    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
          1. Check whether the data is a sample to determine number of entries
          2. For each result, subtract the mean and square the results
          3. Then mean for those squared differences
          4. Take the square root
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """
        # Step 1
        if sample:
          n = len(self.data) - 1
        else: 
          n = len(self.data)

        # Step 2
        sigma = 0
        mean = self.calculate_mean()
        for d in self.data:
          sigma += (d - mean) ** 2
  
        #Step 3 and 4
        self.stdev = math.sqrt(sigma / n)

        return self.stdev    
        
    
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title("Histogram of Data")
        plt.xlabel("Data")
        plt.ylabel("Count")
          
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        variance = self.stdev ** 2

        a = (1 / math.sqrt(2*math.pi*variance)) 
        b = math.exp(-((x - self.mean)**2) / variance * 2)
        return  a * b 

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        # TODO: Nothing to do for this method. Try it out and see how it works.
        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):        
        """Magic method to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        result = Gaussian()
        # calculate mean and stdev of summing together and return
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
        return result 
        
    def __repr__(self):    
        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian        
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

