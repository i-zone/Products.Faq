try:
    from plone.app.folder.migration import BTreeMigrationView
    HAS_FOLDER = True
except ImportError:
    HAS_FOLDER = False

def upgrade_1000_to_1001(portal_setup):
    if not HAS_FOLDER:
        return

    view = BTreeMigrationView(self, REQUEST)
    for brain in self.portal_catalog(portal_type='FaqFolder'):
         obj = brain.getObject()
         view.migrate(obj)
