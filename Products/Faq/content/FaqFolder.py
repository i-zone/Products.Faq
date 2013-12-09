""" Faq Folder Class """

from interfaces import IFaqFolder
from zope.interface import implements
from Products.ATContentTypes.atct import ATFolder, ATFolderSchema
from Products.Archetypes.public import Schema, registerType
from Products.Archetypes.atapi import *

from Products.Faq import config
from Products.Faq import faqMessageFactory as _


schema = ATFolderSchema.copy() + Schema((

    IntegerField('delay',
                 widget=IntegerWidget(description=_(u"desc_delay",
                                      default=u"Delay for a new item."),
                                      label=_(u"label_delay", default=u"Delay")
                        ),
                 default=0,
                 required=1,
                 searchable=0,
                 validators=('isInt',)),

    TextField("text",
        required=0,
        searchable=1,
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default_output_type='text/html',
        validators=("isTidyHtmlWithCleanup",),
        widget = RichWidget(
            label='Anlesertext',
            label_msgid='faqfolder_label_text',
            i18n_domain='faqfolder',
            description='', 
            rows=20,
            allow_file_upload=False,),
        )
    ))

schema['description'].widget.label = _(u"label_folder", default=u"Description")
schema['description'].widget.description = _(u"desc_folder",
                                  default=u"The description of the FAQ category.")

class FaqFolder(ATFolder):
    """ FAQ Folder """

    implements(IFaqFolder)

    schema = schema

registerType(FaqFolder, config.PROJECTNAME)
