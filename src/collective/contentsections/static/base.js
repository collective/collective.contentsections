jQuery(document).ready(function ($) {

    /***  Encapsulate youtube videos inserted with an iframe in HTMLSection to adjust the width ***/
    $('.section-htmlsection iframe').each(function () {
        $(this).wrap('<div class="iframe-container"></div>');
    });

});
