Changelog
=========

1.0.0a22 (2024-02-06)
---------------------

- Remove bootstrap carousel ride. [sverbois]
- Use h-100 class on card macro. [sverbois]
- Add Section primary/secondary/black items to section_css_classes taxonomy. [sverbois]
- Change element view view to redirect to parent folder_contents view. [sverbois]


1.0.0a21 (2023-12-31)
---------------------

- Fix date isoformat in collection section. [sverbois]


1.0.0a20 (2023-12-31)
---------------------

- Fix end_date field in selection view. [sverbois]
- Improve Bootstrap card component with bigger titles, publication date and event dates. [sverbois]
- Improve section ordering drag and drop. [sverbois]

1.0.0a19 (2023-12-25)
---------------------

- Add content type icons. [sverbois]
- Sort sections by position in parent. [sverbois]
- Hide Plone toolbar on Spotlight.js view. [sverbois]


1.0.0a18 (2023-08-23)
---------------------

- Disable workflow on ContactsSection and Contact content type. [sverbois]
- Fix empty Locations section with zoom value. [sverbois]


1.0.0a17 (2023-08-19)
---------------------

- Add Contacts section and Contact content type. [sverbois]


1.0.0a16 (2023-08-19)
---------------------

- Add Locations section and Location element base on pat-leaflet. [sverbois]
- Modify content type names to avoid confusion with Plone's default content types. [sverbois]
- Add plone.formwidget.geolocation >= 3.0.5 dependency. [sverbois]
- Add a Javascript workaround to fix "Add item to default page". [sverbois]
- Use Python 3.11 and Plone 6.0.6 in development buildout. [sverbois]
- Add NewsPage content type. [sverbois]

1.0.0a15 (2023-01-01)
---------------------

- Use Plone 6 final in development buildout. [sverbois]
- Transform internal (resolveuid) links before rendering LinksSection. [sverbois]

1.0.0a14 (2022-12-11)
---------------------

- Set load_defer key to True for resource bundles. [sverbois]
- Use Plone 6 beta 3 in development buildout. [sverbois]
- Update TinyMCE registry profile to TinyMCE 5. [sverbois]
- Add a shortcut in actions menu to add content in sections. [sverbois]
- Use "Card view" as default view for "Images section". [sverbois]
- Move "group_size" field to "default" fieldset. [sverbois]

1.0.0a13 (2022-08-21)
---------------------

- Add a CSS class on each section with the section view template id. [sverbois]
- Add a hide_item_titles field on links sections. [sverbois]
- Allow "Group size" of 6 items. [sverbois]
- Add control buttons and optional title section on card and carousel templates. [sverbois]

1.0.0a12 (2022-08-16)
---------------------

- Remove customized plone.allowed_sizes and plone.toolbar_position configurations. [sverbois]
- Set boolean fields required option to False. [sverbois]
- Require version 3 of collective.taxonomy and collective.z3cform.datagridfield. [sverbois]
- Improve CSS for section full-width managment and card section edition. [sverbois]

1.0.0a11 (2022-03-26)
---------------------

- Add hide_title field on IPage. [sverbois]

1.0.0a10 (2022-03-26)
---------------------

- Allow BasicPage as default page type. [sverbois]
- Remove layout name in item_lead_image_scale method. [sverbois]

1.0.0a9 (2021-12-30)
--------------------

- Allow Python 3.7 as Plone 6. [sverbois]
- Use Plone 6 alpha 2 in development buildout. [sverbois]

1.0.0a8 (2021-12-22)
--------------------

- Use a collective.taxonomy to manage the available section CSS classes. [sverbois]

1.0.0a7 (2021-12-22)
--------------------

- Add model Archimate view. [sverbois]
- Remove remote_url field on CardsSection. We can use the relation_uid field with a Link content. [sverbois]
- Add a Card carousel view on sections. [sverbois]
- Add container width option on sections. [sverbois]

1.0.0a6 (2021-12-20)
--------------------

- Use pat-sortable pattern to reorder sections in a page using drag and drop. [sverbois]

1.0.0a5 (2021-12-19)
--------------------

- Remove the use of accordion in edit forms. [sverbois]
- Remove the row prototype. We want a KISS product. [sverbois]

1.0.0a4 (2021-12-19)
--------------------

- Add tags information in section view which contains context subjects field value. [sverbois]
- Clean up the list of behaviours on content types. [sverbois]
- Don't hide *contentleadimage* viewlet. [sverbois]

1.0.0a3 (2021-12-18)
--------------------

- Add a demo.json export of collective.exportimport with demo pages. [sverbois]
- Clean use of default and missing_value field attributes. [sverbois]

1.0.0a2 (2021-12-17)
--------------------

- Add Event Page portal type. [sverbois]

1.0.0a1 (2021-12-17)
--------------------

- Initial release [sverbois]
