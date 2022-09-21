import numpy as np
import pyrsm as rsm


def example():
    text = """
You just accessed a function from your first python packages!
Change the code in utils/function.py to whatever you need for this assignment
Use 'from utils import functions' to get access to your code
You can add modules to import from by adding additional .py files to the 'utils' directory
Note: If you make changes to the content of this file you will have to restart the notebook kernel to get the updates
"""
    print(text)

## a funtion for profit
def profit_actual(dat, mailto=None, intro=""):
    """
    Calculate projected performance implications from using different 
    targeting strategies

    Parameters
    ----------
    dat : Pandas DataFrame
        Pass the tuango dataset as the default value
    mailto : str
        A string with the name of the 'mailto' variable to use for calculations
    intro : str
        A string that provides an introduction to the printed output


    Returns
    -------
    nr_mail : Total number of mails that would be sent out
    mail_cost : Total cost of sending mails to selected customers (float)
    nr_responses : Total number of positive responses
    response_rate : Expressed as a proportion (no rounding)
    revenue : Total revenue in RMB (no rounding)
    ROME : Return on Marketing Expenditures expressed as a proportion (no rounding)
    profit : Total profit in RMB (no rounding)
    
    """
    dat_test = dat.query("training == 0")
     
    ## no targeting
    if mailto == None:
        nr_mail = len(dat_test)
        mail_cost = nr_mail * 1.41
        nr_responses = dat_test['res1_yes'].sum()
             
    else:
        nr_mail = (dat_test[mailto]).sum()
        mail_cost = nr_mail * 1.41
        nr_responses = dat_test[dat_test[mailto]]['res1_yes'].sum()
        

    response_rate = nr_responses/nr_mail
    revenue = nr_responses * 60
    profit = revenue - mail_cost
    ROME = profit/mail_cost
    
    
#     print(intro)
#     print( f'Total number of mails that would be sent out:{nr_mail:,.0f}' )
#     print( f'Total cost of sending mails to selected customers:{mail_cost:,.0f}' )
#     print( f'Total number of positive responses:{nr_responses:,.0f}' )
#     print( f'Total percentage of positive responses:{100 * response_rate:.2f}%' )
#     print( f'Total revenue in RMB :{revenue:,.2f}' )
#     print( f'Total profit in RMB:{profit:,.0f}' )
#     print( f'ROME:{100 * ROME:.2f}%' )

    return nr_mail, mail_cost, nr_responses, response_rate, revenue, ROME, profit

def expected_profit_wave2(dat,mailto=None):
    dat_test = dat.query("training==0")
    
    # response rate
    mail_perc = (dat_test[mailto]).sum()/len(dat_test)
    response_rate = 0.5 *((dat_test[mailto])&(dat_test['res1_yes']==1)).sum()/(dat_test[mailto]).sum()
    
    nr_mail = round(mail_perc *763334)
    mail_cost = nr_mail*1.41
    nr_responses = round(nr_mail *response_rate)
    
    revenue = nr_responses * 60
    profit = revenue - mail_cost
    ROME = profit/mail_cost    
    
    return nr_mail, mail_cost, nr_responses, response_rate, revenue, ROME, profit