# read_access_token.py

import requests


def get_access_token(username, password):
	payload = {
	    'userName': username,
	    'password': password,
	}

	r = requests.post('https://zdaly.com/api/rest/zdaly/auth/token', data=payload)
	if r.status_code == 200:
	    response_dict = r.json()
	    accessToken = response_dict['responseEntity']['accessToken']
	    print(accessToken)
	    return accessToken
	return None

if __name__ == '__main__':
	username = 'username'
	password = 'password'
	get_access_token(username, password)
