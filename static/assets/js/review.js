// review modal
    $(document).ready(function() {
        $('#review-form').submit(function(event) {
            event.preventDefault();
            
            var formData = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: '{% url "add_review" %}',
                data: formData,
                success: function(response) {
                    // handle success response
                },
                error: function(response) {
                    // handle error response
                }
            });
        });
    });
