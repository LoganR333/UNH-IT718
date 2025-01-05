# AWS												
1.	Create an account on AWS, if needed.  It is recommended that you do NOT create an educational account as these accounts are limited in the services available and your work can not transfer to a normal account later.
2.	AWS provides a free tier. No additional credits are available.
3.	Login to the console. It is HIGHLY RECOMMENDED that you enable MFA.  Provide a screenshot in your lab report showing the console, it should look similar to this:
[Console](Lab1-AWS-console.png)
4.	Open a cloudshell and issue the following commands (replace items in **bold** with your values). 

```
aws budgets create-budget --account-id **$AWS_ACCOUNT_ID** --budget '{"BudgetName":"**DailyBudgetAlert**","BudgetLimit":{"Amount":"**0.01**","Unit":"USD"},"TimeUnit":"DAILY","BudgetType":"COST","CostFilters":{},"CostTypes":{"IncludeTax":true,"IncludeSubscription":true,"UseBlended":false}}'  --notifications-with-subscribers '[{"Notification":{"NotificationType":"ACTUAL","ComparisonOperator":"GREATER_THAN","Threshold":1.0,"ThresholdType":"PERCENTAGE","NotificationState":"ALARM"},"Subscribers":[{"SubscriptionType":"EMAIL","Address":"kmh722@unh.edu"}]}]'
```

Provide a screenshot of the command shell interaction in your lab report. FYI: you can review your budgets with:
```
aws budgets describe-budget –account **$AWS_ACCOUNT_ID** –budget-name "**name**"
```
