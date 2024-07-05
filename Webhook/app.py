from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route('/trigger-call', methods=['GET', 'POST'])
def trigger_call():
    account_sid = 'ACb703786f49cb7bda37c7eadbd3eb3304'
    auth_token = 'a6b938ebf243538f07a52304a3c536b9'
    client = Client(account_sid, auth_token)

    # List of numbers to call
    numbers_to_call = ['+447702032589, '<number>']
    call_sids = []  # To store Call SIDs

    for number in numbers_to_call:
        call = client.calls.create(
                            twim='<Response><Say>"change Alert message here"</Say></Response>',
                            to=number,
                            from_='+447462227973'
                        )
        call_sids.append(call.sid)

    # Joining all the Call SIDs to return in response
    call_sids_str = ', 'join(call_sids)
    return f"Call initiated with SIDs: {call_sids_str}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
