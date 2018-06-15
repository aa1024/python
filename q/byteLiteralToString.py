from qpython import qconnection


if __name__ == '__main__':
    # create connection object
    q = qconnection.QConnection(host='localhost', port=9999)
    # initialize connection
    q.open()

    print(q)

    results = q.sync('([] string 2#.z.d; `a`b)')
    results = q.sync('t:([] 2?.z.d;2?.z.t;2?`3;p:2?100.);update string d, string t, string p from t')
 
    for item in results:
         t = ()
         for x in item:
             t = t + (x.decode(),)     
         print(t)
         
    # print the objets as tuples
    r= [tuple(x.decode() for x in item) for item in results]
    print(r)

     # close connection
    q.close()
    
    
#output print(t)
#('2010.10.23', '05:25:37.694', 'cmj', '34.10485')
#('2007.08.25', '14:34:54.963', 'llm', '86.17972')

#output print(r)
#[('2010.10.23', '05:25:37.694', 'cmj', '34.10485'), ('2007.08.25', '14:34:54.963', 'llm', '86.17972')]