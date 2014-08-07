$(function(){
    $("#add-player-form").bind('ajax:complete', function(){
	this.reset(); 
    });
});