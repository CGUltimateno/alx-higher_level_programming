/**
 * Script that updates the text of the HTML tag HEADER to
 * New Header!!! when the user clicks on DIV#update_header
 * You can’t use document.querySelector to select the HTML tag
 */
$('DIV#update_header').on('click', () => {
    $('header').text('New Header!!!');
}