$(function() {
  $("#search").autocomplete({
    source: "/search_prods/",
    minLength: 2,
    select: function( event, ui ) {
      window.location.href = '/home/'.concat(ui.item.cat, '/', ui.item.id);
    },
  });
});
