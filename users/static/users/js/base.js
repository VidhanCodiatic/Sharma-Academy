var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 100000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 4;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    
    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        
        next.children(':first-child').clone().appendTo($(this));
      }
});


$('#courseid').onClick(function (e) {
  e.preventDefault();

  $.ajax({
    type: "GET",
    url: "{% url 'showcourses' %}",
    success:function(response){ 
      alert('showed'); 
    },
    error: function(response){
      alert('error');
    },
  }) 
});