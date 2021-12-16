jQuery(document).ready(function ($) {

    // Toggle on add / edit forms fieldsets

    // 1. hide default fieldset legend (ckass : expanded)
    $("form.accordion-form fieldset:first legend").hide();
    $("form.accordion-form fieldset:first legend").addClass("expanded");

    // 2. hide all fieldsets content except first (class : collapsed)
    $("form.accordion-form fieldset:not(:first) legend").siblings().hide();
    $("form.accordion-form fieldset:not(:first) legend").addClass("collapsed");

    // 3. add toggle on all fieldsets legends & toggle expanded / collapsed classes
    $("form.accordion-form fieldset:not(:first) legend").click(function () {
        var legend = $(this);
        var changed_class = false;
        $(this).siblings().slideToggle("fast", function () {
            if (!changed_class) {
                legend.toggleClass("collapsed");
                legend.toggleClass("expanded");
                changed_class = true;
            }
        });
    });
});

