import os
from flask import *
app=Flask(__name__)
from src.dbconnectionnew import *
from werkzeug.utils import *
app.secret_key="hggf"


@app.route('/')
def first():
    return render_template("index.html")



@app.route('/login_template')
def login_template():
    return render_template("login template.html")



#login function
@app.route('/login',methods=['post'])
def login():
    uname=request.form['email']
    pswd=request.form['password']
    qry="select * from login where username=%s and password=%s"
    val=(uname,pswd)
    s=selectone(qry,val)
    if s is None:
        return '''<script>alert("invalid username or password");window.location='/'</script>'''
    elif s['usertype']=="admin":
        return redirect('/homead')
    elif s['usertype']=="user":
        session['lid']=s['login_id']
        return redirect('/userhm')
    else:
        return redirect('/login')


@app.route('/homead')
def homead():
    return render_template("adminhome.html")


@app.route('/turfcourtmanage')
def turfcourtmanage():
    qry="select * from `turf/court`"
    res=selectall(qry)
    return render_template("turf and court manage.html",val=res)


@app.route('/edit',methods=['get'])
def editfacility():
    fid=request.args.get('id')
    session['fid']=fid
    q="SELECT * FROM `turf/court` WHERE `f_id`=%s"
    res=selectone(q,fid)
    return render_template("editfacility.html",val=res)


@app.route('/update',methods=['post'])
def updatefacility():
    try:
        fname = request.form['textfield']
        price = request.form['textfield2']
        description = request.form['textfield3']
        image = request.files['file']
        facility = secure_filename(image.filename)
        image.save(os.path.join('static/facility', facility))
        q="UPDATE `turf/court` SET `fname`=%s,`description`=%s,`image`=%s,`price`=%s WHERE f_id=%s"
        val=fname,description,facility,price,session['fid']
        iud(q,val)
        return '''<script>alert("updated");window.location='/turfcourtmanage'</script>'''
    except Exception as e:
        fname = request.form['textfield']
        price = request.form['textfield2']
        description = request.form['textfield3']

        q = "UPDATE `turf/court` SET `fname`=%s,`description`=%s,`price`=%s WHERE f_id=%s"
        val = fname, description, price, session['fid']
        iud(q, val)
        return '''<script>alert("updated");window.location='/turfcourtmanage'</script>'''


@app.route('/delete',methods=['get'])
def deletefacility():
    fid = request.args.get('id')
    q = "DELETE FROM `turf/court` WHERE `f_id`=%s"
    iud(q, fid)
    return '''<script>alert("deleted");window.location='/turfcourtmanage'</script>'''


@app.route('/add',methods=['post'])
def add():
    return render_template("addfacility.html")



@app.route('/addfn',methods=['post'])
def addfn():
    print(request.form)
    fname=request.form['textfield']
    price=request.form['textfield2']
    description=request.form['textfield3']
    adv=request.form['avd']
    image=request.files['file']
    facility=secure_filename(image.filename)
    image.save(os.path.join('static/facility',facility))

    qry="INSERT INTO `turf/court`  VALUES(NULL,%s,%s,%s,%s,%s)"
    val=(fname,description,facility,price,adv)
    iud(qry,val)

    return '''<script>alert("add successfully");window.location='turfcourtmanage'</script>'''



@app.route('/viewbookadm')
def viewbookadm():
    return render_template("view booking.html")

@app.route('/view_requested_package')
def view_requested_package():
    qry = "SELECT * FROM `request package` JOIN `registration` ON `request package`.`u_id`=`registration`.`login_id` AND `request package`.`status`='pending' JOIN `turf/court` ON `turf/court`.`f_id`=`request package`.`f_id`"
    res = selectall(qry)
    return render_template("viewrequestpackage.html",val=res)



@app.route('/accept_requestd_packge')
def accept_requestd_packge():
    rid = request.args.get('id')
    qry="UPDATE `request package` SET `status`='accepted' WHERE `r_id`=%s"
    iud(qry,rid)
    return '''<script>alert("Accepted");window.location='view_requested_package'</script>'''


@app.route('/reject_requestd_packge')
def reject_requestd_packge():
    rid = request.args.get('id')
    qry="UPDATE `request package` SET `status`='rejected' WHERE `r_id`=%s"
    iud(qry,rid)
    return '''<script>alert("Rejected");window.location='view_requested_package'</script>'''


@app.route('/cancelled')
def cancelled():
    return render_template("viewcancelledbooking.html")

@app.route('/feedback')
def feedback():
    return render_template("view feedback.html")

@app.route('/userhm')
def user():
    return render_template("userhome.html")


@app.route('/register')
def register():
    return render_template("register template.html")

#registration function
@app.route('/registration',methods=['post'])
def registration():
    name=request.form['fname']
    address=request.form['address']
    phone_no=request.form['phone']
    gender=request.form['gender']
    email=request.form['email']
    pswd=request.form['password']
    cnpswd= request.form['cpassword']
    if pswd==cnpswd:

        qry="insert into `login` values(null,%s,%s,'user')"
        val=(email,pswd)
        id=iud(qry,val)
        qry="insert into `registration` values(%s,null,%s,%s,%s,%s,%s)"
        val=(str(id),name,address,gender,email,phone_no)
        iud(qry,val)
        return '''<script>alert("registration successfull");window.location='/'</script>'''
    else:
        return '''<script>alert("password missmatch");window.location='/'</script>'''



@app.route('/profile')
def manageprfl():
    return render_template("profilemanagement.html")

@app.route('/facility')
def facility():
    qry = "select * from `turf/court`"
    res = selectall(qry)
    return render_template("view facility.html",val=res)


@app.route('/request')
def request1():
    qry = "select * from `turf/court`"
    res = selectall(qry)
    d = datetime.now().strftime("%Y-%m-%d")
    slts = ["6-7AM", "7-8AM", "8-9AM", "9-10AM", "10-11AM", "11-12AM", "12-1PM", "1-2PM", "2-3PM", "3-4PM", "4-5PM",
            "5-6PM", "6-7PM", "7-8PM", "8-9PM", "9-10PM", "10-11PM", "11-12AM"]

    return render_template("request package.html",val=res,d=d,s=slts)

@app.route('/rqstsnd',methods=['post'])
def rqstsnd():
    facility=request.form['select']
    slot=request.form['select2']
    from1=request.form['textfield']
    to=request.form['textfield2']

    qry1="SELECT * FROM `request package` WHERE %s BETWEEN `from` AND `to` AND `f_id`=%s AND `slot`=%s AND `status`='accepted'"
    ress = selectone(qry1,(from1,facility,slot))

    if ress is not None:
        return '''<script>alert("Slot already Booked");window.location='/request'</script>'''
    else:
        qry="INSERT INTO `request package`  VALUES(NULL,%s,%s,%s,%s,%s,%s)"
        val=(session['lid'],facility,from1,to,slot,'pending')
        iud(qry,val)
        return '''<script>alert("requested");window.location='/request'</script>'''

@app.route('/rqststatus')
def rqststatus():
    qry = "SELECT * FROM `request package` JOIN `registration` ON `request package`.`u_id`=`registration`.`login_id` JOIN `turf/court` ON `turf/court`.`f_id`=`request package`.`f_id` and `request package`.u_id=%s"
    res = selectall2(qry,session['lid'])
    return render_template("viewrequeststatus.html", val=res)




@app.route('/admin_slot_management')
def admin_slot_management():
    qry = "select * from `turf/court`"
    res = selectall(qry)
    d = datetime.now().strftime("%Y-%m-%d")
    slts = ["6-7AM", "7-8AM", "8-9AM", "9-10AM", "10-11AM", "11-12AM", "12-1PM", "1-2PM", "2-3PM", "3-4PM", "4-5PM",
            "5-6PM", "6-7PM", "7-8PM", "8-9PM", "9-10PM", "10-11PM", "11-12AM"]

    qry1="SELECT * FROM `booking`,`turf/court` WHERE `turf/court`.`f_id`=`booking`.`f_id`"
    res2=selectall(qry1)

    if res2:
        return render_template("offline users booking.html",val=res,val2=res2,d=d,s=slts)
    else:
        return render_template("offline users booking.html", val=res,d=d,s=slts,status="ok")



@app.route('/admin_slot_management_post',methods=['post'])
def admin_slot_management_post():
    slot=request.form['select2']
    bdate=request.form['boodkingdate']
    fid=request.form['select']

    res = selectone("SELECT * FROM `booking` WHERE `date`=%s AND `s_id`=%s  AND `u_id`=1",(bdate,slot))

    qry1 = "SELECT * FROM `request package` WHERE %s BETWEEN `from` AND `to` AND `f_id`=%s AND `slot`=%s AND `status`='accepted'"
    ress = selectone(qry1, (bdate, fid, slot))

    if res:
        return '''<script>alert("Booking Already Exist");window.location='/admin_slot_management'</script>'''

    else:
        if ress:
            return '''<script>alert("Booked Package Already Exist");window.location='/admin_slot_management'</script>'''
        else:
            qry = "INSERT INTO `booking` VALUES(null,%s,%s,%s,%s,%s)"
            iud(qry,(1,bdate,slot,fid,'booked'))
            return '''<script>alert("Booked");window.location='/admin_slot_management'</script>'''





@app.route('/cancel_admin_bookings')
def cancel_admin_bookings():
    id = request.args.get('id')
    qry = "delete from booking where b_id=%s"
    iud(qry,id)
    return '''<script>alert("Cancelled");window.location='/admin_slot_management'</script>'''





@app.route('/user_booking')
def user_booking():
    qry = "select * from `turf/court`"
    res = selectall(qry)
    d=datetime.now().strftime("%Y-%m-%d")
    slts=["6-7AM","7-8AM","8-9AM","9-10AM","10-11AM","11-12AM","12-1PM","1-2PM","2-3PM","3-4PM","4-5PM","5-6PM","6-7PM","7-8PM","8-9PM","9-10PM","10-11PM","11-12AM"]

    qry1="SELECT * FROM `booking`,`turf/court` WHERE `turf/court`.`f_id`=`booking`.`f_id` and booking.u_id=%s"
    res2=selectall2(qry1,session['lid'])

    if res2:
        return render_template("user_booking.html",val=res,val2=res2,s=slts,d=d)
    else:
        return render_template("user_booking.html", val=res, status="ok",s=slts,d=d)



@app.route('/user_bookingcheck',methods=['post','get'])
def user_bookingcheck():
    print(request.form)
    date=request.form['date']
    f=request.form['f']

    qry="SELECT `s_id` FROM `booking` WHERE `date`=%s AND `f_id`=%s union SELECT `slot` FROM `request package` WHERE (%s BETWEEN `from` AND `to` ) AND STATUS='accepted' AND `f_id`=%s"
    val=(date,f,date,f)
    res=selectall2(qry,val)
    lis=[]
    slts = ["6-7AM", "7-8AM", "8-9AM", "9-10AM", "10-11AM", "11-12AM", "12-1PM", "1-2PM", "2-3PM", "3-4PM", "4-5PM",
            "5-6PM", "6-7PM", "7-8PM", "8-9PM", "9-10PM", "10-11PM", "11-12AM"]

    for i in res:
        lis.append(i['s_id'])
    sslt=[]
    for i in slts:
        if i not in lis:
            sslt.append(i)
    resp = make_response(jsonify(sslt))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



@app.route('/user_requestcheck',methods=['post','get'])
def user_requestcheck():
    print(request.form)
    fdate=request.form['fdate']
    tdate=request.form['tdate']
    f=request.form['f']

    qry="SELECT `s_id` FROM `booking` WHERE `date`>=%s AND `date`<=%s AND `f_id`=%s union SELECT `slot` FROM `request package` WHERE ((%s<=`from` AND %s>=`from`) OR (%s<=`from` AND `to`<=%s) OR (`from`<=%s AND %s<=`to`) OR (%s<=`to` AND `to`<=%s)) AND `f_id`=%s and status='accepted'"
    val=(fdate,tdate,f,fdate,tdate,fdate,tdate,fdate,tdate,fdate,tdate,f)
    res=selectall2(qry,val)
    lis=[]
    slts = ["6-7AM", "7-8AM", "8-9AM", "9-10AM", "10-11AM", "11-12AM", "12-1PM", "1-2PM", "2-3PM", "3-4PM", "4-5PM",
            "5-6PM", "6-7PM", "7-8PM", "8-9PM", "9-10PM", "10-11PM", "11-12AM"]

    for i in res:
        lis.append(i['s_id'])
    sslt=["select"]
    for i in slts:
        if i not in lis:
            sslt.append(i)
    resp = make_response(jsonify(sslt))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/user_booking_post',methods=['post'])
def user_booking_post():
    slot=request.form['select2']
    bdate=request.form['boodkingdate']
    fid=request.form['select']

    res = selectone("SELECT * FROM `booking` WHERE `date`=%s AND `s_id`=%s  AND `u_id`=%s",(bdate,slot))

    qry1 = "SELECT * FROM `request package` WHERE %s BETWEEN `from` AND `to` AND `f_id`=%s AND `slot`=%s AND `status`='accepted'"
    ress = selectone(qry1, (bdate, fid, slot))

    if res:
        return '''<script>alert("Booking Already Exist");window.location='/user_booking'</script>'''

    else:
        if ress:
            return '''<script>alert("Booked Package Already Exist");window.location='/user_booking'</script>'''
        else:
            qry = "INSERT INTO `booking` VALUES(null,%s,%s,%s,%s,%s)"
            iud(qry,(session['lid'],bdate,slot,fid,'booked'))
            return '''<script>alert("Booked");window.location='/user_booking'</script>'''



@app.route('/payment',methods=['post','get'])
def payment():
    slot = request.form['select2']
    bdate = request.form['boodkingdate']
    fid = request.form['select']


    res = selectone("SELECT * FROM `turf/court` WHERE `f_id`=%s",fid)
    adamt=res['advance_amt']

    session['slot']=slot
    session['fid2']=fid
    session['date']=bdate
    session['amount'] = adamt

    return render_template('payment.html',amt=adamt)

@app.route('/bank', methods=['post'])
def bank():

    qry = "INSERT INTO `booking` VALUES(null,%s,%s,%s,%s,%s)"
    idd = iud(qry, (session['lid'], session['date'],session['slot'],session['fid2'], 'booked'))

    qry = "INSERT INTO `payment` VALUES(NULL,%s,CURDATE(),%s)"
    val = (idd, session['amount'])
    iud(qry, val)

    return '''<script>alert("Booked");window.location='/user_booking'</script>'''

    # bank=request.form['textfield']
    # ifsc = request.form['textfield1']
    # pin = request.form['textfield2']
    # acno = request.form['textfield3']
    #
    # qry = "SELECT * FROM `bank` WHERE `acno`=%s AND `ifsc`=%s AND `pin`=%s AND `bank`=%s AND `user_id`=%s"
    #
    # val = (acno,ifsc,pin,bank,session['lid'])
    #
    # res = selectone(qry,val)
    # if res is None:
    #
    #     return '''<script>alert("Invalid details");window.location="user_booking"</script>'''
    #
    # if int(res['balance'])<int(session['amount']):
    #     return '''<script>alert("Not enough balance");window.location="user_booking"</script>'''
    #
    # else:
    #
    #     bnkid = res['bank_id']
    #
    #
    #     res = selectone("SELECT * FROM `booking` WHERE `date`=%s AND `s_id`=%s  AND `u_id`=%s", ( session['date'],session['slot'],session['lid']))
    #
    #     qry1 = "SELECT * FROM `request package` WHERE %s BETWEEN `from` AND `to` AND `f_id`=%s AND `slot`=%s AND `status`='accepted'"
    #     ress = selectone(qry1, (session['date'],session['fid2'],session['slot']))
    #
    #     if res:
    #         return '''<script>alert("Booking Already Exist");window.location='/user_booking'</script>'''
    #
    #     else:
    #         if ress:
    #             return '''<script>alert("Booked Package Already Exist");window.location='/user_booking'</script>'''
    #         else:
    #             qry = "INSERT INTO `booking` VALUES(null,%s,%s,%s,%s,%s)"
    #             idd = iud(qry, (session['lid'], session['date'],session['slot'],session['fid2'], 'booked'))
    #
    #             qry = "INSERT INTO `payment` VALUES(NULL,%s,CURDATE(),%s)"
    #             val = (idd, session['amount'])
    #             iud(qry, val)
    #
    #             qry = "UPDATE `bank` SET `balance`=`balance`-%s WHERE `bank_id`=%s"
    #             val = (session['amount'], str(bnkid))
    #             iud(qry, val)
    #
    #             qry = "UPDATE `bank` SET `balance`=`balance`+%s WHERE `bank_id`=%s"
    #             val = (session['amount'], 1)
    #             iud(qry, val)
    #
    #             return '''<script>alert("Booked");window.location='/user_booking'</script>'''
    #
    #

        # qry = "INSERT INTO `booking` VALUES(NULL,%s,%s,%s,%s,'booked')"
        # val = (session['lid'],session['date'],session['slot'],session['fid2'])
        # id = iud(qry,val)


        # return '''<script>alert("Successfull");window.location="user_booking"</script>'''



@app.route("/view_facilities")
def view_facilities():
    qry ="SELECT * FROM `turf/court`"

    res = selectall(qry)
    return render_template("home_page_view_facility.html",val=res)


app.run()

