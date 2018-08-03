def request_object():
    application = request.application
    controller = request.controller
    function = request.function
    extension = request.extension
    folder = request.folder
    now = request.now
    client = request.client
    isSecure = request.is_https
    return locals()
    
def request_vars():
    num1 = 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = float(request.post_vars.num1)
        num2 = float(request.post_vars.num1)
        total = num1 + num2
    return locals()

def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    msg = arg1 + arg2
    return msg

def helloworld():
    msg = "Hello from the controller!"
    msg += "\nHow does this work?"
    return locals()

def index(): return dict(message="hello from basics.py")
