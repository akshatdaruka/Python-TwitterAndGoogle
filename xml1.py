import xml.etree.ElementTree as ET
data='''
<person>
<name>Akshat</name>
<phone type="inH">
+123 456 789
</phone>
<email hide="yes"/>
</person>'''
tree= ET.fromstring(data)
print("Name:",tree.find('name').text)
print("Attr:",tree.find('email').get('hide'))
print("phone:",tree.find('phone').text)
