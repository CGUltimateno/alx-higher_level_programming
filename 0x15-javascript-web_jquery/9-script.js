/**
 * Fetches and prints how to say “Hello” depending on the language
 */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
}