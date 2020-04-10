sub_count = int(input_data['subscription_count'])

user = 'DZV5nJfHWY8NZN3t2ozGr3tHiOcF1PvSgYYyfSvNk0'
password = 'X'
x = int(sub_count / 50) + (sub_count % 50 > 0)
appoptics_monthly = 0
appoptics_annual = 0
appoptics_free = 0
monthly_usage = 0
custom_appoptics_monthly = 0
other = 0
for y in range(0,x):
	url = 'https://appoptics-prod.chargify.com/subscriptions.json?per_page=50&page=' + str(y+1)
	payload = requests.get(url, auth=(user, password))
	for subs in payload.json():
		if (subs['subscription']['product']['handle'] == 'appoptics-monthly' and subs['subscription']['state'] == 'active'):
			appoptics_monthly = appoptics_monthly + 1
		elif (subs['subscription']['product']['handle'] == 'appoptics-annual' and subs['subscription']['state'] == 'active'):
			appoptics_annual = appoptics_annual + 1
		elif (subs['subscription']['product']['handle'] == 'appoptics-free' and subs['subscription']['state'] == 'active'):
			appoptics_free = appoptics_free + 1
		elif (subs['subscription']['product']['handle'] == 'custom-appoptics-monthly' and subs['subscription']['state'] == 'active'):
			custom_appoptics_monthly = custom_appoptics_monthly + 1
		elif (subs['subscription']['product']['handle'] == 'monthly-usage' and subs['subscription']['state'] == 'active'):
			monthly_usage = monthly_usage + 1
		else:
			other = other + 1

output = [{'AppOptics Monthly': appoptics_monthly, 'AppOptics Annual': appoptics_annual, 'Monthly Usage': monthly_usage, 'AppOptics Free': appoptics_free, 'Custom AppOptics Monthly': custom_appoptics_monthly}]