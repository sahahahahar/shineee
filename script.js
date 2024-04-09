function send(event){
    event.preventDefault();
    const name = document.getElementById('username').value;
    const mail = document.getElementById('useremail').value;

    fetch("http://127.0.0.1:8000/api/contact?email="+encodeURIComponent(mail)+"&username="+encodeURIComponent(name),
    {method:"POST"}
);
    console.log(JSON.stringify({
        email: mail,
        username: name
        }
    ));
    return false;
}
