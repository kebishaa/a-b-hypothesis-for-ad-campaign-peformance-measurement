<<<<<<< HEAD
# Introduction #
This technical project titled “A/B Hypothesis Testing: Ad campaign performance” aims to help an advertising company (SmartAd) to assess its additional service called Brand Impact Optimizer (BIO). Actually, the BIO service is provided to quantify the increase in brand awareness as a result of the ads it shows to online users. Two groups of users have been made: users who have been shown a dummy ad (controlled group) and users who have been shown a creative (ad) that was designed for the client (exposed group). The overall objective of this project is then to compare the two groups using the brand awareness metric (knowing or not the brand Lux) in order to figure out which one of them performs better. This goal will be reached by testing if the ads that the advertising company runs resulted in a significant lift in brand awareness using A/B testing on the two groups of users. This interim report aims to go through the understanding of the A/B testing framework. In order to do this, different points in the form of questions will be addressed and answered.

# Which online users belong to the control and exposed groups? #
Users in the controlled groups are those who have been shown a dummy ad and users in the exposed group are those who have been shown an ad designed for the client.

# How are the users targeted? #
The users are randomly targeted to be shown a dummy ad or proper ad and then to be presented the BIO (a lightweight questionnaire).

# What is the best way to make a judgment on which experiment is performing better? #
Some might think about using the counts of yes and no answers to make a judgment on which experiment is performing better? But, doing that will lead to a wrong conclusion (we could not declare that the ad had a significant impact) because the data are from a sample, not collected on the entire population of the users (this being even impossible). Then, the counts findings for a given sample will be different for another sample: we can get two opposite answers. Then, the objective is to draw a conclusion which is likely to be true for the whole population. Hence, a significance test is definitely needed to test the difference in the entire population from which the sample is made based on the results of the sample.

# What’s the statistical process that generates the data? - Which statistical model could be used to generate those data using simulation? #
The data is actually a “Yes” and “No” response of online users to the question (Do you know the brand Lux?). The outcome (response) of each user could not be known in advance and has two possible values: 1 (yes) or 0 (no). This is then a Bernoulli trial for each user. Hence, for all the users (being independent), we have a Binomial trial which is a Bernoulli process. Then, one can say that a Bernoulli process has been used for generating the data. Consequently, a Binomial distribution can be used to simulate the data.

# Which statistical tests are appropriate to use for this project? #
Using the central limit theorem, a binomial distribution can be approximated by a normal distribution. Then, a z-test can be used for the test.

# P-values, type I and type II errors #
A p-value quantifies how likely it is to erroneously reject a specific statistical hypothesis, were it true, based on a given set of data. p-values can then be calculated based on the cumulative distribution function (CDFs) of the statistics used for the test. 
Basically, in statistics, a Type I error is a false positive conclusion (rejecting the null hypothesis when it is true, while a Type II error is a false negative conclusion (failing to reject the null hypothesis when it is false). Note that by definition, p-values are related to type I errors.

# How does the classical A/B testing using the z-score framework work? #
The classical A/B using the z-score framework uses the approximation of the distribution of X (here binomial) to a normal distribution to test whether the difference in the conversion rate between the two groups is 0 or not. The approximation statistic test is used to compute the z-score (observed value of the statistic) which in turn is used to calculate the p-value to draw a conclusion.

# How does sequential A/B testing work? #
Unlike the classical A/B testing which requires data collection to be completed and requires a large sample size for reliable conclusions, the sequential sampling works in a very non-traditional way. Instead of a fixed sample size, one chooses one item (or a few) at a time, and then tests his hypothesis. The conclusion can result in either:
- Rejecting the null hypothesis (H0) in favor of the alternate hypothesis (H1) and stop,
- Keep the null hypothesis and stop,
- unable to reach either conclusion with current observation and continue sampling.

# What are some of the advantages of sequential A/B testing? # 
Some advantages of sequential A/B testing over the classical A/B testing:
- optimize necessary observation (sample size)
- reduce the likelihood of error
- gives a chance to finish experiments earlier without increasing the possibility of false results
 
# How is A/B testing done using machine learning? #
The problem in statistical A/B testing which leads to the use of machine learning is that user behavior is vastly more complex than just the two variables used to compare the controlled and exposed group. Differences between users can come from many other factors. Then, the machine learning approach enables modeling complex systems that include all of the ongoing events, user features, and more. There are a number of algorithms that can be used, each with strengths and weaknesses. Those models/algorithms are used to determine the relevant features which can explain the difference between the controlled and the exposed group.
 
# What are the pros and cons of using Machine learning to perform A/B testing? #
The most important advantage of using machine learning to perform A/B testing is especially that with machine learning one can incorporate the complexity and dynamic nature of data and draw insights, which is not possible when using classical A/B testing. Cons of using Machine learning might be the challenge in finding the best model to use to fit the data.

# Problem formulation for machine learning and target variable #
The target variable, here, is the response to the question: Do you know the brand Lux? Only users who have responded will be considered. The possible values are 0 or 1 associated with yes or no. Problem formulation: What are the relevant features that determine the conversion in brand awareness?

=======
- Exposed and Control 

1. Exposed - contains users who are shown the smart ad.
2. Control - contains user who are shown the dumy ad. 

- How to target the users? 
  - You can target your A/B tests to users based on specific behavior, attribute, or event. 
  - There are several types of targeting that should be considered. When A/B testing targeting audiences, we can A/B test within one target category or two targeting categories against one another. For instance, we might test two audiences with different age demographics to see if an ad performs better with one or another.
  - Type of targeting [here](https://www.3qdept.com/blog/display-targeting-fundamentals-ab-test-determine-ideal-audience/): 
    - ***Demographic***: Demographic targeting is based on consumer attributes, such as age, gender, household income, etc. Demographic targeting is extremely easy to scale because there are a wide range of 3rd-party data providers. However, given the nature of 3rd-party data, the resulting lists won’t be nearly as accurate as 1st-party data. We typically use demographic targeting for wide-reaching branding and awareness campaigns that aren’t tied to CPA. Example: For a product like the Amazon Echo that appeals to a large demographic group, we could target fathers age 60+ vs. professional women in the 20s-30s to see which shows better potential for conversion.
    - ***Behavioral***: Behavioral targeting identifies an audience based on specific online activity. An example would be someone searching for sneakers online. A shoe retailer can then use that cookie data to reach a user with an ad for shoes. Like demographic targeting, behavioral data is a type of 3rd-party data targeting and thus comes with the same advantages of being scalable; it’s also more accurate because we’re targeting based on a specific activity.Example: For an airline, we might want to A/B test ads on users who regularly read travel blogs vs. users who are browsing hotel sites.
    - ***Lookalike***: With lookalike targeting, we take a segment of people, such as our current customers, and target people with similar characteristics. An advantage of lookalike targeting is that if we know what resonates with a group of target customers, we can easily extend the reach to more customers who may contain a similar mindset, respond to the same types of messaging, etc. Example: A B2B company might A/B test lookalike audiences based off of current MQLs vs whitepaper downloads.
    - ***Contextual***: Contextual targeting is different than the other types of targeting we’ve covered so far because we aren’t targeting based on user characteristics or actions. With contextual targeting, we are reaching users who visit a specific site. Those sites are selected based on the category/industry or keywords associated with that site. The advantage of contextual, if done correctly, is that we will hit users who are in the right mindset and are interested in what you are offering. For instance, an airline might target vacation and destination sites because users researching places to travel are likely in the right mindset to purchase airfare. Example: Is a golf club company better off targeting customers on the PGA website as opposed to golf course websites?
    - ***Retargeting***: Retargeting allows you to target users who have visited your site. These users came to your site with interest and may have completed certain actions. Retargeting is a way to re-engage them so they move along in the funnel, or encourage them to return for a repeat purchase. Compared to other types of targeting, we tend to see much higher response and CTRs because users are already familiar with the site. The audience size we are reaching is typically much smaller with retargeting, and it’s more expensive to reach, but on the flip side, retargeting has higher conversion rates and demonstrates relatively higher ROI. Example: With retargeting, because we are targeting users who have been to your site, we wouldn’t likely A/B test within retargeting, but we could test against another targeting group to see what’s a more effective use of spend.
    - ***Search retargeting***: With search retargeting, we aim to engage users who have shown intent, but instead of targeting website visitors, we are targeting based on user search history. Example: As seen below, we could A/B test on users looking for tips for sleeping better vs. users searching for a new bed.
- Could we use the counts of yes and no answers to make a judgment on which experiment is performing better? For example if #yes > #no for the exposed group than the control group, could we declare that the ad had a significant impact Why or why not?

    - no, because we have to first check the statistical significancy of the result and its practival significance 
    - the result may be due to the randomization of the data, we may accidently get many users in one group

- What is the statistical process that generates the data? Which kind of statistical model will you use if you were to simulate the data?

- Statistical process has five steps: Designing a study, Collecting a data, Describing the data, Make inferences, Take action. 

  #### Statistical Process [here](https://byuistats.github.io/BYUI_M221_Book/Lesson02.html#:~:text=The%20Statistical%20Process%20has%20five,but%20only%20observe%20what%20happens.)
  1. Design the Study

  Any scientific research should start from stating research questions:
  - Will new internet advertising increase a company’s revenue?
  - oes a newly developed vaccine prevent the spread of disease?
  - Will the new design of an online advertising increase company's brand awareness?

  ___How can we find the answer to the research question? What do we need to do? What is the population (or total collection of all individuals) under consideration? What kind of data need to be collected?___

  The output of this step is a hypothesis. A hypothesis is a statement such as the following:
  - Using new internet advertising will increase the company’s sales revenue.
  - A newly-developed vaccine is effective at preventing tuberculosis.
  - The newly designed advertising can increase company's brand awareness. 

  2. Collect the  Data

  When designing a study, much attention is given to the process by which data are observed. When examining data, it is also important to understand the data collection procedures. A sample is a subset (a portion) of a population. How is this sample obtained? How are the observations made?

  There are many sampling methods used to obtain a sample from a population:

  - A simple random sample (SRS) is a random selection taken from a population
  - A systematic sample is every kth item in the population, beginning at a random starting point
  - A cluster sample is all items in one or more randomly selected clusters, or blocks
  - A stratified sample divides data into similar groups and an SRS is taken from each group
  - A convenience sample is one easily obtained in a less-than-systematic way and should be avoided whenever possible

  3. Describe the Data

  - When we describe data, we use any tools appropriate to the situation. This can include creating graphs or calculating statistics to help understand or visualize the data.

  4. Make Inferences

  - Inference is the process of using the information contained in a sample from a population to make a general statement (i.e. to infer something) about the entire population. Later in the course we will learn techniques that make this type of analysis possible.

  5. Take Action

  - The goal of a statistical analysis is to determine which action to take in a particular situation. Actions can include many things: launching an internet ad campaign (or not), expressing gratitude (or not), getting vaccinated (or not), etc.

- Assessment of the statistical significance of an A/B test is dependent on what kind of probability distribution the experimental data follows. Given your answer above, which statistical tests (z-test, t-test, etc.) are appropriate to use for this project?


- In classical (frequentist) A/B testing, we use p-values to measure the significance of the experimental feature (being exposed to an ad in our case)  over the null hypothesis (the hypothesis that there is no difference in brand awareness between the exposed and control groups in the current case). How are p-values computed? What information do p-values provide? What are the  type-I and type-II errors you may have in the analysis? Can you comment on which error types p-values are related?
>>>>>>> main
