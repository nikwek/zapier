#init for test
#input = {}
#input['event'] = 'payment_success'
#input['user_id'] = 123
#input['amount'] = 3500
#input['first_name'] = 'nik'
#input['last_name'] = 'wekwerth'
#input['email'] = 'nik@librato.com'
#input['state'] = 'past_due'
#input['product_name'] = 'Production'
#end init for test
event      = input['event']
first_name = input['first_name']
last_name  = input['last_name']
email      = input['email']
amount     = 0
state      = input['state']
librato_id = input['user_id']
plan       = input['product_name']
write_key  = input['write_key']
if event == 'signup_success':
    event = "Subscription Started"
    billing_state = 'Active'
    properties = "{\"Subscription Billing Email\":\""+email+"\",\n\"Subscription Billing Name\":\""+first_name+" "+last_name+"\",\n\"Subscription Plan Type\":\"" +plan+ "\",\n\"email\":\""+email+"\"}"
elif event == 'payment_success':
    amount = float(input['amount'])/100
    event = "Subscription Billed"
    billing_state = 'Active'
    properties = "{\"revenue\":"+str(amount)+",\n\"Subscription Billing Email\":\""+email+"\",\n\"Subscription Billing Name\":\""+first_name+" "+last_name+"\",\n\"Subscription Plan Type\":\"" +plan+ "\",\n\"email\":\""+email+"\"}"
elif event == 'payment_failure':
    event = "Subscription Failed"
    billing_state = 'In Arrears'
    properties = "{\"Subscription Billing Email\":\""+email+"\",\n\"Subscription Billing Name\":\""+first_name+" "+last_name+"\",\n\"Subscription Plan Type\":\"" +plan+ "\",\n\"email\":\""+email+"\"}"
elif event == 'subscription_state_change':
    event = "Subscription State Change"
    if state == 'past_due':
        billing_state = 'Past Due'
    elif state == 'unpaid':
        billing_state = 'Unpaid'
    elif state == 'expired':
        billing_state = 'Expired Credit Card'
    elif state == 'canceled':
        billing_state = 'Canceled'
    elif state == 'active':
        billing_state = 'Active'
    else:
        billing_state = state
    properties = "{\"Subscription Billing Email\":\""+email+"\",\n\"Subscription Billing Name\":\""+first_name+" "+last_name+"\",\n\"Subscription Plan Type\":\"" +plan+ "\",\n\"email\":\""+email+"\"}"
else:
    return []
output = {'event':event,'librato_id':librato_id,'billing_state':billing_state,'properties':properties,'write_key':write_key,'email':email}