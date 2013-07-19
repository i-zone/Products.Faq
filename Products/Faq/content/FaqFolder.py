""" Faq Folder Class """

from interfaces import IFaqFolder
from zope.interface import implements
from Products.ATContentTypes.atct import ATFolder, ATFolderSchema
from Products.Archetypes.public import IntegerField, Schema, \
                                       IntegerWidget, registerType, \
                                       TextField, RichWidget

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
        default_output_type="text/html",
        allowable_content_types=("text/html",
                                 "text/plain",
                                 "text/restructured"),
        widget  = RichWidget,
        ),
    ))

schema['description'].widget.label = _(u"label_folder", default=u"Description")
schema['description'].widget.description = _(u"desc_folder",
                                  default=u"The description of the FAQ category.")

class FaqFolder(ATFolder):
    """ FAQ Folder """

    implements(IFaqFolder)

    schema = schema

registerType(FaqFolder, config.PROJECTNAME)
