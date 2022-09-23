This is a case from Kellogg School of Management and Rady School of Management

# Case Introduction
P company decides to decrease their promotional e-mail frequency to keep good customer experience so different departments now had to coordinate their promotional e-mail activities. The analyst need to figure out which type of promotional email can generate the most benefits to the company.


# Key Idea
Since the company doesn't have time to run the experiment again, they use their historical data which can be regarded as randomly assigned.
- Each week the digital marketing department split customers with valid e-mail addresses into seven randomly assigned e-mail groups.
- Each of the seven departments was allocated one of these e-mail groups for their exclusive use during that week, subject to the e-mail frequency limit.
- The e-mails sent by each department would be designed by that department and would feature products from that department. Of course, once customers clicked on the promotional e-mail and were on the Pentathlon website they could buy products from any department or none at all.

# Data Description
- “age”: Customer age (coded in 4 buckets: “< 30”, “30 to 44”, “45 to 59”, and “>= 60”) o “gender”: Gender coded as F or M
- “income”: Income in Euros, rounded to the nearest 5,000 €
- “education”: Percentage of college graduates in the customer’s neighborhood, coded from 0-100
- “children:” Average number of children in the customer’s neighborhood
- “freq_endurance – freq_racquet”: Number of purchases in each department in the last year, excluding any purchase in response to the last email.
-  “buyer”: Did the customer click on the e-mail and complete a purchase within two days of receiving the e-mail (“yes” or “no”)?
- “total_os”: Total order size (in Euros) conditional on the customer having purchased (buyer == “yes”). This measured spending across all departments, not just the department that sent the message.
- “endurance_os – racquet_os”: Department-specific order size (in Euros). This was a breakdown of the total order size if buyer == “yes”. The value was zero for most departments because customers rarely bought products from multiple departments on a single purchase occasion.


- The team randomly picked 50,000 buyers and added 50,000 randomly sampled non-buyers. The 100,000 customers were then randomly split into a training sample (70,000 customers) and a test sample (30,000 customers).
- In addition to the 100,000 customers used for training and test, the leader asked the team to add a representative sample consisting of another 100,000 customers. This sample was representative in that it was a true random sample of the population and therefore contained the average proportion of buyers, namely 1%. This sample would be used to determine the expected benefits from using a next-product-to-buy model.
- To scale the predicted purchase probabilities for use in the representative sample, the team could use (case) weights. The formula to generate the (case) weights is shown below:
 ```pentathlon_nptb["cweight"] = rsm.ifelse(pentathlon_nptb.buyer == "yes", 1, 99)```
