const express = require('express');
const bodyparser=require("body-parser");
const mongoose= require('mongoose');
const ejs = require("ejs");
const md5=require('md5');
const port = process.env.PORT || 3000;

const app = express();
app.set('view engine', 'ejs');
app.use(bodyparser.urlencoded({extended:true}));
app.use(express.static("public"));

mongoose.connect(`mongodb+srv://${process.env.user}:${process.env.pass}@cluster0.lesxr.mongodb.net/gmeetDB`, {useNewUrlParser: true, useUnifiedTopology: true});
// mongo "mongodb+srv://cluster0.lesxr.mongodb.net/myFirstDatabase" --username ritesh
const dataSchema = {
    username:String,
    password:String,
    message: String,
    date : String,
    time : String,
    link : String,
    duration: String,
    attendance: String
}

const Data = mongoose.model("Data",dataSchema);

app.get('/',(req,res)=>{
    res.render('home')
});
app.post('/',(req,res)=>{
    res.redirect('/');
})
app.post('/success',(req,res)=>{
    const date=req.body.date;
    const time=req.body.time;
    const link=req.body.link;
    const duration=req.body.duration;
    const attendance=req.body.attendance;
    const username=req.body.username;
    const password=req.body.password;
    const message=req.body.message;

    const newdata= new Data({
        username:username,
        password:password,
        message: message,
        date : date,
        time : time,
        link : link,
        duration: duration,
        attendance: attendance
    });
    newdata.save();
    res.render('success')
    // console.log(date+" "+time+" "+link+" "+duration+" "+attendance);
});


app.listen(port,() =>{
    console.log("server running");
});
