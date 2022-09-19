This is a case study from Kellogg School of Management. 

# Case Introduction
 T-company's busincess model is similar to that of Groupon, promoting discounted gift certificates that can be used at local or national retailers.
 
Chief Data Scientist decided to reevaluate how mobile campaigns were executed. In particular, she was bothered by the view in the company that the cost of pushing deals onto customers’ phones was essentially zero. However, Liu knew that the true marginal cost of each message was much higher. If customers received too many deal offers that were not relevant to them, customers could block future messages in the app, thereby preventing T-company from contacting them.

# The design of RFM
They want to use RFM analysis to understand the customer and target the customer efficiently. 
1. They have 278780 customers and offer 10% (27878) customer the deal. 
2. Then track response in each RFM cell and assess response, profitability and return on marketing expenditure per RFM cell. 
3. Finally they use the test results to determin if RFM analysis can improve profits and ROME in mobile deal targeting campaigns. 
4. If so, use the profitable RFM cells to target the remaining 250,902 customers.


# Key Assumption
1. 2.5RMB was a good approximation for the true marginal cost of sending an additional deal.
2. Fee on each deal sold is 50% of sales revenues


# Data Structure
|    userid | recency | frequency | monetary | rfm_iq_pre | buyer | ordersize | platform | category | mobile_os | training |
|----------:|--------:|----------:|---------:|-----------:|------:|----------:|---------:|---------:|----------:|---------:|
| U12617430 |     309 |         7 |     39.8 |        514 |    no |         0 |      App |        3 |   android |        1 |
| U63302737 |     297 |         8 |     39.8 |        514 |    no |         0 |  Browser |        3 |   android |        1 |
| U77095928 |     295 |         1 |     72.9 |        553 |    no |         0 |  Browser |        3 |   android |        1 |
| U43509181 |     277 |         1 |       40 |        554 |    no |         0 |  Browser |        3 |   android |        1 |
| U23195941 |     259 |         1 |       21 |        555 |    no |         0 |      App |        3 |   android |        1 |

Explanation of some key variables

| Name                | Description                                                                                        |
|---------------------|----------------------------------------------------------------------------------------------------|
| recency {integer}   | Days since last purchase (excluding the Karaoke deal offer)                                        |
| frequency {integer} | Number of deals purchased during the one-year period prior to the Karaoke deal offer               |
| monetary {float}    | Average amount spent per order (in RMB) during the one year period prior to the Karaoke deal offer |
| rfm_iq_pre {object} | Independent RFM indices                                                                            |
| ordersize {float}   | Amount spent on the Karaoke deal (in RMB)                                                                 

# Key points of this project
1. How to use different types of RFM anlysis to targeting customers
2. How to cauculate expected profit and ROME based on RFM results
3. How does RFM analysis perform in targeting customers
