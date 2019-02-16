from flask import Blueprint, request, render_template, redirect, flash
from flask_login import login_user

from apps.user.models import Role
BLUEPRINT_ACCOUNT_KEY = 'account'
account = Blueprint(BLUEPRINT_ACCOUNT_KEY, __name__, template_folder='templates')
"""
login_user
login_out
login_required
current_user
"""


@account.route('/admin/', methods=['get', 'post'])
def admin():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.values.get('username')
        password = request.values.get('password')
        users = Role.query.filter(Role.name == username).first()
        if users:
            user = users
            if user.psw == password:
                login_user(user, remember=True)
                return redirect("http://127.0.0.1:5000/91admin/")
            else:
                flash('账号或密码有误,请重新输入!!!')
                return render_template('login.html')
        else:
            flash('用户名错误!!!')
            return render_template('login.html')
