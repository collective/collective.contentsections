jQuery(document).ready(function ($) {

    /***  Encapsulate youtube videos inserted with an iframe in HTMLSection to adjust the width ***/
    $('.section-htmlsection iframe[src^="https://www.youtube.com/embed/"]').each(function () {
        $(this).wrap('<div class="youtube-iframe-container"></div>');
    });

});
