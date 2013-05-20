/*
function random_crew(number) {
    var $crew_li = $('ul.crew li.crew');
    if (number === undefined) {
        var number = Math.floor((Math.random() * $crew_li.size()) - 1);
    }
    var $crew_first = $crew_li.eq(number);
    $crew_first.siblings().removeClass('first');
    $crew_first.addClass('first');
}

$('ul.crew li.crew').click(function () {
    random_crew($(this).index());
});
random_crew();


*/

$('ul.crew li.recruit').click(function () {
    $('#recruit').slideToggle(1000);
});