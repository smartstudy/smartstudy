function random_crew(number) {
    var $crew_li = $('ul.crew li');
    if (!number) {var number = Math.floor((Math.random()*$crew_li.size())-1);}
    var $crew_first = $crew_li.eq(number).html();
    $('div.crew_first').empty().append($crew_first);
}
random_crew();

$('ul.crew li').hover(function () {
    random_crew($(this).index());
});

