- Exposed and Control 

1. Exposed - contains users who are shown the smart ad.
2. Control - contains user who are shown the dumy add. 

- How to target the users? 
  - This can be stated while designing the study. The machanism by whci we target the users may vary based on the problem. In the case of internet advertisement, users can be targeted using social media. 
  - There are several types of targeting that should be considered. When A/B testing targeting audiences, we can A/B test within one target category or two targeting categories against one another. For instance, we might test two audiences with different age demographics to see if an ad performs better with one or another.
  - Type of targeting: 
    - ***Demographic***: Demographic targeting is based on consumer attributes, such as age, gender, household income, etc. Demographic targeting is extremely easy to scale because there are a wide range of 3rd-party data providers. However, given the nature of 3rd-party data, the resulting lists won’t be nearly as accurate as 1st-party data. We typically use demographic targeting for wide-reaching branding and awareness campaigns that aren’t tied to CPA. Example: For a product like the Amazon Echo that appeals to a large demographic group, we could target fathers age 60+ vs. professional women in the 20s-30s to see which shows better potential for conversion.
    - Behavioral: Behavioral targeting identifies an audience based on specific online activity. An example would be someone searching for sneakers online. A shoe retailer can then use that cookie data to reach a user with an ad for shoes. Like demographic targeting, behavioral data is a type of 3rd-party data targeting and thus comes with the same advantages of being scalable; it’s also more accurate because we’re targeting based on a specific activity.Example: For an airline, we might want to A/B test ads on users who regularly read travel blogs vs. users who are browsing hotel sites.
    - ***Lookalike***: With lookalike targeting, we take a segment of people, such as our current customers, and target people with similar characteristics. An advantage of lookalike targeting is that if we know what resonates with a group of target customers, we can easily extend the reach to more customers who may contain a similar mindset, respond to the same types of messaging, etc. Example: A B2B company might A/B test lookalike audiences based off of current MQLs vs whitepaper downloads.
    - ***Contextual***: Contextual targeting is different than the other types of targeting we’ve covered so far because we aren’t targeting based on user characteristics or actions. With contextual targeting, we are reaching users who visit a specific site. Those sites are selected based on the category/industry or keywords associated with that site. The advantage of contextual, if done correctly, is that we will hit users who are in the right mindset and are interested in what you are offering. For instance, an airline might target vacation and destination sites because users researching places to travel are likely in the right mindset to purchase airfare. Example: Is a golf club company better off targeting customers on the PGA website as opposed to golf course websites?
    - ***Retargeting***: Retargeting allows you to target users who have visited your site. These users came to your site with interest and may have completed certain actions. Retargeting is a way to re-engage them so they move along in the funnel, or encourage them to return for a repeat purchase. Compared to other types of targeting, we tend to see much higher response and CTRs because users are already familiar with the site. The audience size we are reaching is typically much smaller with retargeting, and it’s more expensive to reach, but on the flip side, retargeting has higher conversion rates and demonstrates relatively higher ROI. Example: With retargeting, because we are targeting users who have been to your site, we wouldn’t likely A/B test within retargeting, but we could test against another targeting group to see what’s a more effective use of spend.
    - ***Search retargeting***: With search retargeting, we aim to engage users who have shown intent, but instead of targeting website visitors, we are targeting based on user search history. Example: As seen below, we could A/B test on users looking for tips for sleeping better vs. users searching for a new bed.
- Could we use the counts of yes and no answers to make a judgment on which experiment is performing better? For example if #yes > #no for the exposed group than the control group, could we declare that the ad had a significant impact Why or why not?

    - no, because we have to first check the statistical significancy of the result and its practival significance 
    - the result may be due to the randomization of the data, we may accidently get many users in one group

- What is the statistical process that generates the data? Which kind of statistical model will you use if you were to simulate the data?

- Statistical process has five steps: Designing a study, Collecting a data, Describing the data, Make inferences, Take action. 

  #### Statistical Process
  1. Design the Study

  Any scientific research should start from stating research questions:
  - Will new internet advertising increase a company’s revenue?
  - oes a newly developed vaccine prevent the spread of disease?
  - Will the new design of an online advertising increase company's brand awareness?

  ___ How can we find the answer to the research question? ___ What do we need to do? What is the population (or total collection of all individuals) under consideration? What kind of data need to be collected?

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
