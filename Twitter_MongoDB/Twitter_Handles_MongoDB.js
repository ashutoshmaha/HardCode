use new_db
show dbs   

db.createCollection('Twitter_Handles');
show collections
db.new_db.drop()
Twitter_Handles

//Insert documents:

db.Twitter_Handles.insert([  
{"Name":"Jay","Surname":"Shawn","Date_of_join":"25-03-2014",
"Date_of_Tweet":"26-09-2017","Origin_Country":"Norway","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Radha","Surname":"Madhavan","Date_of_join":"20-02-2014",
"Date_of_Tweet":"16-01-2016","Origin_Country":"India","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Shaela","Surname":"Hancock","Date_of_join":"15-06-2014",
"Date_of_Tweet":"23-06-2017","Origin_Country":"USA","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Jimmie","Surname":"Turner","Date_of_join":"29-03-2014",
"Date_of_Tweet":"15-09-2017","Origin_Country":"Germany","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Pradyumn","Surname":"Shastri","Date_of_join":"05-03-2015",
"Date_of_Tweet":"21-10-2019","Origin_Country":"France","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Donald","Surname":"Trump","Date_of_join":"06-05-2012",
"Date_of_Tweet":"11-05-2018","Origin_Country":"USA","VIP_Status":"President","Account_Status":"Not_Active"},

{"Name":"Sam","Surname":"Williams","Date_of_join":"13-04-2020",
"Date_of_Tweet":"13-04-2020","Origin_Country":"Samoa","VIP_Status":"None","Account_Status":"Active"},

{"Name":"Angela","Surname":"Markel","Date_of_join":"19-04-2017",
"Date_of_Tweet":"15-12-2017","Origin_Country":"Germany","VIP_Status":"Chancellor","Account_Status":"Active"},

{"Name":"Chris","Surname":"Thomson","Date_of_join":"20-05-2013",
"Date_of_Tweet":"25-01-2016","Origin_Country":"Switzerland","VIP_Status":"None","Account_Status":"Not_Active"},

{"Name":"Angelina","Surname":"Jones","Date_of_join":"05-12-2014",
"Date_of_Tweet":"11-05-2014","Origin_Country":"Luxembourg","VIP_Status":"None","Account_Status":"Active"}
]) 

//Find the required records using document criteria:

db.Twitter_Handles.find({VIP_Status: "President"}) 
db.Twitter_Handles.find({Origin_Country: "India"})
db.Twitter_Handles.find()  //show all documents

//Update finds the document using first parameter & updates by second parameter:

db.Twitter_Handles.update({Name:"Chris"},{$set: {Surname:"Jordan"}})  
db.Twitter_Handles.update({Name:"Radha"},{$set: {Surname:"Madhvan",Handle_Name:"Radha221"}})
db.Twitter_Handles.update({Name:"Sam"},{$set: {Handle_Name:"Sammy4018"}})
db.Twitter_Handles.update({VIP_Status:"President"},{$set: {Handle_Name:"POTUS"}})
db.Twitter_Handles.find()

//Upsert updates and inserts a document simulteneously:
db.Twitter_Handles.update({Name:"Abu"},{$set: {Surname:"AlHayek",Account_Status:"Not_Active",Handle_Name:"AlHayekAboo",Origin_Country:"UAE"}},{upsert: true})
db.Twitter_Handles.find()

//Unset removes the field
db.Twitter_Handles.update({Name:"Angelina"},{$unset: {Origin_Country: 1,Handle_Name:"Radha221"}})
db.Twitter_Handles.find()

//Remove document:
db.Twitter_Handles.remove({Name:"Shaela"})
db.Twitter_Handles.find()

//Arrays:
db.Twitter_Handles.insert({Name:"George",Surname:"Franco", Tweet_Locations: 
    [{Cuba:"Unknown", Nepal:"Kathmandu",Australia:"Perth",India:"Nainitaal",Jordan:"Unknown"},
    {China:"Xingiang",Russia:"Kremlin"}],           //Array1
    Tweet_Keywords:
    [{Day:"Travel "},{Night:"Dinner"}]
})

db.Twitter_Handles.find({Name:George},{Tweet_Locations:1})      //shows output arrays

//Sort, Skip, Limit:
db.Twitter_Handles.find({},{"Name":1, "Surname":1,"_id":0}).limit(6)  //Limits the number of fields shown for each document, removes id

db.Twitter_Handles.find({},{"Name":1, "Surname":1,"_id":0}).skip(3)  //skips the number of documents given and shows next ones

db.Twitter_Handles.find({},{"Name":1, "Surname":1,"_id":0}).skip(1).limit(5) 

db.Twitter_Handles.find({},{"Name":1, "Surname":1,"_id":0}).sort({"Name":1}) // 1=ascending, -1=descending order


//Ashutosh Mahajan, M.Sc. Web and Data Science, University of Koblenz-Landau.


