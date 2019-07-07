#start- Python List
org = ['hrdept','a b ', 'ABC234', 34.5]
orgDept = org[0]
orgDetails = org[1:2]
org1 = org[1:0]
print(org,type(org),orgDept,type(orgDept),orgDetails,org1)

deptTuple = ('fin','RefID','ID34')
print(deptTuple,type(deptTuple))

injuryDesc = "this is to report the injury occured" 
injuryDesc_5 = injuryDesc[5]
print(injuryDesc,type(injuryDesc),injuryDesc_5,type(injuryDesc_5))

empIDs = {'ID1','ID2',"ID3"}
print(empIDs,type(empIDs))

depttoEmp = {'id1':'emp1','id2':'emp2',"id3":"emp3",2:"emp4"}
depttoEmp_id = depttoEmp['id1']
depttoEmp_2 = depttoEmp_id[2]
depttoEmp_3 = depttoEmp['id3']
print(depttoEmp,type(depttoEmp),depttoEmp_id,depttoEmp_2,depttoEmp_3)

#end- Python List