
#initial state
event = input['event']
amount_value = 0
message = ""
send = "false"
subscription_state = ""
product_name = ""
first_name = str(input['first_name'])
last_name = str(input['last_name'])
email = str(input['email'])
#user_id = input['user_id'] threw an error whne there was no user_id defined
user_id = input['user_id'] if input.get('user_id') else "not found"
subscription_state = input['subscription_state']
product_name = input['product_name']
#switch statement
if event == 'signup_success':
	tail = ":hatching_chick:" if product_name == "Librato Developer" else ":hatched_chick:"
elif event == 'payment_success':
	amount_value = float(input['amount'])/100
	if amount_value >= 10000.00:
		tail = ":whale:"
	elif amount_value >= 400.00:
		tail = ":gem:"
	elif amount_value < 5.00:
		tail = ":droplet:"
	else:
		tail = ":moneybag:"
elif event == 'payment_failure':
	if subscription_state == 'unpaid':
		tail = ":fire: :fire: :fire:"
	else:
		tail = ":shit:"
elif event == 'subscription_state_change':
	revenue = float(input['total_revenue'])/100
	if subscription_state == 'canceled':
		tail = ":cry: Total Revenue: " + str(revenue) + " | Customer since: " + input['creation_date']
	elif subscription_state == 'active':
		tail = ":smiley:"
	else:
		tail = " "
elif event == 'subscription_product_change':
	previous_product = input['previous_product']
	if previous_product == 'Librato Production':
		tail = ":confused: " + previous_product + " -> " + product_name
	elif previous_product == 'Librato Developer':
		tail = ":blush: " + previous_product + " -> " + product_name
	else:
		tail = previous_product + " -> " + product_name
else:
	return []

output = [{'event': event, 'first_name': first_name, 'last_name': last_name, 'email': email, 'user_id': user_id ,'tail': tail, 'state': subscription_state, 'amount': amount_value, 'product_name': product_name}]
