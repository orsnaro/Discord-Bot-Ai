# import aiohttp
# import asyncio
# import keys
# from bs4 import BeautifulSoup

# async def clear_cookies( _session : aiohttp.ClientSession ) -> bool : 

# 	_session.cookie_jar.clear("bard.google.com")
 
# 	# Verify that the cookies have been cleared
# 	cookies = _session.cookie_jar.filter_cookies("https://bard.google.com")
# 	if cookies is None:
# 		return True
# 	else:
# 		return False

# async def logout_bard( _session : aiohttp.ClientSession  , CSRF_name : str) -> bool :
# 	# Send a request to the website to get the necessary credentials
# 	async with _session.get("https://bard.google.com/") as response:
# 		html_content = await response.text()
# 		# Parse the HTML content with BeautifulSoup
# 		soup = BeautifulSoup(html_content, "html.parser")
# 		csrf_token =soup.find("input", {"name": CSRF_name})["value"]
# 		# Send a POST request to the logout endpoint with the CSRF token
  
# 		async with _session.post("https://bard.google.com/u/logout", data={"CSRFToken": csrf_token}) as response:
# 			if response.status == 200:
# 				return True
# 			else:
# 				return False
   
# async def regenerate_cookie():
# 	# get credentials form pc (keys.py)
# 	email = keys.bardGmail
# 	password = keys.bardGmail_KEY
 
# 	async with aiohttp.ClientSession() as session:
# 		is_cleared : bool = await clear_cookies(session)

# 		try :
# 			if not is_cleared :
# 				raise Exception("Error in Wizard bot :: bard api key refresher : can't clear old bard cookies")
 
# 		finally :
# 			print("Cookies have been cleared! refreshing bark api key...")

# 		# NOTE : clearing cookies does log me out auto no need to log out
# 		# try :
# 		# 	is_logedout = await logout_bard(session , CSRF_name= "csrfmiddlewaretoken")
# 		# 	if not is_logedout :	
# 		# 		is_logedout = await logout_bard(session , CSRF_name= "CSRFToken")
# 		# 		if not is_logedout :
# 		# 			raise Exception("Error in Wizard bot :: bard api key refresher : can't logout from 'bard.google.com' in order to refresh API Key")
# 		# finally :
# 		# 	print("Logout from 'Bard' is successful")
		
  
# 		# Send a request to the server to regenerate the cookie with the new credentials
# 		async with session.post("https://accounts.google.com/signin/challenge/sl/password", data={"identifier": email, "password": password}) as response:
# 			if response.status == 200 :
# 				raise Exception("Error in Wizard bot :: bard api key refresher : couldn't refresh the api key (probably not right post request or worng cradentials)")
# 			else :
# 				pass

# 		# Extract the new cookie from the response
# 		refreshed_cookie = session.cookie_jar.filter_cookies("https://bard.google.com/").get("__Secure-1PSID").value

# 		#Close the session
# 		await session.close()
  
# 		return refreshed_cookie
		


# # Run the coroutine
# new_bard_api_key = asyncio.run(regenerate_cookie())

# with open(r"../bard_apiKey.txt" , 'w') as bardfile : 
#    bardfile.write(new_bard_api_key)

# keys.bardAPI_KEY = new_bard_api_key
# del new_bard_api_key



# import requests
# import keys
# from bs4 import BeautifulSoup

# def clear_cookies( session : requests.Session ) -> bool:

# 	# Clear the cookies for the bard.google.com domain
# 	session.cookies.clear(domain='bard.google.com')

# 	# Verify that the cookies have been cleared
# 	cookies = session.cookies.get_dict('https://bard.google.com')
# 	if cookies is None:
# 		return True
# 	else:
# 		return False

# def logout_bard():
# 	# Send a request to the website to get the necessary credentials
# 	response = requests.get('https://bard.google.com/')
# 	html_content = response.text
# 	# Parse the HTML content with BeautifulSoup
# 	soup = BeautifulSoup(html_content, 'html.parser')
# 	csrf_token = soup.find('input', {'name': 'CSRFToken'})['value']
# 	# Send a POST request to the logout endpoint with the CSRF token
# 	response = requests.post('https://bard.google.com/u/logout', data={'CSRFToken': csrf_token})
# 	if response.status_code == 200:
# 		return True
# 	else:
# 		return False

# def regenerate_cookie():
# 	# Get the credentials from keys.py
# 	email = keys.bardGmail
# 	password = keys.bardGmail_KEY

# 	# Create a requests session
# 	session = requests.Session()

# 	# Clear the cookies for the bard.google.com domain
# 	is_cleared : bool = clear_cookies(session)
# 	try :
# 		if not is_cleared :
# 			raise Exception("Error in Wizard bot :: bard api key refresher : can't clear old bard cookies")

# 		print("Cookies have been cleared! refreshing bark api key...")
# 	finally :
# 		pass

# 	# # Logout of Bard
# 	# if not logout_bard():
# 	# 	raise Exception('Error in Wizard bot :: bard api key refresher : can\'t logout from \'bard.google.com\' in order to refresh API Key')

# 	# Send a request to the server to regenerate the cookie with the new credentials
# 	response = requests.post('https://accounts.google.com/signin/challenge/sl/password', data={'identifier': email, 'password': password})
# 	if response.status_code != 200:
# 		raise Exception('Error in Wizard bot :: bard api key refresher : couldn\'t refresh the api key (probably not right post request or worng cradentials)')

# 	# Extract the new cookie from the response
# 	refreshed_cookie = session.cookies.get('https://bard.google.com/', '__Secure-1PSID')

# 	return refreshed_cookie


# # Run the coroutine
# new_bard_api_key = regenerate_cookie()

# # Save the new api key to a file
# with open('bard_apiKey.txt', 'w') as bardfile:
# 	bardfile.write(new_bard_api_key)

# # Update the bardAPI_KEY variable in keys.py
# keys.bardAPI_KEY = new_bard_api_key
# del new_bard_api_key



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keys

def regenerate_cookie():
    email = keys.bardGmail
    password = keys.bardGmail_KEY

    driver = webdriver.Chrome()

    driver.get('https://bard.google.com/')

   #  driver.delete_all_cookies()

   #  # Logout of Bard
   #  driver.find_element_by_xpath('//*[@id="u_0"]/div/div[3]/div[2]/a').click()

    # Enter the credentials and log back in
    driver.implicitly_wait(100)
    signBut = driver.find_element(by= By.LINK_TEXT , value= 'Sign in').click()
    driver.find_element(by= By.ID , value= 'identifierId').send_keys(email)
    driver.find_element(by= By.ID , value= 'identifierId').send_keys(Keys.ENTER)
    driver.find_element(by= By.NAME , value= 'Passwd').send_keys(password)
    driver.find_element(by= By.NAME , value= 'Passwd').send_keys(Keys.ENTER)

    # Get the new cookie
   #  refreshed_cookie = driver.get_cookie('__Secure-1PSID')

   #  return refreshed_cookie


# Run the coroutine
new_bard_api_key = regenerate_cookie()
print (new_bard_api_key)

# # Save the new api key to a file
# with open('bard_apiKey.txt', 'w') as bardfile:
#     bardfile.write(new_bard_api_key)

# # Update the bardAPI_KEY variable in keys.py
# keys.bardAPI_KEY = new_bard_api_key
# del new_bard_api_key