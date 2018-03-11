var express =   require("express");  
var multer  =   require('multer');  
var app =   express();  

app.use(express.static(__dirname+'/public'));
////
var PythonShell = require('python-shell');
var pyshell = new PythonShell('JobRecommender(1).py');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});
///////
var storage =   multer.diskStorage({  
  destination: function (req, file, callback) {  
    callback(null, './uploads');  
  },  
  filename: function (req, file, callback) {  
    callback(null, file.originalname);  
  }  
});  
var upload = multer({ storage : storage}).single('myfile');  
  
app.get('/',function(req,res){  
      res.sendFile(__dirname + "/main.html");  
});

app.get('/',function(req,res){  
      res.sendFile(__dirname + "/results.html");  
});

app.post('/results.html',function(req,res){  
    upload(req,res,function(err) {  
        if(err) {  
            return res.end("Error uploading file.");  
        }  
        res.sendFile(__dirname + "/results.html");   
    });  
});  



app.listen(process.env.PORT || 2000,function(){  
    console.log("Server is running on port 2000");  
});  