### Exposed and Control 

- Exposed - contains users who are shown the smart ad.
- Control - contains user who are shown the dumy add. 

### How to target the users? 


###  Could we use the counts of yes and no answers to make a judgment on which experiment is performing better? For example if #yes > #no for the exposed group than the control group, could we declare that the ad had a significant impact Why or why not?

 - no, because we have to first check the statistical significancy of 
   the result and its practival significance
 - the result may be due to the randomization of the data, we may accidently 
   get many users in one group

### What is the statistical process that generates the data? Which kind of statistical model will you use if you were to simulate the data?

Statistical process has five steps: Designing a study, Collecting a data, Describing the data, Make inferences, Take action. 

In a designed experiment, researchers control the conditions of the study. In an observational study, researchers don’t control the conditions but only observe what happens.

There are many sampling methods used to obtain a sample from a population:

- A simple random sample (SRS) is a random selection taken from a population
- A systematic sample is every kth item in the population, beginning at a random starting point
- A cluster sample is all items in one or more randomly selected clusters, or blocks
- A stratified sample divides data into similar groups and an SRS is taken from each group
- A convenience sample is one easily obtained in a less-than-systematic way and should be avoided whenever possible

- Quantitative variables represent things that are numeric in nature, such as the value of a car or the number of students in a classroom. Categorical variables represent non-numerical data that can only be considered as labels, such as colors or brands of shoes.





### Assessment of the statistical significance of an A/B test is dependent on what kind of probability distribution the experimental data follows. Given your answer above, which statistical tests (z-test, t-test, etc.) are appropriate to use for this project?

### In classical (frequentist) A/B testing, we use p-values to measure the significance of the experimental feature (being exposed to an ad in our case)  over the null hypothesis (the hypothesis that there is no difference in brand awareness between the exposed and control groups in the current case). How are p-values computed? What information do p-values provide? What are the  type-I and type-II errors you may have in the analysis? Can you comment on which error types p-values are related?
