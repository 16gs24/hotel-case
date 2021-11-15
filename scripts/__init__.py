from scipy.stats import ttest_ind
import pandas as pd

def test_financial_metrics(dataset, metric):
    '''
Split the dataset to test & control and calculate the lift within the group

keyword arguments:
    dataset -- dataframe with a thank you status column with values of strings 'thank_you_call' or 'no_call'
    metric -- column to calculate the t test on
    '''
    #split data
    thank_you_call = dataset[dataset.THANK_YOU_STATUS == 'thank_you_call']
    no_call = dataset[dataset.THANK_YOU_STATUS == 'no_call']

    # test & report
    ttest_results = ttest_ind(a=thank_you_call[metric],b=no_call[metric])
    financial_metric_average = dataset[dataset.THANK_YOU_STATUS == 'thank_you_call'][metric].mean()
    control_financial_metric_average = dataset[dataset.THANK_YOU_STATUS == 'no_call'][metric].mean()
    delta = financial_metric_average - control_financial_metric_average
    lift = delta / control_financial_metric_average

    print(f'Campaign lift of ${delta} ({100*lift:.2}%) vs ${control_financial_metric_average} baseline with p {ttest_results[1]}')

    return lift, financial_metric_average, control_financial_metric_average

if __name__ == '__main__':
    #TODO: put this into a unit test folder
    test_data = {'THANK_YOU_STATUS': ['thank_you_call','thank_you_call','no_call','no_call'],
    'GMV': [100,100,1,1]
    }

    test_df = pd.DataFrame(data = test_data)
    lift, test, control = test_financial_metrics(test_df,'GMV')
    assert lift == 99
    #assert test_financial_metrics(test_df,'GMV') == (100,100,0)