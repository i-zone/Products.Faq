""" Faq Folder Class """

from interfaces import IFaqFolder
from zope.interface import implements
from Products.Archetypes.public import IntegerField, TextField, \
    BaseFolderSchema, Schema, TextAreaWidget, IntegerWidget, registerType, \
    OrderedBaseFolder


schema = BaseFolderSchema + Schema((
    TextField('description',
              widget=TextAreaWidget(description_msgid="desc_folder",
                        description="The description of the FAQ category.",
                        label_msgid="label_folder",
                        label="Description",
                        i18n_domain="faq",
                        rows=6)),
    IntegerField('delay',
                 widget=IntegerWidget(description="Delay for a new item.",
                                      description_msgid="desc_delay",
                                      label_msgid="label_delay",
                                      label="Delay",
                                      i18n_domain="faq"),
                 default=7,
                 required=1,
                 searchable=0,
                 validators=('isInt',)),
    ))


class FaqFolder(OrderedBaseFolder):
    """A simple folderish archetype Folder"""

    implements(IFaqFolder)

    meta_type = "FaqFolder"
    schema = schema
    _at_rename_after_creation = True

registerType(FaqFolder, 'Products.Faq')
