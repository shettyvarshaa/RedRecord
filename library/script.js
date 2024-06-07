document.querySelector('.add-subject').addEventListener('click', function() {
    var newSubject = prompt('Please enter the new subject:');
    if (newSubject) {
        alert('You added a new subject: ' + newSubject);
    }
});