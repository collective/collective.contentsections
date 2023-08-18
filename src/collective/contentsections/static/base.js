jQuery(document).ready(function ($) {
  /*** Encapsulate youtube videos inserted with an iframe in HTMLSection to adjust the width ***/
  $(".section-htmlsection iframe").each(function () {
    $(this).wrap('<div class="iframe-container"></div>');
  });

  /*** Workaround to fix "Add item to default page" modal (https://github.com/plone/plone.app.contentmenu/issues/54) ***/
  $("a#plone-contentmenu-add-to-default-page").attr(
    "data-pat-plone-modal",
    '{"actionOptions": {"disableAjaxFormSubmit": true}}'
  );
});
