$(document).ready(function () {
    // Initialize UI
    $('#btn-predict').hide();
    $('.loader').hide();
    $('#output-title').hide();
    $('#result').hide();
    $('#thank-you').hide();
    $('#imagePreview').hide();

    // Function to read and preview the uploaded image
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                // Display image in the preview
                $('#imagePreview')
                    .css('background-image', 'url(' + e.target.result + ')')
                    .hide()
                    .fadeIn(650); // Smooth fade-in animation
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    // Handle file input change
    $("#imageUpload").change(function () {
        // Show the predict button after an image is uploaded
        $('#btn-predict').show();
        $('#imagePreview').show();
        $('#output-title').hide();
        $('#result').hide().text('');
        $('#thank-you').hide();
        $('.loader').hide();

        // Preview the uploaded image
        readURL(this);
    });

    // Handle Predict Button Click
    $('#btn-predict').click(function () {
        // Prepare the API call
        var formData = new FormData();
        var fileInput = $('#imageUpload')[0].files[0];
        if (!fileInput) {
            alert("Please upload an image before predicting.");
            return;
        }
        formData.append('file', fileInput); // Match the key 'file' with Flask's app.py

        // Show loader
        $('#btn-predict').hide();
        $('.loader').show();

        // API call
        $.ajax({
            url: '/predict', // The prediction endpoint in app.py
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function (response) {
                // Handle the API response
                $('.loader').hide();
                $('#output-title').fadeIn().text("Prediction Result:");
                $('#result')
                    .fadeIn()
                    .html(`
                        <strong>Disease:</strong> ${response.predicted_label}
                    `); // Display class and label
                $('#thank-you').fadeIn().text("Thank you for using our Disease Detection system!");
            },
            error: function (xhr, status, error) {
                // Handle errors
                $('.loader').hide();
                alert("An error occurred: " + xhr.responseJSON?.error || error);
                $('#btn-predict').show();
            }
        });
    });
});