#Chargify to Segment integration

The Zap consists of 5 steps:

1. Webhook capture
1. Filter
1. Python code (switch based on event type)
1. Webhook for segment.identify
1. Webhook for segment.track

##Webhook capture
I created a private zap that creates a webhook url which is added 
to Chargify's webhook configuration. The payload is captured and 
passed on to the following zaps. This could be done with the Zapier
Webhook Zap but this way I could add the Chargify icon. 

##Filter
This filters for 4 Chargify events. All others are ignored. 

- signup_success
- payment_success
- payment_failure
- subscription_state_change

Anything else is ignored. 

##Python code
The [Python code](chargify_segment.py) preps 
the following steps based on the event. It sets the 
Billing State for the user, prettyfies the text, and constructs
the `properties` part of the segment.track post. 

##segment.identify webhook
The `identify` call specifies a customer identity that you can 
reference across the customer’s whole lifetime. It is used to change
customer traits. The fields are: 

- userId: required.
- traits.email: required by Hubspot.
- traits.Billing State: Sets the billing state of the user.

##segment.track webhook
The `track` method is how you record any actions your users perform.
This is a Zapier `Custom Request` webhook where you can construct the 
data in raw format. It is used to track events. The fields are:

- userID: required
- event: the Chargify event
- properties: this is contstructed in the Python code based on the event.