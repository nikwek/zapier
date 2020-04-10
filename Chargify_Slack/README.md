#Chargify to Slack Integration

This integration consists of 4 steps:

1. Chargify private zap
1. Filter
1. Python code
1. Slack Zap

##Chargify private zap
This is a private Chargify zap that is basically just a webhook. It creats
a URL that we use in the Chargify webhook. 

##Filter
The filter checks for 4 Chargify events:

- signup_success
- payment_success
- payment_failure
- subscription_state_change

Everything else is ignored. 

##Run Python
The [Python code](chargify_slack.py) is a switch statement that checks for 
the Chargify event and then constructs elements of the Slack message 
based on the event. These elements are passed on to the Slack Zap.

##Slack Zap
POSTs a message to the #Chargify channel in Slack with the Chargify event. 
