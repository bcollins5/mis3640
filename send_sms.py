# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC23d8464a31c614947e7c3f8875890dbc"
auth_token = "ac5aea0a4e3b745eb7024d47f4f86bb2"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello there!", 
                                to="+12316851234",     #replace with your phone number
                                from_="12722687072")  #replace with your twilio number


print(message.sid)
