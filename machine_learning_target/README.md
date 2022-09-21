This is a case study from Rady School of Management and company Intuit

# Case Introduction
The key event, the release of version 3 of the QuickBooks software, takes place in 1995. Although ecommerce was already feasible in 1991, at the time of the case, QuickBooks products could only be purchased through Intuit Direct (i.e., delivery by mail) or through “brick-and-mortar” retailers like Best Buy.
 
The intuit75.pkl file contains data on 75,000 (small) businesses selected randomly from the 801,821 that were sent the wave-1 mailing.1 The mailing contained an offer to upgrade to the latest version of the QuickBooks software.

Variable “res1” denotes which of these businesses responded to the mailing by purchasing QuickBooks version 3.0 from Intuit Direct. Use the available data to predict which businesses that did not respond to the wave-1 mailing, are most likely to respond to the wave-2 mailing. 

# Key Assumption
- Assume each mail piece costs $1.41 and that the margin (or net revenue) from each responder, excluding the mailing cost, is $60. 
- Usual practice would be to assume a 50 percent drop off in response from wave-1 to wave-2, which means every response probability in wave-2 is only 50% of the response probability we predict for that business based on the wave-1 response data.

# Data Description
| Variable   | Type      | Description                                                                                                                |
|------------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| id         | integer   | Small business customer ID                                                                                                 |
| zip        | character | 5-Digit ZIP Code (00000 = unknown, 99999 = international ZIPs).                                                            |
| zip_bins   | integer   | Zip-code bins (20 approximately equal sized bins from lowest to highest zip code number)                                   |
| sex        | factor    | “Female”, “Male”, or “Unknown.”                                                                                            |
| bizflag    | integer   | Business Flag. Address contains a Business name (1=yes, 0=no or unknown).                                                  |
| numords    | integer   | Number of orders from Intuit Direct in the previous 36 months                                                              |
| dollars    | numeric   | Total $ ordered from Intuit Direct in the previous 36 months                                                               |
| last       | integer   | Time (in months) since last order from Intuit Direct in the previous 36 months                                             |
| sincepurch | integer   | Time (in months) since original (not upgrade) Quickbooks purchase                                                          |
| version1   | integer   | Is 1 if the customer's current Quickbooks is version 1, 0 if version 2                                                     |
| owntaxprod | integer   | Is 1 if the customer purchased tax software, 0 otherwise                                                                   |
| upgraded   | integer   | Is 1 if customer upgraded from Quickbooks version 1 to version 2 Response to wave-1 mailing (“Yes” if responded else “No”) |
| res1       | factor    | 70/30 split, 1 for training sample, 0 for test set                                                                         |
