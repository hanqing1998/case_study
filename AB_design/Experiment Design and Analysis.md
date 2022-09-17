
# Introduction
This file contains the experiment design process.

[Pre-experiment](#pre)
 1. [Operation Funnel](#funnel)
 2. [Metrics Selection](#metric)
 3. [Sizing/Duration/Exposure](#sizing)
 
[Post-experiment](#post)

 1. [Sanity Check](#check)
 2. [Result Analysis](#result)
  - [Effect Size](#effect)
  - [Sign Tests](#sign)
  - [Summary](#summary)



# Pre-experiment <a name="pre"></a>
## Operation Funnel <a name="funnel"></a>
- Control group 
<img src="imgs/control.png" width="720" height="360">

- Treatment Group
<img src="imgs/treatment.png" width="720" height="360">

According to the pictures above, we are expected to see the number of retention users after 14 days keep the same and the number of users who access the course material increase. The main goal is to increase the user experiences and Udacity want the number of frastrated users who enrolled in the course decrease.

## Metrics Selection <a name="metric"></a>
The Introduction offers 7 metrics:

---
- Number of cookies: That is, number of unique cookies to view the course overview page. (dmin=3000)
- Number of user-ids: That is, number of users who enroll in the free trial. (dmin=50)
- Number of clicks: That is, number of unique cookies to click the "Start free trial" button (which happens before the free trial screener is trigger). (dmin=240)
- Click-through-probability: That is, number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page. (dmin=0.01)
- Gross conversion: That is, number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button. (dmin= 0.01)
- Retention: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout. (dmin=0.01)
- Net conversion: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button. (dmin= 0.0075)
---

We need to select two types of metrics, one is <b>invariant metric</b> for sanity check which is expected not to be affected by experiment and another one is evaluation metric.
Since our changes are made after users click on the 'Start free trail' button. Therefore, the metrics that are related to the user journey before reaching to this button, should remain invariant. I finally select three of them.

| No.| Invariant Metrics       |
|---|---------------------------|
| 1 | Number of cookies         |
| 2 | Number of clicks          |
| 3 | Click-through-probability |

As for the evaluation metric, I show them in the following table due to they are all related to the function we changed.

| No. |      Metrics     | Expectation |
|:---:|:----------------:|:-----------:|
|  1  | Gross conversion |   Decrease  |
|  2  |     Retention    |   Increase  |
|  3  |  Net conversion  |     Keep    |

I decide not to use Number of user-ids who enroll in the free trail because this could not tell us wheather a user get frastrated on the course and thus could help us decide the effect of the change. It can't be used as an invariant metric either because the number of users will definitely decrease because of the new function.

Gross conversion decrease means that the frastrated user decrease and the retention increase means that the left user keep in pace with the course. Both of these two metrics should be analyzed together with the net conversion. Similar net vonversion means the change doesn't affect the final revenue we earn.

## Sizing/Duration/Exposure <a name="sizing"></a>
 Next step is to decide the number of samples given alpha (0.05) and beta(0.2). We now have the baseline value for the metrics above.
 
Metric                    | Explanation                                          | Value     |
|---------------------------|------------------------------------------------------|-----------|
| Number of cookies         | Unique cookies to view course overview page per day: |     40000 |
| Number of clicks          | Unique cookies to click "Start free trial" per day:  |      3200 |
| Number of user-ids        | Enrollments per day:                                 |       660 |
| Click-through-probability | Click-through-probability on "Start free trial":     |      0.08 |
|  Gross conversion         | Probability of enrolling, given click:               |   0.20625 |
| Retention                 | Probability of payment, given enroll:                |      0.53 |
| Net conversion            | Probability of payment, given click                  | 0.1093125 |

We could use a [online sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html) to see the expected sample size for each group.

| Metrics          | Pratical Difference | Sample Size Per Group | Required Cookies who view the<br>course overview page, per group | Required Cookies  for both groups | Required Days             |
|------------------|---------------------|-----------------------|----------------------------------------------------------------|-----------------------------------|---------------------------|
| Gross conversion |                0.01 |                25,835 |                                     25835 * 40K/3.2K =322937.5 |                          645875.0 | Required cookies/40K=16.1 |
| Retention        |                0.01 |                39,115 |                                     39115 * 40K/660 =2370606.1 |                         4741212.1 |                     118.5 |
| Net conversion   |              0.0075 |                27,413 |                                     27413 * 40K/3.2K =342662.5 |                          685325.0 |                      17.1 |

After deciding the sample size, we could calculate the estimated page views required for this experiment (See the column Required Cookies for both groups, which is per group * 2 because we expect equal data in both control and treatment group). 

Since the maximum traffic for the course page is only 40K, if we use 100% traffic, the experiment duration could be calculated (See the column Required days) However, we could notice that the required days for retention is 118 days which is too long for us. Therefore, we will only keep Gross conversion and Net conversion as our evaluation metrics.

Next, we need to decide the traffic we use. If we use 100% traffic, the required time are 2-3 weeks; if we use 50% traffic, we need to extend the experiment time to 5-6 weeks.


# Post-experiment <a name="post"></a>
The experiment results could be checked at [here](https://docs.google.com/spreadsheets/d/1Mu5u9GrybDdska-ljPXyBjTpdZIUev_6i7t4LRDfXM8/edit#gid=0).
## Sanity Check <a name="check"></a>
Let's start by checking whether your invariant metrics are equivalent between the two groups.

|      Metrics      | Expected Value | Actual Value | CI Lowver Bound | CI Upper Bound | Pass or not |
|:-----------------:|:--------------:|:------------:|:---------------:|:--------------:|:-----------:|
| Number of cookies |       0.5      |    0.5006    |      0.4988     |     0.5012     |     Pass    |
|  Number of clicks |       0.5      |    0.5005    |      0.4959     |     0.5042     |     Pass    |
|   CTP Difference  |        0       |   0.0000566  |    -0.0012957   |    0.0012957   |     Pass    |

Note: Expected Value for cookies and Clicks are for control group. 
We could see that all three metrics pass the sanity check, so we could move to next step.

## Result Analysis <a name="result"></a>
### Effect Size <a name="effect"></a>
we build a confidence interval with 95% confidence level around the observed difference between the two groups, the results are shown below.

| Metric           | practical difference | Observed Difference | CI Lower Bound | CI Upper Bound | Result                                            |
|------------------|----------------------|---------------------|----------------|----------------|---------------------------------------------------|
| Gross Conversion | 0.01                 | -0.0205             | -0.0291       | -0.0120          | Satistically and Practically Significant          |
| Net Conversion   | 0.0075               | 0.0048              | -0.0116        | 0.0019         | Neither Statistically nor Practically Significant |

The gross conversion is statistically significant and pratically significant because the lower bound is still greater than the pratical difference (-0.012>-0.01). However, the net conversion is not statistically significant because the confidence inerval includes 0. 

### Sign Tests <a name="sign"></a>
Sign test is just an another method to validate the result obtained above. The sensitivity of sign test is lower than that of the above test.
|      Metrics     | Number of days Treatment>Control | P Value |      Result     |
|:----------------:|:--------------------------------:|:-------:|:---------------:|
| Gross Conversion |                 4                |  0.026  |   Significant   |
|  Net Conversion  |                10                |  0.6776 | Not Significant |

*The null hypothesis is that if control group is same as the treatment group then the probability of 'success' is 0.5. We use a two-tail p value with 5% significance level.
*[Binomial Caculator](https://www.graphpad.com/quickcalcs/binomial1.cfm)

The result is the same as effect size method. Gross Conversion decrease significantly and net conversion doesn't change significantly.

### Summary <a name="summary"></a>
Udacity wants to see whether adding a question asking students devoting time and making course type recommendation could improve user experience. They divide the pageviews into experiment group which could see the new function and control group which can't see the new function.Three metrics(Number of cookies, number of clicks and click through probability) are chosen for sanity check and three metrics (gross conversion, retention and net conversion) are selected for evaluation. 

The experiment lasts from Oct. 11th to Nov. 16th (37 days) covering 690K pageviews. Analysis revealed the invariant metrics' differences between control and treatment groups are 0 at 95% confidence level so we could move on to the result analysis. As a result, gross conversion is significant for both statistic and practical level while net conversion is not significant. Retention is not used for analysis because of the long expected experiment time.

I would recommend not launching this test. Although a decrease in gross conversion makes the number of frustrated students decreases, but we still don't have enough confidence to say how this action influences the final payment.
