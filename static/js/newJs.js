function Register(){
    username=document.getElementById('username').value;
    fname=document.getElementById('fname').value;
    lname=document.getElementById('lname').value;
    email=document.getElementById('username').value;
    password=document.getElementById('password').value;
    cpassword=document.getElementById('cpassword').value;

    if(!username || !fname || !lname || !email || !password || !cpassword){
        alert("Please enter the fields");
    }
    else{
        alert("Registration Successful");
    }

}

function Login(){
    name=document.getElementById('name').value
    pass=document.getElementById('pass').value
    if(!name || !pass){
        alert("Please enter the fields");
    }
    else{
        alert("Login Successful");
    }
}


function Contact(){
    email = document.getElementById('email').value;
    contact = document.getElementById('number').value;
    name = document.getElementById('name').value;
    message = document.getElementById('message').value;
    if (!email || !contact || !name || !message) {
        alert("Please fill out all fields");
    }
    else{
    alert("Message submitted successfully!");
    }
}