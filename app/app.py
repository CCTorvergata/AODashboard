import os

from flask import Flask, render_template

vulnbox_ip = os.environ.get("VULNBOX_IP", "")
vulnbox_password = os.environ.get("VULNBOX_PASSWORD", "")
gameserver_ip = os.environ.get("GAMESERVER_IP", "")
sysadmin_ip = os.environ.get("SYSADMIN_IP", "")
firegex_password = os.environ.get("FIREGEX_PASSWORD", "")
flagwarehouse_password = os.environ.get("FLAGWAREHOUSE_PASSWORD", "")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           vulnbox_ip=vulnbox_ip,
                           vulnbox_password=vulnbox_password,
                           gameserver_ip=gameserver_ip,
                           sysadmin_ip=sysadmin_ip,
                           firegex_password=firegex_password,
                           flagwarehouse_password=flagwarehouse_password)


if __name__ == '__main__':
    app.run(debug=True)
