const checkIfUserExists = (event) =>{
    //const registrationForm = document.forms['registration-form']
    const emailformElement = event.target
    const email = event.target.value
    axios.post('/validate-doctor-registration', {
        email: email
    })
    .then((response) => {
        if(response.data.user_exists == "true"){
            emailformElement.setCustomValidity("This User Already Exists, please login instead")
            emailformElement.reportValidity()
        }
    }, (error) =>{
        console.log(error)
    })
}