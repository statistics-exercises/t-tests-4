# Plotting the t-distribution

Hopefully, the last exercise convinced you that the test statistic we have been using:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{S_n\sqrt{n}}\sum_{i=1}^n(X_i-\mu))

is not a sample from a normal distribution.  Using an estimate of the sample variance in place of the true variance of the distribution ensures that the tails of the distribution are fatter than the tails of a Gaussian.  The statistic above is a sample from a distribution that is known as Student's t-distribution.  This distribution has one parameter n, which can take any integer value greater than 1.  Normally, this parameter is specified by giving the number of degrees of freedom for the distribution, n-1.

When n is large the t-distribution and the normal distribution are almost identical.  If we are asked to do a hypothesis tests and if we are given a lot of data points (as we were in the exercises last week) it is fine to perform tests using the methods that were introduced last were.  In other words, it is fine to use an estimate of the sample variance when computing the standard deviation.  When we are only given a small number of data points, however, this approximation is less valid and one should then use the t-distribution instead.  In the remainder of this exercise, we will thus investigate how to perform hypothesis tests using this distribution.

Unlike the other distributions that you have learned about in this course, you do not need to memorise the form of the probability density function for this distribution.  You instead need to know how to extract values for this probability density from the statistical tables.  It is also useful if you know how to exploit this function in your python programs.

With that in mind, I have written code in the panel on the left to plot the probability density function for a normal random variable with a variance of 1/3.  This distribution would be the one that the central limit theorem tells us that a sum of three standard normal random variables would be from.  __Your task is to plot a similar curve for the t-distribution with 2 degrees of freedom.__  Notice that you can extract the value of the cumulative distribution function at x for the t-distribution with `v` degrees of freedom using the python command:

````
y = scipy.stats.t.cdf( x, v )
````

To get the inverse of the cumulative distribution at y you use the following command:

````
x = scipy.stats.t.ppf( x, v )
````

and lastly to get the probability density function for this random variable at x you use: 

````
p = scipy.stats.t.pdf( x, v )
````
