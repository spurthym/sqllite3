import xml.etree.ElementTree as et
xm = '''<head>
          <college>
            <student id="1001">
              <name>NAME:rajesh</name>
              <bdate>D.O.B:21 dec 2000</bdate>
              <grade>GRADE:4.5</grade>
            </student>
             <student id="1002">
              <name>NAME:latha</name>
              <bdate>D.O.B:21 sept 2001</bdate>
              <grade>GRADE:4</grade>
            </student>
             <student id="1003">
              <name>NAME:sita 3</name>
              <bdate>D.O.B:21 oct 2000</bdate>
              <grade>GRADE:4</grade>
            </student>
             <student id="1004">
              <name>NAME:geetha 3</name>
              <bdate>D.O.B:31 jan 2001</bdate>
              <grade>GRADE:5</grade>
            </student>
          </college>
        </head>'''
        
obj = et.fromstring(xm)
cl = obj.findall('college/student')
for i in cl:
    print(i.find('name').text)
    print(i.find('bdate').text)
    print(i.find('grade').text)
    print()
