qry="select * from `turf/court`"
    res=selectall(qry)
    return render_template("turf and court manage.html",val=res)
