""" FaqEntry ContentType  """

from interfaces import IFaqEntry
from zope.interface import implements
from Products.Archetypes.public import Schema, StringWidget, TextAreaWidget, \
    VisualWidget, registerType, StringField, TextField, BaseSchema, \
     BaseContent


schema = BaseSchema + Schema((

    StringField('title',
                required=1,
                searchable=1,
                default='',
                accessor='Title',
                widget=StringWidget(label_msgid="label_question",
                            label='Question',
                            description="The frequently asked question.",
                            description_msgid="desc_question",
                            i18n_domain="faq"),
                ),

   TextField('description',
             required=0,
             searchable=1,
             accessor='Description',
             widget=TextAreaWidget(label='Detailed Question',
                   label_msgid='label_detailed_question',
                   description='More details on the question, ' +\
                    'if not evident from the title.',
                   description_msgid="desc_detailed_question",
                   i18n_domain='faq'),
             ),

    TextField('answer',
              primary=1,
              required=1,
              searchable=1,
              default_content_type="text/html",
              default_output_type='text/x-html-safe',
              allowable_content_types=("text/plain", "text/structured",
                                         "text/restructured", "text/html"),
              widget=VisualWidget(label='Answer',
                      label_msgid="label_answer",
                      description="Meaningful sentences that " + \
                          "explains the answer.",
                      description_msgid="desc_answer",
                      i18n_domain="faq",
                      width='100%',
                      rows=10),
              ),
    ))


class FaqEntry(BaseContent):

    implements(IFaqEntry)

    meta_type = "FaqEntry"
    schema = schema
    _at_rename_after_creation = True


registerType(FaqEntry, 'Products.Faq')
